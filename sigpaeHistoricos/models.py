# -*- coding: utf-8 -*-
from django.db import models
from django.core.exceptions import ValidationError
from datetime import date
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

# Validador para el formato pdf de los archivos a subir.
def valid_extension(value):
    if not (value.name.endswith('.pdf') or value.name.endswith('.PDF') or value.name.endswith('.Pdf')
            or value.name.endswith('.PDf') or value.name.endswith('.pdF') or value.name.endswith('.PdF')
            or value.name.endswith('.pDF') or value.name.endswith('.pDf')):
        raise ValidationError("Sólo se permiten archivos en formato PDF.")


class Departamento(models.Model):
    nombre = models.CharField('Nombre', max_length=100, null=True)

    def __str__(self):
        return self.nombre


class Decanato(models.Model):
    nombre = models.CharField('Nombre', max_length=100, null=True)

    def __str__(self):
        return self.nombre


class Coordinacion(models.Model):
    decanato = models.ForeignKey(Decanato, verbose_name='Decanato', null=True)
    nombre = models.CharField('Nombre', max_length=100, null=True)

    def __str__(self):
        return self.nombre


class Pdfs(models.Model):
    SEP_DIC = 'sep-dic'
    ENE_MAR = 'ene-mar'
    ABR_JUL = 'abr-jul'
    VERANO = 'intensivo'

    PERIODOS = (
        (SEP_DIC, SEP_DIC),
        (ENE_MAR, ENE_MAR),
        (ABR_JUL, ABR_JUL),
        (VERANO, VERANO),
    )

    años = []
    for i in range(1969, date.today().year + 1):
        años.append((i, str(i)))

    AÑOS = tuple(años)

    # Salva los PDF en /media/uploads/
    pdf = models.FileField(
        upload_to='uploads/',
        validators=[valid_extension],
    )


    # Almacena el string generado por la transformación del PDF
    texto = models.TextField('Texto', null=True)
    
    codigo = models.CharField('Código', max_length=50, null=True)

    denominacion = models.CharField('Denominación', max_length=100,null= True)


    periodo = models.CharField(
        'Período',
        max_length=9,
        null=True,
        choices=PERIODOS,
    )

    año = models.PositiveIntegerField('Año', choices=AÑOS, null=True)

    horas_practica = models.PositiveIntegerField('Horas de práctica', null=True, default=0)

    horas_teoria = models.PositiveIntegerField('Horas de teoría', null=True, default=0)

    horas_laboratorio = models.PositiveIntegerField('Horas de laboratorio', null=True, default=0)

    creditos = models.PositiveIntegerField('Créditos', null=True, validators=[MinValueValidator(0),
                                                                              MaxValueValidator(16)])

    requisitos = models.TextField('Requisitos', null=True)

    objetivos = models.TextField('Objetivos', null=True)

    sinopticos = models.TextField('Contenidos Sinópticos', null=True)

    estrategias_metodologicas = models.TextField('Estrategias Metodológicas', null=True)

    estrategias_evaluacion = models.TextField('Estrategias de Evaluación', null=True)

    ftes_info_recomendadas = models.TextField('Fuentes de Información Recomendadas', null=True)

    observaciones = models.TextField('Observaciones', null=True)

    encargado = models.CharField('Encargado', max_length=100, null=True)

    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)



class Programa(models.Model):
    SEP_DIC = 'sep-dic'
    ENE_MAR = 'ene-mar'
    ABR_JUL = 'abr-jul'
    VERANO = 'intensivo'

    PERIODOS = (
        (SEP_DIC, SEP_DIC),
        (ENE_MAR, ENE_MAR),
        (ABR_JUL, ABR_JUL),
        (VERANO, VERANO),
    )

    años = []
    for i in range(1969, date.today().year + 1):
        años.append((i, str(i)))

    AÑOS = tuple(años)


    periodo = models.CharField(
        'Período',
        max_length=9,
        null=True,
        choices=PERIODOS,
    )

    año = models.PositiveIntegerField('Año', choices=AÑOS, null=True)

    horas_practica = models.PositiveIntegerField('Horas de práctica', null=True, default=0)

    horas_teoria = models.PositiveIntegerField('Horas de teoría', null=True, default=0)

    horas_laboratorio = models.PositiveIntegerField('Horas de laboratorio', null=True, default=0)


    objetivos_generales = models.TextField('Objetivos Generales', null=True)
    objetivos_especificos = models.TextField('Objetivos Específicos', null=True)

    sinopticos = models.TextField('Contenidos Sinópticos', null=True)

    estrategias_metodologicas = models.TextField('Estrategias Metodológicas', null=True)

    estrategias_evaluacion = models.TextField('Estrategias de Evaluación', null=True)

    ftes_info_recomendadas = models.TextField('Fuentes de Información Recomendadas', null=True)

    contenidos = models.TextField('Encargado', max_length=100, null=True)

    cronograma = models.TextField('Encargado', max_length=100, null=True)

    def __str__(self):
        return self.denominacion    



class Solicitud (models.Model):
    coordinacion = models.CharField('Coordinación', max_length=100)
    fecha_elaboracion = models.DateTimeField(auto_now=True, null=True)
    codigo = models.CharField('Código',max_length=7)
    codigo_anterior = models.CharField('Código anterior',max_length=7,null=True)
    denominacion = models.CharField(max_length=70)
    creditos = models.PositiveIntegerField()
    tipo_aula = models.CharField(max_length=20)
    horas_teoria = models.BooleanField()
    horas_practica = models.BooleanField()
    horas_laboratorio = models.BooleanField()
    trim = models.CharField(max_length=9)
    año = models.CharField(max_length = 4)
    carrera = models.CharField(max_length=35)
    trim_pensum = models.BooleanField()
    requisitos_cred =  models.BooleanField()
    permiso_coord = models.BooleanField()
    tipo_materia = models.CharField(max_length=20)
    clase_materia = models.CharField(max_length=25)
    observaciones = models.TextField(null=True)
    vigente = models.BooleanField()
    imparticion = models.CharField(max_length=15)
    decanato = models.CharField(max_length = 50,null=True)
    obsanul = models.TextField(null=True)
    programa = models.ForeignKey(Programa)
