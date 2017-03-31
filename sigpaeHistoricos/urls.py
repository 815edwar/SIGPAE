from django.conf.urls import url
from sigpaeHistoricos.views import *
from . import views

urlpatterns = [
    url(r'^mostrar_pdf/$', DisplayPDF.as_view(), name='mostrar_pdf'),
    url(r'^agregar_pdf/$', NewPdf.as_view(), name='agregar_pdf'),
    url(r'^pdf_list/$', PDFList.as_view(), name='pdf_list'),
    url(r'^programa_list/$', ProgramaList.as_view(), name='programa_list'),
    url(r'^pasa_list/$', PasaList.as_view(), name='pasa_list'),
    url(r'^aprobar_siglas/$', SiglasList.as_view(), name='siglas_list'),
    url(r'^program_detail/(?P<pk>\d+)/$', DisplayProgram.as_view(), name="program_details"),
    url(r'^pasa_detail/(?P<pk>\d+)/$', DisplayTranscripcion.as_view(), name="Transcripcion_details"),
    url(r'^mod_programa/(?P<pk>\d+)/$', ModifyPDF.as_view(), name='ModifyPDF'),

    url(r'^ajax/encargado/$', views.encargado, name='encargado'),
    url(r'^ajax/crearCampo/$', views.crear_campo, name='crearCampo'),
    url(r'^ajax/proponerTranscripcion/$', views.ProponerTranscripcion, name='ProponerTranscripcion'),
    url(r'^ajax/siglas/$', views.siglas, name='siglas'),

    


]
