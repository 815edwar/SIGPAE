#!/usr/bin/env python
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


# Vista de la pantalla home
#
# @date [31/01/2017]
#
# @author [PowerSoft]
#
class HomeView(TemplateView):
    template_name = 'home.html'


# Vista que muestra la lista de programas en SIGPAE
#
# @date [13/03/2017]
#
# @author [PowerSoft]
#
class ProgramaList(TemplateView):
    template_name = 'programas.html'

    #  Permite obtener el contexto necesario para renderizar la vista
    #
    #  @date [13/03/2017]
    #
    #  @author [PowerSoft]
    #
    #  @param [**kwargs] Diccionario con datos pasados en el template
    #
    #  @returns Diccionario con el conjunto de programas guardados en SIGPAE
    #
    def get_context_data(self, **kwargs):
        context = super(ProgramaList, self).get_context_data(**kwargs)
        programas = Solicitud.objects.all()
        context['programas'] = programas
        return context

class PasaList(TemplateView):
    template_name = 'pasa.html'

    #  Permite obtener el contexto necesario para renderizar la vista
    #
    #  @date [13/03/2017]
    #
    #  @author [PowerSoft]
    #
    #  @param [**kwargs] Diccionario con datos pasados en el template
    #
    #  @returns Diccionario con el conjunto de programas guardados en SIGPAE
    #
    def get_context_data(self, **kwargs):
        context = super(PasaList, self).get_context_data(**kwargs)
        programas = Transcripcion.objects.filter(propuesto=True)
        context['programas'] = programas
        return context
        


# Vista que muestra un programa de SIGPAE
#
# @date [13/03/2017]
#
# @author [PowerSoft]
#
class DisplayProgram(TemplateView):
    template_name = "display_program.html"

    #  Permite obtener el contexto necesario para renderizar la vista
    #
    #  @date [13/03/2017]
    #
    #  @author [PowerSoft]
    #
    #  @param [**kwargs] Diccionario con datos pasados en el template
    #
    #  @returns Diccionario con el programa de SIGPAE que se va a mostrar
    #           y los datos extra del programa que se mostraran en la vista.
    #
    def get_context_data(self, **kwargs):
        context = super(DisplayProgram, self).get_context_data(**kwargs)
        solicitud = Solicitud.objects.get(pk=int(kwargs['pk']))
        programa = solicitud.programa
        horas_semanales = programa.h_prac + programa.h_teoria + programa.h_lab
        context['programa'] = programa
        context['horas_semanales'] = horas_semanales
        context['solicitud'] = solicitud
        return context

class DisplayTranscripcion(TemplateView):
    template_name = "display_transcripcion.html"

    #  Permite obtener el contexto necesario para renderizar la vista
    #
    #  @date [13/03/2017]
    #
    #  @author [PowerSoft]
    #
    #  @param [**kwargs] Diccionario con datos pasados en el template
    #
    #  @returns Diccionario con el programa de SIGPAE que se va a mostrar
    #           y los datos extra del programa que se mostraran en la vista.
    #
    def get_context_data(self, **kwargs):
        context = super(DisplayTranscripcion, self).get_context_data(**kwargs)
        transcripcion = Transcripcion.objects.get(pk=int(kwargs['pk']))
        context['transcripcion'] = transcripcion
        return context


# Vista que muestra la lista de transcripciones en en SIGPAE historicos
#
# @date [31/01/2017]
#
# @author [PowerSoft]
#
class PDFList(TemplateView):
    template_name = 'transcripciones_en_proceso.html'

    #  Permite obtener el contexto necesario para renderizar la vista
    #
    #  @date [31/01/2017]
    #
    #  @author [PowerSoft]
    #
    #  @param [**kwargs] Diccionario con datos pasados en el template
    #
    #  @returns Diccionario con la lista de transcripciones guardadas en
    #           SIGPAE historicos y sus nombres.
    #
    def get_context_data(self, **kwargs):
        context = super(PDFList, self).get_context_data(**kwargs)

        programas = Transcripcion.objects.filter(propuesto=False)
        context['programas'] = programas
        pdf_names = []
        for programa in programas:
            nombre_pdf = programa.pdf.url.split('/')[-1]
            pdf_names.append(nombre_pdf)
        context['pdf_names'] = pdf_names
        context['tform'] = TranscriptorForm()
        return context


# Vista que muestra la lista de siglas propuestas como validas en SIGPAE historicos
#
# @date [13/03/2017]
#
# @author [PowerSoft]
#
class SiglasList(TemplateView):
    template_name = 'siglas_por_aprobar.html'

    #  Permite obtener el contexto necesario para renderizar la vista
    #
    #  @date [13/03/2017]
    #
    #  @author [PowerSoft]
    #
    #  @param [**kwargs] Diccionario con datos pasados en el template
    #
    #  @returns Diccionario con la lista de prefijos propuestos que aun
    #           no han sido aprobados.
    #
    def get_context_data(self, **kwargs):
        context = super(SiglasList, self).get_context_data(**kwargs)

        prefijos = Prefijo.objects.filter(aprobado=False)
        context['prefijos'] = prefijos

        return context


# Vista que muestra los detalles de una transcripcion en curso y permite editarlos
#
# @date [31/01/2017]
#
# @author [PowerSoft]
#
class ModifyPDF(TemplateView):
    template_name = 'display_pdf.html'

    #  Permite obtener el contexto necesario para renderizar la vista
    #
    #  @date [31/01/2017]
    #
    #  @author [PowerSoft]
    #
    #  @param [**kwargs] Diccionario con datos pasados en el template
    #
    #  @returns Diccionario con la transcripcion y todos los detalles
    #           asociados a la misma.
    #
    def get_context_data(self, **kwargs):
        context = super(ModifyPDF, self).get_context_data()
        pdf = Transcripcion.objects.get(pk=int(kwargs['pk']))
        otro_campo = ContenidoExtra.objects.filter(transcripcion=pdf.id)
        pdf_form = PdfForm(instance=pdf)
        context['formulario'] = pdf_form
        context['pdf'] = pdf
        context['encargado'] = pdf.encargado
        context['modifying'] = True
        context['nombres'] = CampoAdicional.objects.all()
        context['campos'] = otro_campo

        return context

    #  Permite procesar los datos que se envian a traves de la vista
    #
    #  @date [31/01/2017]
    #
    #  @author [PowerSoft]
    #
    #  @param [dict] request: Diccionario con los datos que envio el usuario.
    #  @param [dict] kwargs: Diccionario con datos pasados en el template
    #
    #  @returns Redireccionamiento a la pantalla home en caso de que los datos enviados
    #           se hayan procesado exitosamente.
    #           Redireccionamiento a la misma pantalla en caso de que haya un error en el
    #           procesamiento de los datos, con la especificacion de los datos erroneos.
    #
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
            for c in campo:
                if c.campo_adicional.nombre in post_values:
                    c.contenido = post_values[c.campo_adicional.nombre]
                    c.save()

            if 'campo_adicional' in post_values:
                campos_adicionales = post_values.pop('campo_adicional')
                contenido_campos = post_values.pop('contenido_campos')
                for i in range(len(campos_adicionales)):
                    if campos_adicionales[i] != "" and campos_adicionales[i] != "ninguna":
                        campo = CampoAdicional.objects.get(nombre=campos_adicionales[i])
                        ContenidoExtra.objects.create(transcripcion=pdf, campo_adicional=campo,
                                                      contenido=contenido_campos[i])

            if (pdf.codigo != "" and pdf.encargado!="" and pdf.denominacion!="" and pdf.periodo!=""
                and pdf.año!= "" and pdf.horas_practica!="" and pdf.horas_teoria!=" "
                and pdf.horas_laboratorio!= "" and pdf.sinopticos!= "" and pdf.ftes_info_recomendadas!= "" and
                pdf.codigo != None and pdf.encargado!=None and pdf.denominacion!=None and pdf.periodo!=None
                and pdf.año!= None and pdf.horas_practica!=None and pdf.horas_teoria!=" "
                and pdf.horas_laboratorio!= None and pdf.sinopticos!= None and pdf.ftes_info_recomendadas!= None):
                pdf.pasa = True
                pdf.save()
            else :
                pdf.pasa = False
                pdf.save()
            return redirect('home')


        else:
            context = {'formulario': pdf_form, 'pdf': pdf}
            return render(request, 'display_pdf.html', context)


# Vista que muestra los detalles de una transcripcion y permite editarlos
#
# @date [31/01/2017]
#
# @author [PowerSoft]
#
class DisplayPDF(TemplateView):
    template_name = 'display_pdf.html'

    #  Permite obtener el contexto necesario para renderizar la vista
    #
    #  @date [31/01/2017]
    #
    #  @author [PowerSoft]
    #
    #  @returns Diccionario con la transcripcion y todos los detalles
    #           asociados a la misma.
    #
    def get_context_data(self):
        context = super(DisplayPDF, self).get_context_data()
        msgs = get_messages(self.request)
        pdf_id = -1
        for message in msgs:
            pdf_id = int(str(message))
        msgs.used = True
        pdf = Transcripcion.objects.get(id=pdf_id)
        pdf_form = PdfForm(instance=pdf)
        if pdf.codigo is not None and pdf.codigo != '':
            expresion = '[A-Z][A-Z][A-Z]|[A-Z][A-Z]'
            patron = re.compile(expresion)
            matcher = patron.search(pdf.codigo)
            prefijo = Prefijo.objects.filter(siglas=matcher.group(0))
            if prefijo.exists():
                prefijo = Prefijo.objects.filter(siglas=matcher.group(0))[0]
                departamento = Departamento.objects.filter(nombre=prefijo.asociacion)
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
        context['nombres'] = CampoAdicional.objects.all()

        return context

    #  Permite procesar los datos que se envian a traves de la vista
    #
    #  @date [31/01/2017]
    #
    #  @author [PowerSoft]
    #
    #  @param [dict] request: Diccionario con los datos que envio el usuario.
    #
    #  @returns Redireccionamiento a la pantalla home en caso de que los datos enviados
    #           se hayan procesado exitosamente.
    #           Redireccionamiento a la misma pantalla en caso de que haya un error en el
    #           procesamiento de los datos, con la especificacion de los datos erroneos.
    #
    @staticmethod
    def post(request):
        post_values = request.POST.copy()
        if 'siglas' in post_values:
            if post_values['siglas'] != '':
                prefijo_nuevo = Prefijo.objects.create(siglas=post_values['siglas'],
                                                       asociacion=post_values['asociacion'],
                                                       aprobado=False)
                prefijo_nuevo.save()
        elif 'siglas2' in post_values:
            if post_values['siglas2'] != '':
                prefijo_nuevo = Prefijo.objects.create(siglas=post_values['siglas2'],
                                                       asociacion="", aprobado=False)
                prefijo_nuevo.save()

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
                pdf.encargado = post_values['encargado1']
                pdf_form.save()

            if 'campo_adicional' in post_values:
                campos_adicionales = post_values.pop('campo_adicional')
                contenido_campos = post_values.pop('contenido_campos')
                for i in range(len(campos_adicionales)):
                    if campos_adicionales[i] != "" and campos_adicionales[i] != "ninguna":
                        campo = CampoAdicional.objects.get(nombre=campos_adicionales[i])
                        ContenidoExtra.objects.create(transcripcion=pdf, campo_adicional=campo,
                                                      contenido=contenido_campos[i])

            return redirect('home')

        else:
            context = {'formulario': pdf_form, 'pdf': pdf}
            return render(request, 'display_pdf.html', context)


# Vista que permite agregar una nueva transcripcion a partir de un nuevo PDF
# que se sube en el sistema.
#
# @date [31/01/2017]
#
# @author [PowerSoft]
#
class NewPdf(TemplateView):
    template_name = 'pdf.html'

    #  Permite obtener el contexto necesario para renderizar la vista
    #
    #  @date [31/01/2017]
    #
    #  @author [PowerSoft]
    #
    #  @returns Diccionario con el formulario que permite subir el PDF nuevo al
    #           sistema.
    #
    def get_context_data(self, **kwargs):
        context = super(NewPdf, self).get_context_data(**kwargs)
        context['formulario'] = AddPdfForm()

        return context

    #  Permite procesar los datos que se envian a traves de la vista
    #
    #  @date [31/01/2017]
    #
    #  @author [PowerSoft]
    #
    #  @param [dict] request: Diccionario con los datos que envio el usuario.
    #
    #  @returns Redireccionamiento a la pantalla DisplayPDF en caso de que los datos enviados
    #           se hayan procesado exitosamente.
    #           Redireccionamiento a la misma pantalla en caso de que haya un error en el
    #           procesamiento de los datos, con la especificacion de los datos erroneos.
    #
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


#  Función que permite extraer texto de un PDF sin imagen.
#
#  @date [31/01/2017]
#
#  @author [PowerSoft]
#
#  @param [String] path: El path donde se encuentra el pdf del que se quiere extraer texto
#
#  @returns El texto plano extraido del pdf.
#
def extract_text(path):
    os.system("pdftotext -layout " + path + " extraccion.txt")
    # filename = re.sub('(p|P)(d|D)(f|F)', 'txt', path)
    file = open("extraccion.txt", "r")
    text = file.read()
    file.close()
    os.system("rm extraccion.txt")
    return text


#  Función que permite extraer texto de un PDF de imagen.
#
#  @date [31/01/2017]
#
#  @author [PowerSoft]
#
#  @param [String] path: El path donde se encuentra el pdf del que se quiere extraer texto
#
#  @returns El texto plano extraido del pdf.
#
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


#  Función que dada una peticion de creacion de un nuevo campo, verifica si el campo ya existe
#  en la base. Si no existe, entonces crea el nuevo campo opcional, en caso contrario no lo crea.
#
#  @date [13/03/2017]
#
#  @author [PowerSoft]
#
#  @param [dict] request: La informacion de la peticion del usuario
#
#  @returns Diccionario con booleano para informar si el campo fue creado o no y la denominacion
#           del nuevo campo en caso de que se haya creado.
#
def crear_campo(request):
    campo = request.GET.get('campo', None)

    campos_actuales = CampoAdicional.objects.all()

    for c in campos_actuales:
        if campo.lower().replace(" ", "") == c.nombre.lower().replace(" ", ""):
            data = {
                'creado': False
            }
            return JsonResponse(data)

    CampoAdicional.objects.create(nombre=campo)
    data = {
        'creado': True,
        'nombre': campo
    }

    return JsonResponse(data)


#  Función que dada una peticion para definir un encargado, filtra los posibles responsables
#  en base a dicha peticion. Puede ser a partir de una coordinacion o un departamento. Ademas
#  si se quiere escoger una coordinacion como responsable, se filtra por decanato.
#
#  @date [13/03/2017]
#
#  @author [PowerSoft]
#
#  @param [dict] request: La informacion de la peticion del usuario
#
#  @returns Diccionario con la lista de departamentos si la peticion de filtro es por departamento.
#           Diccionario con la lista de decanatos si la peticion de filtro es por coordinacion.
#           Diccionario con la lista de coordinaciones en caso de se haya definido el decanato por el
#           cual se quiere filtrar a las coordinaciones.
#
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


#  Función que dada una propuesta de codigo de materia, verifica si el prefijo de dicho codigo esta
#  registrado en el sistema como un codigo valido.
#
#  @date [13/03/2017]
#
#  @author [PowerSoft]
#
#  @param [dict] request: La informacion de la peticion del usuario
#
#  @returns Diccionario con booleano para informar si el campo fue creado o no y la denominacion
#           del nuevo campo en caso de que se haya creado.
#
def siglas(request):
    codigo = request.GET.get('codigo', None)
    sigla = match_dpto(codigo)
    try:
        prefijo = Prefijo.objects.get(siglas=sigla)
        data = {
            'respuesta': prefijo.asociacion,
            'siglas': sigla
        }
    except:
        data = {
            'respuesta': '',
            'siglas': sigla
        }

    return JsonResponse(data)


#  Función que permite extraer codigo html de un pdf
#
#  @date [31/01/2017]
#
#  @author [PowerSoft]
#
#  @param [String] path: La informacion de la peticion del usuario
#
#  @returns Diccionario con booleano para informar si el campo fue creado o no y la denominacion
#           del nuevo campo en caso de que se haya creado.
#
def extract_html(path):
    os.system("pdftohtml -s -c " + path)
    output = re.sub('.(p|P)(d|D)(f|F)', '-html.html', path)
    file = open(output, "r")
    text = file.read()
    file.close()
    os.system("rm " + output + ' *.png')
    return text


#  Función que dado un string, verifica si hay un substring con formato valido para un posible
#  codigo de asignatura en dicho string.
#
#  @date [13/03/2017]
#
#  @author [PowerSoft]
#
#  @param [String] text: String al que se le hara la verificacion
#
#  @returns El substring que cumple con el formato de un codigo de asignatura en caso de encontrarlo.
#           None en caso contrario
#
def match_codigo_asig(text):
    expresion = '([A-Z][A-Z](-|\s|[^a-z|^A-Z|^0-9]|)[0-9][0-9][0-9][0-9])'\
                '|([A-Z][A-Z][A-Z](-|\s|[^a-z|^A-Z|^0-9]|)[0-9][0-9][0-9])'
    patron = re.compile(expresion)
    matcher = patron.search(text)
    if matcher is not None:
        return matcher.group(0)
    else:
        return None


#  Función que dado un string con un formato de codigo de asignatura, extrae el prefijo de dicho
#  codigo.
#
#  @date [13/03/2017]
#
#  @author [PowerSoft]
#
#  @param [String] codigo: El codigo del cual se extraera su prefijo
#
#  @returns Substring del codigo con su prefijo.
#
def match_dpto(codigo):
    expresion = '[A-Z][A-Z][A-Z]|[A-Z][A-Z]'
    patron = re.compile(expresion)
    matcher = patron.search(codigo)
    return matcher.group(0)

#  Función que dado unos datos de transcriptor los introduce a la base y 
#  propone la transcripcion para sigpae
#  @date [29/03/2017]
#
#  @author [PowerSoft]
#
#  @param [String] request: La informacion de la peticion del usuario
#
#  @returns Diccionario con booleano para informar si el transcriptor fue creado o no 

def ProponerTranscripcion(request):

    nombre = request.GET.get('nombre', None)
    apellido = request.GET.get('apellido', None)
    correo = request.GET.get('correo', None)
    tlf = request.GET.get('tlf', None)
    transcripcion = request.GET.get('programa',None)

    if (nombre!="" and apellido!="" and correo!="" and tlf!=''):
        if (re.match('[^@]+@[^@]+\.[^@]+',correo) and re.match('[0-9]{11}',tlf)):
            completo = True
        else:   
            completo = False
    else:   
        completo = False

    programa = Transcripcion.objects.get(id=transcripcion)

    busqueda = propuestos.objects.filter(programa__denominacion=programa.denominacion,programa__periodo=programa.periodo,programa__año=programa.año)
    if busqueda.exists(): 
        data = {
        'creado': False,
        'completo': completo
        }
    else:
        if completo:

            transcriptor = Transcriptor.objects.create()
            transcriptor.nombre = nombre
            transcriptor.apellido = apellido 
            transcriptor.correo = correo
            transcriptor.telefono = tlf
            programa.propuesto = True
            transcriptor.save()
            programa.save()
            propuesto = propuestos.objects.create(transcriptor=transcriptor,programa=programa)
            propuesto.save()
            data = {
                'creado': True,
                'completo': completo
            }
        else:
            data = {
                'creado': False,
                'completo': completo
            }


    

    return JsonResponse(data)