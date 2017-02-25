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
        print("\n\n\n\n\n")
        print(context['pdf_names'])
        return context

class ModifyPDF(TemplateView):
    template_name = 'display_pdf.html'

    def get_context_data(self, **kwargs):
        context = super(ModifyPDF, self).get_context_data(**kwargs)
        pdf = Pdfs.objects.get(pk=int(kwargs['pk']))
        pdf_form = PdfForm(instance=pdf)
        context['formulario'] = pdf_form
        context['pdf'] = pdf
        return context

    @staticmethod
    def post(request, **kwargs):
        post_values = request.POST.copy()
        pdf_id = int(post_values['pdf_id'])
        pdf = Pdfs.objects.get(id=pdf_id)
        pdf_form = PdfForm(post_values, instance=pdf)
        pdf_form.save()
        return redirect('home')

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
        return context

    @staticmethod
    def post(request):
        post_values = request.POST.copy()
        pdf_id = int(post_values['pdf_id'])
        pdf = Pdfs.objects.get(id=pdf_id)
        pdf_form = PdfForm(post_values, instance=pdf)
        pdf_form.save()
        return redirect('home')

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
            text = extract_text('SIGPAE/'+newpdf.pdf.url)
            newpdf.texto = text
            newpdf.save()
            messages.add_message(request, messages.INFO, str(newpdf.id) )
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

    '''
    pdfFile = open(path, 'rb')
    retstr = io.StringIO()
    password = ''
    pagenos = set()
    maxpages = 0
    laparams = LAParams()
    rsrcmgr = PDFResourceManager()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    process_pdf(rsrcmgr, device, pdfFile, pagenos, maxpages=maxpages, password=password, check_extractable=True)
    device.close()
    pdfFile.close()
    return retstr
    '''
