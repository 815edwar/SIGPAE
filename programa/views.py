from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect, render_to_response
from programa.forms import *
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse

class HomeView(TemplateView):
    template_name = 'base.html'

class NewPdf(TemplateView):
    
    template_name = 'pdf.html'

    def get_context_data(self, **kwargs):
        context = super(NewPdf, self).get_context_data(**kwargs)
        context['formulario'] = PdfForm()

        return context

    def post(self, request, *args, **kwargs):

        post_values = request.POST.copy()

        pdfForm = PdfForm(post_values,request.FILES)

        if pdfForm.is_valid():
            newpdf = pdfForm.save()
            return HttpResponseRedirect(reverse_lazy('pdf'))
        else:
            context = {'formulario': pdfForm}

            return render_to_response('pdf.html', context)
