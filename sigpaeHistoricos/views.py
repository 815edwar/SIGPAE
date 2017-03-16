# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from sigpaeHistoricos.forms import *
from django.shortcuts import render, redirect
import io
import os
import re
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.messages import get_messages
from wand.image import Image
from PIL import Image as Pi
import pyocr
import pyocr.builders


class HomeView(TemplateView):
    template_name = 'home.html'



class ProgramaList(TemplateView):
    template_name = 'programas.html'

    def get_context_data(self, **kwargs):
        context = super(ProgramaList, self).get_context_data(**kwargs)
        programas = Programa.objects.all()
        context['programas'] = programas
        return context

class DisplayProgram(TemplateView):
    template_name = "display_program.html"

    def get_context_data(self,**kwargs):
        context= super(DisplayProgram,self).get_context_data(**kwargs)
        programa = Programa.objects.get(pk=kwargs['pk'])
        horas_semanales = programa.horas_practica + programa.horas_teoria + programa.horas_laboratorio 
        context['programa'] = programa
        context['horas_semanales'] = horas_semanales
        return context


class PDFList(TemplateView):
    template_name = 'transcripciones_en_proceso.html'

    def get_context_data(self, **kwargs):
        context = super(PDFList, self).get_context_data(**kwargs)

        programas = Transcripcion.objects.all()
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
        context = super(ModifyPDF, self).get_context_data()
        pdf = Transcripcion.objects.get(pk=int(kwargs['pk']))
        pdf_form = PdfForm(instance=pdf)

        expresion = '[A-Z][A-Z]|[A-Z][A-Z][A-Z]'
        patron = re.compile(expresion)
        matcher = patron.search(pdf.codigo)
        codigo = matcher.group(0)

        prefijo = Prefijo.objects.filter(siglas=codigo)[0]
        if prefijo != None:
            print(prefijo.asociacion)
            context['prefijo'] = prefijo
        context['formulario'] = pdf_form
        context['pdf'] = pdf
        context['encargado'] = pdf.encargado

        return context

    @staticmethod
    def post(request, **kwargs):
        post_values = request.POST.copy()
        print(post_values)
        pdf_id = int(post_values['pdf_id'])
        pdf = Transcripcion.objects.get(id=pdf_id)
        pdf_form = PdfForm(post_values, instance=pdf)
        if pdf_form.is_valid():
            if 'check' in post_values and post_values['check'] == 'Departamento':
                pdf.encargado = post_values['departamentos']
                pdf.save()
            elif 'check' in post_values and post_values['check'] == 'Coordinacion':
                pdf.encargado = post_values['coordinacion']
                pdf.save()
            else:
                pdf_form.save()
            return redirect('home')
        else:
            context = {'formulario': pdf_form, 'pdf': pdf}
            return render(request, 'display_pdf.html', context)


class DisplayPDF(TemplateView):
    template_name = 'display_pdf.html'

    def get_context_data(self):
        context = super(DisplayPDF, self).get_context_data()
        msgs = get_messages(self.request)
        pdf_id = -1
        for message in msgs:
            pdf_id = int(str(message))
        msgs.used = True
        pdf = Transcripcion.objects.get(id=pdf_id)
        pdf_form = PdfForm(instance=pdf)
        context['formulario'] = pdf_form
        context['pdf'] = pdf
        context['encargado'] = None
        return context

    @staticmethod
    def post(request):
        post_values = request.POST.copy()
        pdf_id = int(post_values['pdf_id'])
        pdf = Transcripcion.objects.get(id=pdf_id)
        pdf_form = PdfForm(post_values, instance=pdf)
        if pdf_form.is_valid():
            if 'check' in post_values and post_values['check'] == 'Departamento':
                pdf.encargado = post_values['departamentos']
                pdf.save()
            elif 'check' in post_values and post_values['check'] == 'Coordinacion':
                pdf.encargado = post_values['coordinacion']
                pdf.save()
            else:
                pdf_form.save()
            return redirect('home')
        else:
            context = {'formulario': pdf_form, 'pdf': pdf}
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
            print(newpdf.pdf.url)
            if post_values['tipo'] == 'texto':
                text = extract_text('SIGPAE/' + newpdf.pdf.url)
            else:
                text = extract_text_from_image('SIGPAE/' + newpdf.pdf.url)

            print(text)
            newpdf.texto = text

            newpdf.save()
            messages.add_message(request, messages.INFO, str(newpdf.id))
            newpdf.codigo = match_codigo_asig(text)
            newpdf.save()
            if newpdf.codigo is not None:
                match_dpto(newpdf.codigo)
            return redirect('mostrar_pdf')
        else:
            pdf_form = AddPdfForm(post_values, request.FILES)
            context = {'formulario': pdf_form}

            return render(request, 'pdf.html', context)


def extract_text(path):
    os.system("pdftotext -layout " + path)
    filename = re.sub('(p|P)(d|D)(f|F)', 'txt', path)
    print(filename)
    print("\n\n\n\n\n\n")
    file = open(filename, "r")
    text = file.read()
    file.close()
    os.system("rm " + filename)
    return text


def extract_text_from_image(path):
    tool = pyocr.get_available_tools()[0]
    lang = tool.get_available_languages()[0]

    req_image = []
    final_text = []

    image_pdf = Image(filename=path, resolution=200)
    image_jpeg = image_pdf.convert('jpeg')

    for img in image_jpeg.sequence:
        img_page = Image(image=img)
        req_image.append(img_page.make_blob('jpeg'))

    for img in req_image:
        txt = tool.image_to_string(Pi.open(io.BytesIO(img)),
                                   lang=lang,
                                   builder=pyocr.builders.TextBuilder()
                                   )
        final_text.append(txt)

    trancription = ''
    for i in final_text:
        trancription += i

    return trancription


def encargado(request):
    responsable = request.GET.get('encargado', None)
    decanato = request.GET.get('decanato', None)
    if responsable == 'Departamento':
        departamentos = list(Departamento.objects.all().values())
        data = {
            'departamento': departamentos
        }
    elif responsable == "Coordinacion":
        decanatos = list(Decanato.objects.all().values())
        data = {
            'decanatos': decanatos
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
    patron = re.compile(expresion)
    matcher = patron.search(text)
    if matcher is not None:
        print("El código asociado al programa es " + matcher.group(0))
        return matcher.group(0)
    else:
        print("No se encontró código")
        return None


def match_dpto(codigo):
    expresion = '[A-Z][A-Z]|[A-Z][A-Z][A-Z]'
    patron = re.compile(expresion)
    matcher = patron.search(codigo)
    if matcher is not None:
        if matcher.group(0) == "CI" or matcher.group(0) == "CIB":
            print("El dpto es Computacion")
            return matcher.group(0)
        else:
            print("No se consiguó dpto")
            return None
