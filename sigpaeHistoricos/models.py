# -*- coding: utf-8 -*-
from django.db import models
from django.core.exceptions import ValidationError
from datetime import date


# Create your models here.

# Validador para el formato pdf de los archivos a subir.
def valid_extension(value):
    if not (value.name.endswith('.pdf') or value.name.endswith('.PDF') or value.name.endswith('.Pdf')
     		or value.name.endswith('.PDf') or value.name.endswith('.pdF') or value.name.endswith('.PdF') 
     		or value.name.endswith('.pDF') or value.name.endswith('.pDf')):
        raise ValidationError("Sólo se permiten archivos en formato PDF.")


class Pdfs(models.Model):
    SEP_DIC = 'sep-dic'
    ENE_MAR = 'ene-mar'
    ABR_JUL = 'abr-jul'
    VERANO = 'intensivo'

    PERIODOS = (
        (SEP_DIC, 'Septiembre-Diciembre'),
        (ENE_MAR, 'Enero-Marzo'),
        (ABR_JUL, 'Abril-Julio'),
        (VERANO, 'Intensivo'),
    )

    CIENCIA_MATERIALES = 'DCM'
    CIENCIAS_TIERRA = 'DCT'
    COMPUTACION_TI = 'DCTI'
    COMPUTO_CIENTIFICO = 'DCCE'
    CONVERSION_TRANSPORTE = 'DCTE'
    ELECTRONICA_CIRCUITOS = 'DEC'
    FISICA = 'DF'
    MATEMATICAS = 'DMPA'
    MECANICA = 'DM'
    PROCESOS_SISTEMAS = 'DPS'
    QUIMICA = 'DQ'
    TERMO_FENOMENOS = 'DTFT'

    DEPARTAMENTOS = (
        (CIENCIA_MATERIALES, 'Departamento de Ciencia de los Materiales'),
        (CIENCIAS_TIERRA, 'Departamento de Ciencias de la Tierra'),
        (COMPUTACION_TI, 'Departamento de Computación y Tecnología de Información'),
        (COMPUTO_CIENTIFICO, 'Departamento de Cómputo Científico y Estadística'),
        (CONVERSION_TRANSPORTE, 'Departamento de Conversión y Transporte de Energía'),
        (ELECTRONICA_CIRCUITOS, 'Departamento de Electrónica y Circuitos'),
        (FISICA, 'Departamento de Física'),
        (MATEMATICAS, 'Departamento de Matemáticas Puras y Aplicadas'),
        (MECANICA, 'Departamento de Mecánica'),
        (PROCESOS_SISTEMAS, 'Departamento de Procesos y Sistemas'),
        (QUIMICA, 'Departamento de Química'),
        (TERMO_FENOMENOS, 'Departamento de Termodinámica y Fenómenos de Transferencia'),
    )

    anyos = []
    for i in range(1969, date.today().year + 1):
        anyos.append((i, str(i)))

    ANYOS = tuple(anyos)

    # Salva los PDF en /media/uploads/año/mes/día
    pdf = models.FileField(
        upload_to='uploads/',
        validators=[valid_extension],
    )

    titulo = models.CharField('Título', max_length=50, null=True)

    # Almacena el string generado por la transformación del PDF
    texto = models.TextField('Texto', null=True)

    observaciones = models.TextField('Observaciones', null=True)

    departamentos = models.CharField(
        'Departamento',
        max_length=4,
        null=True,
        choices=DEPARTAMENTOS,
    )
    periodo = models.CharField(
        'Período',
        max_length=9,
        null=True,
        choices=PERIODOS,
    )
    ano = models.PositiveIntegerField('Año', choices=ANYOS, null=True)
