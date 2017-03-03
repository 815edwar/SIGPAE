# -*- coding: utf-8 -*-
from django.db import models
from django.core.exceptions import ValidationError
from datetime import date
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator



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

    codigo = models.CharField('Código', max_length=50, null=True)

    # Almacena el string generado por la transformación del PDF
    texto = models.TextField('Texto', null=True)

    denominacion = models.TextField('Denominación', null= True)

    periodo = models.CharField(
        'Período',
        max_length=9,
        null=True,
        choices=PERIODOS,
    )

    año = models.PositiveIntegerField('Año', choices=AÑOS, null=True)

    horas_semanales = models.PositiveIntegerField('Horas Semanales', null=True, validators=[MinValueValidator(0),
                                                             MaxValueValidator(40)])

    creditos = models.PositiveIntegerField('Créditos', null=True,  validators=[MinValueValidator(0),
                                                             MaxValueValidator(16)])

    requisitos = models.TextField('Requisitos', null=True)

    objetivos = models.TextField('Objetivos', null=True)

    sinopticos = models.TextField('Contenidos Sinópticos', null=True)

    estrategias_metodologicas = models.TextField('Estrategias Metodológicas', null=True)

    estrategias_evaluacion = models.TextField('Estrategias de Evaluación', null=True)

    ftes_info_recomendadas = models.TextField('Fuentes de Información Recomendadas', null=True)

    observaciones = models.TextField('Observaciones', null=True)

    departamento = models.ForeignKey(Departamento,verbose_name='Departamento', null=True)

    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)

