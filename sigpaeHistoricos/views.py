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
        programas = Solicitud.objects.all()
        context['programas'] = programas
        return context

class DisplayProgram(TemplateView):
    template_name = "display_program.html"

    def get_context_data(self,**kwargs):
        context= super(DisplayProgram,self).get_context_data(**kwargs)
        solicitud = Solicitud.objects.get(pk=int(kwargs['pk']))
        programa = solicitud.programa
        horas_semanales = programa.h_prac + programa.h_teoria + programa.h_lab 
        context['programa'] = programa
        context['horas_semanales'] = horas_semanales
        context['solicitud'] = solicitud
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

class SiglasList(TemplateView):
    template_name = 'siglas_por_aprobar.html'

    def get_context_data(self, **kwargs):
        context = super(SiglasList, self).get_context_data(**kwargs)

        prefijos = Prefijo.objects.filter(aprobado=False)
        context['prefijos'] = prefijos

        return context


class ModifyPDF(TemplateView):
    template_name = 'display_pdf.html'

    def get_context_data(self, **kwargs):
        context = super(ModifyPDF, self).get_context_data()
        pdf = Transcripcion.objects.get(pk=int(kwargs['pk']))
        otro_campo = ContenidoExtra.objects.filter(transcripcion=pdf.id)
        pdf_form = PdfForm(instance=pdf)
        contenido_form = ContenidoFormSet()
        context['contenido'] = contenido_form
        context['formulario'] = pdf_form
        context['pdf'] = pdf
        context['encargado'] = pdf.encargado
        context['modifying'] = True
        context['nombres'] = CampoAdicional.objects.all();
        context['campos'] = otro_campo
        return context

    @staticmethod
    def post(request, **kwargs):
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

            campo = ContenidoExtra.objects.filter(transcripcion=pdf.id)
            print("\n\n\n\n")
            for c in campo:
                print("Entro en for con " + c.campo_adicional.nombre)
                if c.campo_adicional.nombre in post_values:
                    print("Entro en if")
                    c.contenido = post_values[c.campo_adicional.nombre]
                    c.save()

            if 'campo_adicional' in post_values:
                campos_adicionales = post_values.pop('campo_adicional')
                contenido_campos = post_values.pop('contenido_campos')
                print(campos_adicionales, contenido_campos)
                for i in range(len(campos_adicionales)):
                    if campos_adicionales[i] != "" and campos_adicionales[i] != "ninguna":
                        campo = CampoAdicional.objects.get(nombre=campos_adicionales[i])
                        ContenidoExtra.objects.create(transcripcion=pdf, campo_adicional=campo, 
                                                      contenido=contenido_campos[i])

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
        if pdf.codigo != None and pdf.codigo != '':
            print('entre')
            expresion = '[A-Z][A-Z][A-Z]|[A-Z][A-Z]'
            patron = re.compile(expresion)
            matcher = patron.search(pdf.codigo)
            prefijo = Prefijo.objects.filter(siglas = matcher.group(0))
            if prefijo.exists():
                prefijo = Prefijo.objects.filter(siglas = matcher.group(0))[0]
                departamento = Departamento.objects.filter(nombre = prefijo.asociacion) 
                if departamento.exists():
                    departamento = departamento[0]
                    context['departamento'] = departamento
                else:
                    context['prefijo'] = prefijo
            else:
                context['siglas'] = matcher.group(0)
                context['departamentos'] = Departamento.objects.all()
        elif pdf.codigo == '':
            context['modifying'] = True

        context['formulario'] = pdf_form
        context['pdf'] = pdf
        context['encargado'] = None
        context['nombres'] = CampoAdicional.objects.all();
        
        return context

    @staticmethod
    def post(request):
        post_values = request.POST.copy()
        if 'siglas' in post_values:    
            if(post_values['siglas'] != ''):
                prefijo_nuevo = Prefijo.objects.create(siglas = post_values['siglas'],
                                                       asociacion = post_values['asociacion'], 
                                                       aprobado = False)
                prefijo_nuevo.save()
        elif 'siglas2' in post_values:    
            if(post_values['siglas2'] != ''):
                prefijo_nuevo = Prefijo.objects.create(siglas = post_values['siglas2'],\
                    asociacion ="", aprobado = False)
                prefijo_nuevo.save()
        pdf_id = int(post_values['pdf_id'])
        pdf = Transcripcion.objects.get(id=pdf_id)
        pdf_form = PdfForm(post_values, instance=pdf)
        print(post_values['encargado1'] )
        print('\n\n\n\n\n')
        if pdf_form.is_valid():
            if 'check' in post_values and post_values['check'] == 'Departamento':
                pdf.encargado = post_values['departamentos']
                pdf.save()
            elif 'check' in post_values and post_values['check'] == 'Coordinacion':
                pdf.encargado = post_values['coordinacion']
                pdf.save()
            else:
                pdf.encargado = post_values['encargado1']   
                pdf_form.save()

            if 'campo_adicional' in post_values:
                campos_adicionales = post_values.pop('campo_adicional')
                contenido_campos = post_values.pop('contenido_campos')
                print(campos_adicionales, contenido_campos)
                for i in range(len(campos_adicionales)):
                    if campos_adicionales[i] != "" and campos_adicionales[i] != "ninguna":
                        campo = CampoAdicional.objects.get(nombre=campos_adicionales[i])
                        ContenidoExtra.objects.create(transcripcion=pdf, campo_adicional=campo, 
                                                      contenido=contenido_campos[i])

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

            newpdf.texto = text

            newpdf.save()
            messages.add_message(request, messages.INFO, str(newpdf.id))

            if post_values['extraer'] == 'si':
                newpdf.codigo = match_codigo_asig(text)
                newpdf.save()
            else:
                newpdf.codigo = ''
                newpdf.save()
            return redirect('mostrar_pdf')
        else:
            pdf_form = AddPdfForm(post_values, request.FILES)
            context = {'formulario': pdf_form}

            return render(request, 'pdf.html', context)


def extract_text(path):
    os.system("pdftotext -layout " + path + " extraccion.txt")
    #filename = re.sub('(p|P)(d|D)(f|F)', 'txt', path)
    file = open("extraccion.txt", "r")
    text = file.read()
    file.close()
    os.system("rm extraccion.txt")
    return text


def extract_text_from_image(path):
    tool = pyocr.get_available_tools()[0]
    lang = tool.get_available_languages()[2]

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


def crearCampo(request):
    campo = request.GET.get('campo', None)

    campos_actuales = CampoAdicional.objects.all()

    for c in campos_actuales:
        if campo.lower().replace(" ", "") == c.nombre.lower().replace(" ", ""):
            print("\n\n\n\n\n")
            print("Entro")
            print("\n\n\n\n\n")
            data = {
                'creado' : False
            }
            return JsonResponse(data)

    CampoAdicional.objects.create(nombre=campo)
    data = {
        'creado' : True,
        'nombre' : campo
    }

    return JsonResponse(data)


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



def siglas(request):
    codigo = request.GET.get('codigo', None)
    siglas = match_dpto(codigo)
    print(siglas)
    try:
        prefijo = Prefijo.objects.get(siglas=siglas)
        print(prefijo.asociacion)
        data = {
            'respuesta': prefijo.asociacion,
            'siglas' : siglas
        }
    except:
        data = {
            'respuesta': '',
            'siglas' : siglas
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
    expresion = '([A-Z][A-Z](-|\s|[^a-z|^A-Z|^0-9]|)[0-9][0-9][0-9][0-9])|([A-Z][A-Z][A-Z](-|\s|[^a-z|^A-Z|^0-9]|)[0-9][0-9][0-9])'
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
    return matcher.group(0)
    