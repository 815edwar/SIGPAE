# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

class Periodos(models.Model):
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

	periods = models.CharField(
		max_length = 9,
		choices = PERIODOS,
	)

class Departamentos(models.Model):
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
		(CIENCIA_MATERIALES,'Departamento de Ciencia de los Materiales'),
		(CIENCIAS_TIERRA,'Departamento de Ciencias de la Tierra'),
		(COMPUTACION_TI,'Departamento de Computación y Tecnología de Información'),
		(COMPUTO_CIENTIFICO,'Departamento de Cómputo Científico y Estadística'),
		(CONVERSION_TRANSPORTE,'Departamento de Conversión y Transporte de Energía'),
		(ELECTRONICA_CIRCUITOS,'Departamento de Electrónica y Circuitos'),
		(FISICA,'Departamento de Física'),
		(MATEMATICAS,'Departamento de Matemáticas Puras y Aplicadas'),
		(MECANICA,'Departamento de Mecánica'),
		(PROCESOS_SISTEMAS,'Departamento de Procesos y Sistemas'),
		(QUIMICA,'Departamento de Química'),
		(TERMO_FENOMENOS,'Departamento de Termodinámica y Fenómenos de Transferencia'),
	)

	departments = models.CharField(
		max_length = 4,
		choices = DEPARTAMENTOS,
	)

