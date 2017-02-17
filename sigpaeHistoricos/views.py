# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from sigpaeHistoricos.forms import *
from django.shortcuts import render, render_to_response
import io
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams


class HomeView(TemplateView):
    template_name = 'home.html'


class DisplayPDF(TemplateView):
    template_name = 'display_pdf.html'

    def get_context_data(self, **kwargs):
        context = super(DisplayPDF, self).get_context_data(**kwargs)

        return context

    @staticmethod
    def post(request):
        post_values = request.POST.copy()
        print(post_values)


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
            newpdf.texto = text.getvalue()
            newpdf.save()
            context = {'formulario': PdfForm(instance=newpdf), 'pdf': newpdf}
            return render_to_response('display_pdf.html', context)
        else:
            pdf_form = AddPdfForm(post_values, request.FILES)
            context = {'formulario': pdf_form}

            return render(request, 'pdf.html', context)


def extract_text(path):
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
