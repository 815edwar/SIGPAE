# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from sigpaeHistoricos.forms import *
from django.shortcuts import render, render_to_response, redirect
import io
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import os
import re
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.messages import get_messages
import datetime



class HomeView(TemplateView):
    template_name = 'home.html'

class PDFList(TemplateView):
    template_name = 'transcripciones_en_proceso.html'
    
    def get_context_data(self, **kwargs):
        context = super(PDFList, self).get_context_data(**kwargs)

        programas = Pdfs.objects.all()
        context['programas'] = programas
        pdf_names = []
        for programa in programas:
            nombre_pdf = programa.pdf.url.split('/')[-1]
            pdf_names.append(nombre_pdf)
        context['pdf_names'] = pdf_names
        return context

class ModifyPDF(TemplateView):
    template_name = 'display_pdf.html'

    def get_context_data(self, **kwargs):
        context = super(ModifyPDF, self).get_context_data(**kwargs)
        pdf = Pdfs.objects.get(pk=int(kwargs['pk']))
        pdf_form = PdfForm(instance=pdf)
        context['formulario'] = pdf_form
        context['pdf'] = pdf
        print(pdf.encargado)
        context['encargado'] = pdf.encargado
        
        return context

    @staticmethod
    def post(request, **kwargs):
        post_values = request.POST.copy()
        print(post_values)
        pdf_id = int(post_values['pdf_id'])
        pdf = Pdfs.objects.get(id=pdf_id)
        pdf_form = PdfForm(post_values, instance=pdf)
        if pdf_form.is_valid():
            if post_values['check'] == 'Departamento':
                pdf.encargado = post_values['departamentos']
                pdf.save()
            elif post_values['check'] == 'Coordinacion':
                print('entre')
                pdf.encargado = post_values['coordinacion']
                pdf.save()
            
            pdf_form.save()
            return redirect('home')
        else:
            context = {'formulario': pdf_form, }
            context['pdf'] = pdf
            return render(request, 'display_pdf.html', context)

class DisplayPDF(TemplateView):
    template_name = 'display_pdf.html'

    def get_context_data(self, **kwargs):
        context = super(DisplayPDF, self).get_context_data(**kwargs)
        messages = get_messages(self.request)
        for message in messages:
            pdf_id = int(str(message))
        messages.used = True
        pdf = Pdfs.objects.get(id=pdf_id)
        pdf_form = PdfForm(instance=pdf)
        context['formulario'] = pdf_form
        context['pdf'] = pdf
        context['encargado'] = None
        return context

    @staticmethod
    def post(request):
        post_values = request.POST.copy()
        pdf_id = int(post_values['pdf_id'])
        pdf = Pdfs.objects.get(id=pdf_id)
        pdf_form = PdfForm(post_values, instance=pdf)
        if pdf_form.is_valid():
            if post_values['check'] == 'Departamento':
                pdf_form.encargado = post_values['departamentos']
                pdf_form.save()
            elif post_values['check'] == 'Coordinacion':
                pdf_form.encargado = post_values['departamentos']
                pdf_form.save()
            else:
                pdf_form.save()
            return redirect('home')
        else:
            context = {'formulario': pdf_form, }
            context['pdf'] = pdf
            return render(request, 'display_pdf.html', context)

class NewPdf(TemplateView):
    template_name = 'pdf.html'

    def get_context_data(self, **kwargs):
        context = super(NewPdf, self).get_context_data(**kwargs)
        context['formulario'] = AddPdfForm()

        return context

    @staticmethod
    def post(request):

        post_values = request.POST.copy()

        pdf_form = AddPdfForm(post_values, request.FILES)

        if pdf_form.is_valid():
            newpdf = pdf_form.save()
            if post_values['tipo'] == 'texto':
                text = extract_text('SIGPAE/'+newpdf.pdf.url)
            else:
                text = extract_html('SIGPAE/'+newpdf.pdf.url)

            newpdf.texto = text

            newpdf.save()
            messages.add_message(request, messages.INFO, str(newpdf.id) )
            newpdf.codigo = match_codigo_asig(text)
            newpdf.save()
            if newpdf.codigo != None:
                match_dpto(newpdf.codigo)

            return redirect('mostrar_pdf')
        else:
            pdf_form = AddPdfForm(post_values, request.FILES)
            context = {'formulario': pdf_form}

            return render(request, 'pdf.html', context)


def extract_text(path):
    os.system("pdftotext -layout " + path)
    filename = re.sub('(p|P)(d|D)(f|F)', 'txt', path)
    file = open(filename, "r")
    text = file.read()
    file.close()
    os.system("rm " + filename)
    return text


def Encargado(request):
    encargado = request.GET.get('encargado', None)
    decanato = request.GET.get('decanato', None)
    if encargado == 'Departamento':
        departamentos = list(Departamento.objects.all().values())
        data = {
            'departamento' : departamentos
        }
    elif encargado == "Coordinacion":
        decanatos = list(Decanato.objects.all().values())
        data = {
            'decanatos' : decanatos
        }
    else: 
        coordinaciones = list(Coordinacion.objects.filter(decanato=int(decanato)).values())
        data = {
            'coordinaciones': coordinaciones
        }

    return JsonResponse(data)

        


def extract_html(path):
    os.system("pdftohtml -s -c " + path)
    output = re.sub('.(p|P)(d|D)(f|F)', '-html.html', path)
    file = open(output, "r")
    text = file.read()
    file.close()
    os.system("rm " + output + ' *.png')
    return text

def match_codigo_asig(text):
    expresion = '([A-Z][A-Z](-|\s|)[0-9][0-9][0-9][0-9])|([A-Z][A-Z][A-Z](-|\s|)[0-9][0-9][0-9])'
    patron=re.compile(expresion)
    matcher = patron.search(text)
    if matcher != None:
        print ("El código asociado al programa es " + matcher.group(0))
        return matcher.group(0)
    else:
        print ("No se encontró código")
        return None

def match_dpto(codigo):
    expresion = '[A-Z][A-Z]|[A-Z][A-Z][A-Z]'
    patron=re.compile(expresion)
    matcher = patron.search(codigo)
    if matcher != None:
        if matcher.group(0) == "CI" or  matcher.group(0) == "CIB":
            print ("El dpto es Computacion")
            return matcher.group(0)
        else:
            print ("No se consiguó dpto")
            return None
        

    