from django.db import models

# Create your models here.
# -*- coding: utf-8 -*-

from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.



# Validador para el formato pdf de los archivos a subir.
def valid_extension(value):
    if not value.name.endswith('.pdf'):
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


    # Salva los PDF en /media/uploads/año/mes/día
    pdf = models.FileField(
		upload_to='uploads/',
        validators=[valid_extension],
    )

    # Almacena el string generado por la transformación del PDF
    text = models.TextField(null=True)

    departmentos = models.CharField(
        max_length=4,
        null=True,
        choices=DEPARTAMENTOS,
    )
    periodo = models.CharField(
        max_length=9,
        null=True,
        choices=PERIODOS,
    )
