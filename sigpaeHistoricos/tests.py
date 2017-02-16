from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from sigpaeHistoricos.models import *

class ModelsTestCase(TestCase):
	def setUp(self):
		self.periodo1 = Periodos.objects.create(periods = 'abr-jul')
		self.periodo2 = Periodos.objects.create(periods = 'ene-mar')
		self.periodo3 = Periodos.objects.create(periods = 'sep-dic')
		self.periodo4 = Periodos.objects.create(periods = 'intensivo')
		self.departamento1 = Departamentos.objects.create(departments = 'Departamento de Computación y Tecnología de Información')
		self.departamento2 = Departamentos.objects.create(departments = 'Departamento de Ciencia de los Materiales')
		self.departamento3 = Departamentos.objects.create(departments = 'Departamento de Física')
		self.departamento4 = Departamentos.objects.create(departments = 'Departamento de Procesos y Sistemas')
		self.departamento5 = Departamentos.objects.create(departments = 'Departamento de Termodinámica y Fenómenos de Transferencia')

	def test_periods(self):
		""" Se prueba que los campos estén iguales a su inicialización. """
		self.assertEqual(self.periodo1.periods, 'abr-jul')
		self.assertEqual(self.periodo2.periods, 'ene-mar')
		self.assertEqual(self.periodo3.periods, 'sep-dic')
		self.assertEqual(self.periodo4.periods, 'intensivo')

	def test_departments(self):
		""" Se prueba que los campos estén iguales a su inicialización. """
		self.assertEqual(self.departamento1.departments, 'Departamento de Computación y Tecnología de Información')
		self.assertEqual(self.departamento2.departments, 'Departamento de Ciencia de los Materiales')
		self.assertEqual(self.departamento3.departments, 'Departamento de Física')
		self.assertEqual(self.departamento4.departments, 'Departamento de Procesos y Sistemas')
		self.assertEqual(self.departamento5.departments, 'Departamento de Termodinámica y Fenómenos de Transferencia')

	def test_acronyms(self):
		""" Pruebo los acrónimos de cada clase. """
		self.assertEqual(self.periodo1.ABR_JUL, 'abr-jul')
		self.assertEqual(self.periodo2.ENE_MAR, 'ene-mar')
		self.assertEqual(self.periodo3.SEP_DIC, 'sep-dic')
		self.assertEqual(self.periodo4.VERANO, 'intensivo')

		self.assertEqual(self.departamento1.COMPUTACION_TI, 'DCTI')
		self.assertEqual(self.departamento2.CIENCIA_MATERIALES, 'DCM')
		self.assertEqual(self.departamento3.FISICA, 'DF')
		self.assertEqual(self.departamento4.PROCESOS_SISTEMAS, 'DPS')
		self.assertEqual(self.departamento5.TERMO_FENOMENOS, 'DTFT')
