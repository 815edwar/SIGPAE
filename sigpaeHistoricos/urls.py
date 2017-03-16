from django.conf.urls import url
from sigpaeHistoricos.views import *
from . import views

urlpatterns = [
    url(r'^mostrar_pdf/$', DisplayPDF.as_view(), name='mostrar_pdf'),
    url(r'^agregar_pdf/$', NewPdf.as_view(), name='agregar_pdf'),
    url(r'^pdf_list/$', PDFList.as_view(), name='pdf_list'),
    #url(r'^programa_list/$', ProgramaList.as_view(), name='programa_list'),
    url(r'^ajax/encargado/$', views.encargado, name='encargado'),
    #url(r'^program_detail/(?P<pk>\d+)/$', DisplayProgram.as_view(), name="program_details")

]
