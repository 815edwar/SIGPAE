from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

class DisplayPDF(TemplateView):
	template_name = 'display_pdf.html'

	def get_context_data(self, **kwargs):
		context = super(DisplayPDF, self).get_context_data(**kwargs)

		context['pdf'] = "a.pdf"

		return context