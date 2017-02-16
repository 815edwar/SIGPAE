from django.conf.urls import url
from django.contrib import admin
from sigpaeHistoricos.views import *

urlpatterns = [
	url(r'^mostrar_pdf/$', DisplayPDF.as_view(), name='mostrar_pdf'),
	url(r'^agregar_pdf/$', NewPdf.as_view(), name='agregar_pdf'),
]