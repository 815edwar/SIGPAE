from django.views.generic import TemplateView
from sigpaeHistoricos.forms import *
from django.shortcuts import render_to_response, redirect
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

    def post(self, request, *args, **kwargs):
        post_values = request.POST.copy()
        print(post_values)


class NewPdf(TemplateView):
    template_name = 'pdf.html'

    def get_context_data(self, **kwargs):
        context = super(NewPdf, self).get_context_data(**kwargs)
        context['formulario'] = AddPdfForm()

        return context

    def post(self, request, *args, **kwargs):

        post_values = request.POST.copy()

        pdfForm = AddPdfForm(post_values, request.FILES)

        if pdfForm.is_valid():
            newpdf = pdfForm.save()
<<<<<<< HEAD
            print(newpdf.pdf.url)
            text = extract_text(newpdf.pdf.url)
=======
            print("\n\n\n\n\n" + newpdf.pdf.url + "\n\n\n\n\n")
            print(newpdf)
            text = extract_text('SIGPAE/'+newpdf.pdf.url)
>>>>>>> fc17003fa3cdcf48ddd7a619681aaf0302677a44
            newpdf.text = text.getvalue()
            newpdf.save()
            context = {'formulario': PdfForm(instance=newpdf), 'pdf': newpdf}
            return redirect('DisplayPDF', newpdf.id)
        else:
            context = {'formulario': pdfForm}

            return render_to_response('pdf.html', context)


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
