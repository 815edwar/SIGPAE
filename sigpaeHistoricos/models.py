#!/usr/bin/env python# -*- coding: utf-8 -*-from django.db import modelsfrom django.core.exceptions import ValidationErrorfrom datetime import datefrom django.core.validators import RegexValidator# Validadores # Validator for phonesPHONE_VALIDATOR = RegexValidator(    regex=r'^(0414|0412|0424|0416|0426)\d{7}$',    message="Teléfono inválido.",)CODIGO_VALIDATOR =RegexValidator(    regex = r'([A-Z][A-Z](-|\s|[^a-z|^A-Z|^0-9]|)[0-9][0-9][0-9][0-9])'\                '|([A-Z][A-Z][A-Z](-|\s|[^a-z|^A-Z|^0-9]|)[0-9][0-9][0-9])',        message = "Código inválido")EMAIL_VALIDATOR = RegexValidator(    regex=r'^[^@]+@[^@]+\.[^@]+',    message="Correo inválido.",)#  Función que permite verificar que la extensión de un archivo es PDF##  @date [31/01/2017]##  @author [PowerSoft]##  @param [URL] value: El URL del archivo a verificar##  @throws ValidationError: Si el archivo no tiene la extension pdf requerida.#def valid_extension(value):    if not (value.name.endswith('.pdf') or value.name.endswith('.PDF') or value.name.endswith('.Pdf')       or value.name.endswith('.PDf') or value.name.endswith('.pdF') or value.name.endswith('.PdF')       or value.name.endswith('.pDF') or value.name.endswith('.pDf')):            raise ValidationError("Sólo se permiten archivos con extensión PDF.")#  Representa los prefijos de códigos de materias registrados en la base del sistema.#  Incluye los prefijos propuestos por los transcriptores como prefijos válidos#  y también los que ya están verificados.##  @date [10/03/2017]##  @author [PowerSoft]##  @field [models.CharField] siglas: El prefijo correspondiente.#  @field [models.CharField] asociación: La dependencia con la que se relaciona.#                            Puede ser un departamento o un tipo de trabajo.#  @field [models.BooleanField] aprobado: Indica si el prefijo ya está verificado.#class Prefijo(models.Model):    siglas = models.CharField('Prefijo', max_length=3)    asociacion = models.CharField('Asociación', null=True, max_length=100)    aprobado = models.BooleanField(default=True)#  Representa los departamentos registrados en la USB##  @date [13/02/2017]##  @author [PowerSoft]##  @field [models.CharField] nombre: El nombre del departamento.#class Departamento(models.Model):    nombre = models.CharField('Nombre', max_length=100, null=True)    # Sobrescribe la transformación a string por defecto de una instancia    # de este modelo    #    # @date [13/02/17]    #    # @author [PowerSoft]    #    # @returns [String] La transformación a string del objeto.    #    def __str__(self):        return self.nombre#  Representa los decanatos registrados en la USB##  @date [13/02/2017]##  @author [PowerSoft]##  @field [models.CharField] nombre: El nombre del decanato.#class Decanato(models.Model):    nombre = models.CharField('Nombre', max_length=100, null=True)    # Sobrescribe la transformación a string por defecto de una instancia    # de este modelo    #    # @date [13/02/17]    #    # @author [PowerSoft]    #    # @returns [String] La transformación a string del objeto.    #    def __str__(self):        return self.nombre#  Representa las coordinaciones registradas en la USB##  @date [13/02/2017]##  @author [PowerSoft]##  @field [models.CharField] nombre: El nombre de la coordinación.#  @field [models.ForeignKey] decanato: Referencia al decanato del cual depende#                             la coordinación.#class Coordinacion(models.Model):    decanato = models.ForeignKey(Decanato, verbose_name='Decanato', null=True)    nombre = models.CharField('Nombre', max_length=100, null=True)    # Sobrescribe la transformación a string por defecto de una instancia    # de este modelo    #    # @date [13/02/17]    #    # @author [PowerSoft]    #    # @returns [String] La transformación a string del objeto.    #    def __str__(self):        return self.nombre#  Representa las transcripciones en curso de algun programa de la USB##  @date [31/01/2017]##  @author [PowerSoft]##  @field [models.FileField] pdf: Archivo pdf con el contenido del programa.#  @field [models.TextField] texto: Texto plano extraído del pdf.#  @field [models.CharField] codigo: Código de la materia describida por el programa.#  @field [models.CharField] denominacion: Título del programa.#  @field [models.CharField] periodo: Periodo donde entro en vigencia el programa.#  @field [models.PositiveIntegerField] año: Año donde entro en vigencia el programa.#  @field [models.PositiveIntegerField] horas_teoria: Horas de teoria dedicadas a la materia#                                       describida por el programa.#  @field [models.PositiveIntegerField] horas_practica: Horas de practica dedicadas a la ma-#                                       teria describida por el programa.#  @field [models.PositiveIntegerField] horas_laboratorio: Horas de laboratorio dedicadas a#                                       la materia describida por el programa.#  @field [models.PositiveIntegerField] creditos: Creditos de la materia que describe el programa.#  @field [models.TextField] sinopticos: Contenidos sinopticos de la materia que describe el programa.#  @field [models.TextField] ftes_info_recomendadas: Fuentes de informacion sobre la materia recomendadas#  @field [models.TextField] observaciones: Observaciones sobre la materia.#  @field [models.CharField] encargado: Instancia responsable del programa#  @field [models.DatetimeField] fecha_modificacion: Ultima fecha de modificacion del programa#  @field [models.BooleanField] pasa: si puede ser propuesto o no para sigpae#  @field [models.BooleanField] propuesto: si ha sido propuesto para programa#class Transcripcion(models.Model):    # Definición del dominio del periodo de vigencia del programa que se transcribe    SEP_DIC = 'sep-dic'    ENE_MAR = 'ene-mar'    ABR_JUL = 'abr-jul'    VERANO = 'intensivo'    PERIODOS = (        (SEP_DIC, SEP_DIC),        (ENE_MAR, ENE_MAR),        (ABR_JUL, ABR_JUL),        (VERANO, VERANO),    )    # Definición del dominio de las horas de dedicación al curso del programa    horas = []    for i in range(0, 41):        horas.append((i, str(i)))    HORAS = tuple(horas)    # Definición del dominio de los creditos de un programa    creditos = []    for i in range(0, 17):        creditos.append((i, str(i)))    CREDITOS = tuple(creditos)    pdf = models.FileField(upload_to='uploads/', validators=[valid_extension])    texto = models.TextField('Texto', null=True)    codigo = models.CharField('Código', max_length=50, null=True, validators=[CODIGO_VALIDATOR])    denominacion = models.CharField('Denominación', max_length=100, null=True)    fecha_elaboracion = models.CharField('Fecha de elaboración',max_length=30, null=True)    periodo = models.CharField('Período', max_length=9, null=True, choices=PERIODOS)    año = models.PositiveIntegerField('Año', null=True)    horas_teoria = models.PositiveIntegerField('Horas de teoría', null=True, choices=HORAS)    horas_practica = models.PositiveIntegerField('Horas de práctica', null=True, choices=HORAS)    horas_laboratorio = models.PositiveIntegerField('Horas de laboratorio', null=True, choices=HORAS)    creditos = models.PositiveIntegerField('Créditos', null=True, choices=CREDITOS)    sinopticos = models.TextField('Contenidos Sinópticos', null=True)    ftes_info_recomendadas = models.TextField('Fuentes de Información Recomendadas', null=True)    requisitos = models.TextField('Requisitos', null=True)    estrategias_met = models.TextField('Estrategias Metodológicas', null=True)    estrategias_eval = models.TextField('Estrategias de Evaluación', null=True)    justificacion = models.TextField('Justificación', null=True)    observaciones = models.TextField('Observaciones', null=True)    objetivos_generales = models.TextField('Objetivos', null=True)    objetivos_especificos = models.TextField('Objetivos Especificos', null=True)    encargado = models.CharField('Encargado', max_length=100, null=True)    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)    pasa = models.BooleanField(default= False)    propuesto = models.BooleanField(default= False)#  Representa los programas aprobados de la USB##  @date [10/03/2017]##  @author [PowerSoft]##  @field [models.PositiveIntegerField] h_teoria: Horas de teoria dedicadas a la materia#                                       describida por el programa.#  @field [models.PositiveIntegerField] h_prac: Horas de practica dedicadas a la materia#                                       describida por el programa.#  @field [models.PositiveIntegerField] h_lab: Horas de laboratorio dedicadas a la materia#                                       describida por el programa.#  @field [models.CharField] fecha_vigTrim: Periodo donde entro en vigencia el programa.#  @field [models.PositiveIntegerField] fecha_vigAno: Año donde entro en vigencia el programa.#  @field [models.TextField] obj_g: Objetivos generales de la materia.#  @field [models.TextField] obj_e: Objetivos especificos de la materia.#  @field [models.TextField] contenidos: Contenidos de la materia.#  @field [models.TextField] estrategias: Estrategias implementadas para dictar la materia.#  @field [models.TextField] estrat_eval: Estrategias para evaluar la materia.#  @field [models.TextField] fuentes: Fuentes de informacion de la materia.#  @field [models.TextField] cronograma: Cronograma de la materia.#  @field [models.TextField] sinoptico: Contenidos sinopticos de la materia# class Programa(models.Model):    # Definición del dominio del periodo de vigencia del programa que se transcribe    SEP_DIC = 'sep-dic'    ENE_MAR = 'ene-mar'    ABR_JUL = 'abr-jul'    VERANO = 'intensivo'    PERIODOS = (        (SEP_DIC, SEP_DIC),        (ENE_MAR, ENE_MAR),        (ABR_JUL, ABR_JUL),        (VERANO, VERANO),    )    # Definición del dominio de año de vigencia del programa que se transcribe    años = []    for i in range(1969, date.today().year + 1):        años.append((i, str(i)))    AÑOS = tuple(años)    h_teoria = models.PositiveIntegerField('Horas de teoría', null=True, default=0)    h_prac = models.PositiveIntegerField('Horas de práctica', null=True, default=0)    h_lab = models.PositiveIntegerField('Horas de laboratorio', null=True, default=0)    fecha_vigTrim = models.CharField('Período', max_length=9, null=True, choices=PERIODOS)    fecha_vigAno = models.PositiveIntegerField('Año', choices=AÑOS, null=True)    obj_g = models.TextField('Objetivos Generales', null=True)    obj_e = models.TextField('Objetivos Específicos', null=True)    contenidos = models.TextField('Encargado', max_length=100, null=True)    estrategias = models.TextField('Estrategias Metodológicas', null=True)    estrat_eval = models.TextField('Estrategias de Evaluación', null=True)    fuentes = models.TextField('Fuentes de Información Recomendadas', null=True)    cronograma = models.TextField('Encargado', max_length=100, null=True)    sinoptico = models.TextField('Contenidos Sinópticos', null=True)    # Sobrescribe la transformación a string por defecto de una instancia    # de este modelo    #    # @date [10/03/17]    #    # @author [PowerSoft]    #    # @returns [String] La transformación a string del objeto.    #    def __str__(self):        return self.contenidos#  Campos adicionales posibles para una transcripcion del programa##  @date [10/03/2017]##  @author [PowerSoft]##  @field [models.CharField] nombre: Nombre del campo adicional.#class CampoAdicional(models.Model):    nombre = models.CharField('Nombre', max_length=100)    # Sobrescribe la transformación a string por defecto de una instancia    # de este modelo    #    # @date [10/03/17]    #    # @author [PowerSoft]    #    # @returns [String] La transformación a string del objeto.    #    def __str__(self):        return self.nombre#  Contenido extra a los obligatorios y normados que puede tener un programa##  @date [10/03/2017]##  @author [PowerSoft]##  @field [models.ForeignKey] transcripcion: Referencia a la transcripcion a la que#                             pertenece el contenido extra.#  @field [models.ForeignKey] campo_adicional: Referencia al campo adicional que con-#                             tiene el programa.#  @field [models.TextField] contenido: Cuerpo del campo adicional del programa.#class ContenidoExtra(models.Model):    transcripcion = models.ForeignKey(Transcripcion, verbose_name='Transcripcion')    campo_adicional = models.ForeignKey(CampoAdicional)    contenido = models.TextField('Contenido')#  Solicitudes enviadas a SIGPAE para que se verifique una transcripcion y se apruebe#  como un programa valido##  @date [10/03/2017]##  @author [PowerSoft]#class Solicitud(models.Model):    coordinacion = models.CharField('Coordinación', max_length=100)    porasignar = models.BooleanField()    porrevisarD = models.BooleanField()    porrevisarP = models.BooleanField()    rechazadoC = models.BooleanField()    validadoC = models.BooleanField()    enviadoD = models.BooleanField()    devueltoD = models.BooleanField()    fecha_elaboracion = models.DateTimeField(auto_now=True, null=True)    tipo_solicitud = models.CharField(max_length=20)    subtipo_solicitud = models.CharField(max_length=30)    nivel = models.CharField(max_length=20)    codigo = models.CharField('Código', max_length=7)    codigo_anterior = models.CharField('Código anterior', max_length=7, null=True)    denominacion = models.CharField(max_length=70)    creditos = models.PositiveIntegerField()    tipo_aula = models.CharField(max_length=20)    horas_teoria = models.BooleanField()    horas_practica = models.BooleanField()    horas_laboratorio = models.BooleanField()    trim = models.CharField(max_length=9)    año = models.CharField(max_length=4)    accion = models.CharField(max_length=20)    carrera = models.CharField(max_length=35)    trim_pensum = models.BooleanField()    requisitos_cred = models.BooleanField()    permiso_coord = models.BooleanField()    tipo_materia = models.CharField(max_length=20)    clase_materia = models.CharField(max_length=25)    observaciones = models.TextField(null=True)    vigente = models.BooleanField()    validadodace = models.BooleanField()    especial = models.BooleanField()    imparticion = models.CharField(max_length=15)    decanato = models.CharField(max_length=50, null=True)    obsanul = models.TextField(null=True)    programa = models.ForeignKey(Programa)# Transcriptor encargado de la edición de los campos de una transcripción en proces##  @date [20/03/2017]##  @author [PowerSoft]##  @field [models.Charfield] nombre indica el nombre del transcriptor#  @field [models.Charfield] apellido indica el apellido del transcriptor#  @field [models.Charfield] correo indica el correo electronico del transcriptor#  @field [models.Charfield] telefono numero telefonico de contacto del transcriptorclass Transcriptor(models.Model):    nombre = models.CharField('Nombres',max_length = 100)    apellido = models.CharField('Apellidos',max_length = 200)    correo = models.CharField('Correo',max_length = 100, validators = [EMAIL_VALIDATOR])    telefono = models.CharField('Telefono',max_length = 100, validators = [PHONE_VALIDATOR])    def __str__(self):        return self.nombre #  Relacion entre un transcriptor y un programa analitico sujeto a aprobacion#  @date [20/03/2017]##  @author [PowerSoft]# #  @field [models.ForeignKey] transciptor hace referencia al encargado de la transcripcion#  @field [models.ForeignKey] transcipcion hace referencia a la transcripcion por aprobarclass propuestos(models.Model):    transcriptor = models.ForeignKey(Transcriptor)    programa = models.ForeignKey(Transcripcion)