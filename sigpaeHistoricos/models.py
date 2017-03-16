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

class Prefijo(models.Model):
    siglas = models.CharField('Prefijo',max_length=3)
    asociacion = models.CharField('Asociación', null=True, max_length=100)
    aprobado = models.BooleanField(default=True)

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


class Transcripcion(models.Model):
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

    denominacion = models.CharField('Denominación', max_length=100, null=True)

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

    codigo = models.CharField('Código', max_length=50, null=True)

    denominacion = models.CharField('Denominación', max_length=100, null=True)

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

    objetivos_generales = models.TextField('Objetivos Generales', null=True)
    objetivos_especificos = models.TextField('Objetivos Específicos', null=True)

    sinopticos = models.TextField('Contenidos Sinópticos', null=True)

    estrategias_metodologicas = models.TextField('Estrategias Metodológicas', null=True)

    estrategias_evaluacion = models.TextField('Estrategias de Evaluación', null=True)

    ftes_info_recomendadas = models.TextField('Fuentes de Información Recomendadas', null=True)

    encargado = models.CharField('Encargado', max_length=100, null=True)

    def __str__(self):
        return self.denominacion    