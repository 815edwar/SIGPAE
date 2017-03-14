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
            context = {'formulario': pdf_form, 'pdf': pdf}
            return render(request, 'display_pdf.html', context)


class DisplayPDF(TemplateView):
    template_name = 'display_pdf.html'

    def get_context_data(self, **kwargs):
        context = super(DisplayPDF, self).get_context_data(**kwargs)
        msgs = get_messages(self.request)
        pdf_id = -1
        for message in msgs:
            pdf_id = int(str(message))
        msgs.used = True
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
                pdf.encargado = post_values['departamentos']
                pdf.save()
            elif post_values['check'] == 'Coordinacion':
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
            if post_values['tipo'] == 'texto':
                text = extract_text('SIGPAE/' + newpdf.pdf.url)
            else:
                text = extract_text_from_image('SIGPAE/' + newpdf.pdf.url)

            print(text)
            newpdf.texto = text
            newpdf.save()
            messages.add_message(request, messages.INFO, str(newpdf.id))
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
