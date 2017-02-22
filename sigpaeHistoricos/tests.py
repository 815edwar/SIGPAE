from django.test import TestCase

# Create your tests here.
# -*- coding: utf-8 -*-

from django.test import TestCase
from sigpaeHistoricos.models import *

# Create your tests here.

class PDFTestCase(TestCase):
	
	def setUp(self):
		self.pdf1 = Pdfs.objects.create(
			titulo="Programa 1",
			texto="Amarillo", 
			observaciones="Primero", 
			departamentos="Departamento de Física",
			periodo="sep-dic",
			ano="1969",
		)

		self.pdf2 = Pdfs.objects.create(
			titulo="Programa 2",
			texto="Azul", 
			observaciones="Segundo", 
			departamentos="Departamento de Computación y Tecnología de Información",
			periodo="ene-mar",
			ano="1999",
		)

		self.pdf3 = Pdfs.objects.create(
			titulo="Programa 3",
			texto="Rojo", 
			observaciones="Tercero", 
			departamentos="Departamento de Termodinámica y Fenómenos de Transferencia",
			periodo="abr-jul",
			ano="2014",
		)

		self.pdf4 = Pdfs.objects.create(
			titulo="Programa 4",
			texto="Blanco", 
			observaciones="Cuarto", 
			departamentos="Departamento de Electrónica y Circuitos",
			periodo="intensivo",
			ano="2017",
		)

	# PRUEBAS UNITARIAS

	# Se prueba el campo "titulo" y su correctitud.
	def test_titulo(self):
		self.assertEqual(self.pdf1.titulo, "Programa 1")
		self.assertEqual(self.pdf2.titulo, "Programa 2")
		self.assertEqual(self.pdf3.titulo, "Programa 3")
		self.assertEqual(self.pdf4.titulo, "Programa 4")

	# Se prueba el campo "texto" y su correctitud.
	def test_texto(self):
		self.assertEqual(self.pdf1.texto, "Amarillo")
		self.assertEqual(self.pdf2.texto, "Azul")
		self.assertEqual(self.pdf3.texto, "Rojo")
		self.assertEqual(self.pdf4.texto, "Blanco")

	# Se prueba el campo "observaciones" y su correctitud.
	def test_observaciones(self):
		self.assertEqual(self.pdf1.observaciones, "Primero")
		self.assertEqual(self.pdf2.observaciones, "Segundo")
		self.assertEqual(self.pdf3.observaciones, "Tercero")
		self.assertEqual(self.pdf4.observaciones, "Cuarto")

	# Se prueba el campo "departamentos" y su correctitud.
	def test_departamento(self):
		self.assertEqual(self.pdf1.departamentos, "Departamento de Física")
		self.assertEqual(self.pdf1.FISICA, "DF")

		self.assertEqual(self.pdf2.departamentos, "Departamento de Computación y Tecnología de Información")
		self.assertEqual(self.pdf2.COMPUTACION_TI, "DCTI")

		self.assertEqual(self.pdf3.departamentos, "Departamento de Termodinámica y Fenómenos de Transferencia")
		self.assertEqual(self.pdf3.TERMO_FENOMENOS, "DTFT")

		self.assertEqual(self.pdf4.departamentos, "Departamento de Electrónica y Circuitos")
		self.assertEqual(self.pdf4.ELECTRONICA_CIRCUITOS, "DEC")

	# Se prueba el campo "periodo" y su correctitud.
	def test_periodo(self):
		self.assertEqual(self.pdf1.periodo, "sep-dic")
		self.assertEqual(self.pdf1.SEP_DIC, "sep-dic")

		self.assertEqual(self.pdf2.periodo, "ene-mar")
		self.assertEqual(self.pdf2.ENE_MAR, "ene-mar")

		self.assertEqual(self.pdf3.periodo, "abr-jul")
		self.assertEqual(self.pdf3.ABR_JUL, "abr-jul")

		self.assertEqual(self.pdf4.periodo, "intensivo")
		self.assertEqual(self.pdf4.VERANO, "intensivo")

	# Se prueba el campo "ano" y su correctitud.
	def test_ano(self):
		self.assertEqual(self.pdf1.ano, "1969")
		self.assertEqual(self.pdf2.ano, "1999")
		self.assertEqual(self.pdf3.ano, "2014")
		self.assertEqual(self.pdf4.ano, "2017")
