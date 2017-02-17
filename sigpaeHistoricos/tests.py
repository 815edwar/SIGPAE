from django.test import TestCase
from sigpaeHistoricos.models import *

#PRUEBAS

class TestPdf(TestCase):
	#Inicializando objetos para las pruebas
	def setUp(self):
		Pdfs.objects.create(periods="sep-dic")
		Pdfs.objects.create(periods="intensivo")

	#Prueba Frontera de creacion de periodos
	def test_create_periodo_sep_dic(self):
		sepDic = Periodos.objects.get(periods="sep-dic")
		self.assertEqual(sepDic.periods,"sep-dic")

	def test_create_periodo_intensivo(self):
		intensivo = Periodos.objects.get(periods="intensivo")
		self.assertEqual(intensivo.periods,"intensivo")

	def test_create_periodo_wrong(self):
		Periodos.objects.create(periods=4)
		intensivo = Periodos.objects.get(periods=4)
		self.assertNotEqual(intensivo.periods,4)




