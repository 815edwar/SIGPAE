# -*- coding: utf-8 -*-

from django.test import TestCase
from datetime import datetime, timezone
from sigpaeHistoricos.models import *

# Suit de pruebas para los modelos del sistema SIGPAE, junto a sus métodos.

class ModelsTestCase(TestCase):
	
	def setUp(self):

		# Departamentos de prueba.

		self.departamento1 = Departamento.objects.create(
			nombre="Departamento de Física",
		)

		self.departamento2 = Departamento.objects.create(
			nombre="Departamento de Computación y Tecnología de Información",
		)

		self.departamento3 = Departamento.objects.create(
			nombre="Departamento de Termodinámica y Fenómenos de Transferencia",
		)

		self.departamento4 = Departamento.objects.create(
			nombre="Departamento de Electrónica y Circuitos",
		)

		# Transcripciones de prueba.

		self.transcripcion1 = Transcripcion.objects.create(
			texto="Texto de prueba 1",
			codigo="CI2345",
			denominacion="Primero", 
			periodo="sep-dic",
			año="1969",
			horas_practica = 10,
			horas_teoria = 20,
			horas_laboratorio = 10,
			creditos=3,
			requisitos="CI1234, PS1234",
			objetivos="Desarrollar competencias en el área de bases de datos.",
			sinopticos="Un contenido maravilloso.",
			estrategias_metodologicas="Clases magistrales.",
			estrategias_evaluacion="Ocho exámenes parciales.",
			ftes_info_recomendadas="Aho, A., Lam, M., Sethi, R., y Ullman, J. Compilers.",
			observaciones="Primer curso de la cadena de realidad aumentada.",
			encargado = "Departamento de Computación y Tecnología de la Información",
			fecha_modificacion=datetime.now(timezone.utc),
		)

		self.transcripcion2 = Transcripcion.objects.create(
			texto="Texto de prueba 2",
			codigo="CI4891",
			denominacion="Segundo", 
			periodo="ene-mar",
			año="1999",
			horas_practica = 0,
			horas_teoria = 0,
			horas_laboratorio = 0,
			creditos=16,
			requisitos="Estructuras discretas III, Interfaces con el usuario",
			objetivos="Desarrollar competencias en el área de mecánica cuántica.",
			sinopticos="Contenido entretenido.",
			estrategias_metodologicas="Clases en línea.",
			estrategias_evaluacion="Un trabajo, una exposición y veinte mini-proyectos.",
			ftes_info_recomendadas="PURCELL. Octava edición.",
			observaciones="Curso sujeto a cambios.",
			encargado = "Departamento de Computación y Tecnología de la Información",
			fecha_modificacion=datetime.now(timezone.utc),
		)

		self.transcripcion3 = Transcripcion.objects.create(
			texto="Texto de prueba 3",
			codigo="CI1790",
			denominacion="Tercero", 
			periodo="abr-jul",
			año="2014",
			horas_practica = 40,
			horas_teoria = 0,
			horas_laboratorio = 0,
			creditos=0,
			requisitos="Algoritmos y estructuras II",
			objetivos="Desarrollar competencias en el área de palíndromos.",
			sinopticos="Aspectos varios de cualquier cosa.",
			estrategias_metodologicas="Clases a distancia y algunas sesiones personales.",
			estrategias_evaluacion="Un parcial de 100%.",
			ftes_info_recomendadas="Tanembaum, A. (2000). Redes de computadores.",
			observaciones="-",
			encargado = "Departamento de Computación y Tecnología de la Información",
			fecha_modificacion=datetime.now(timezone.utc),
		)

		self.transcripcion4 = Transcripcion.objects.create(
			texto="Texto de prueba 4",
			codigo="CI1010",
			denominacion="Cuarto",
			periodo="intensivo",
			año="2017",
			horas_practica = 0,
			horas_teoria = 0,
			horas_laboratorio = 40,
			creditos=12,
			requisitos="CI9876",
			objetivos="Desarrollar competencias en el área de suma y resta.",
			sinopticos="Contenidos diversos e interesantes.",
			estrategias_metodologicas="Clases magistrales una vez al mes.",
			estrategias_evaluacion="Tres parciales de 33,3%. 0,1% por asistencias.",
			ftes_info_recomendadas="Holy Bible.",
			observaciones="Nada particular.",
			encargado = "Departamento de Computación y Tecnología de la Información",
			fecha_modificacion=datetime.now(timezone.utc),
		)

		# Programas de prueba.

		self.programa1 = Programa.objects.create(
			codigo = "PS1111",
			denominacion = "Modelos lineales I",
			periodo = "ene-mar",
			año = "1983",
			horas_practica = 0,
			horas_teoria = 40,
			horas_laboratorio = 0,
			creditos = 4,
			requisitos = "CO3211",
			objetivos_generales = "Desallorar competencias a nivel de optimización de recursos y recorrido óptimo de caminos.",
			objetivos_especificos = "Aprender el método SIMPLEX, aprender sobre problemas de transporte y trasbordo.",
			sinopticos = "Métodos de optimización en general.",
			estrategias_metodologicas = "Clases magistrales y realización de numerosos ejercicios.",
			estrategias_evaluacion = "Tres exámenes parciales: 1) 30 %, 2) 30 %, 3) 40 %.",
			ftes_info_recomendadas = "Taha, A. Programación lineal.",
			encargado = "Departamento de Cómputo Científico y Estadística",
		)

		self.programa2 = Programa.objects.create(
			codigo = "CSA212",
			denominacion = "Venezuela ante el siglo XXI",
			periodo = "abr-jul",
			año = "2013",
			horas_practica = 20,
			horas_teoria = 0,
			horas_laboratorio = 20,
			creditos = 15,
			requisitos = "Ninguno.",
			objetivos_generales = "Aprender sobre el desarrollo de la humanidad como civilización.",
			objetivos_especificos = "Leer 'Ética para Amador' y otras lecturas random.",
			sinopticos = "Mucha historia.",
			estrategias_metodologicas = "Clases magistrales y asignación de innumerables lecturas.",
			estrategias_evaluacion = "Tres exámenes parciales, el primero y el segundo de 35 %, el último de 30 %.",
			ftes_info_recomendadas = "Todas las lecturas que el profesor mande.",
			encargado = "Departamento de Ciencias Sociales",
		)

		self.programa3 = Programa.objects.create(
			codigo = "MA2115",
			denominacion = "Matemáticas 4",
			periodo = "sep-dic",
			año = "2010",
			horas_practica = 20,
			horas_teoria = 20,
			horas_laboratorio = 0,
			creditos = 4,
			requisitos = "MA1113",
			objetivos_generales = "Utilizar serie y sucesiones, además de ecuaciones diferenciales.",
			objetivos_especificos = "Aprender serie de McLaurin, la de Taylor y los métodos para resolver ecuaciones diferenciales ordinarias.",
			sinopticos = "Matemática de la buena.",
			estrategias_metodologicas = "Clases magistrales y preparadurías.",
			estrategias_evaluacion = "Dos exámenes parciales de 50 %.",
			ftes_info_recomendadas = "Viola, Proli",
			encargado = "Departamento de Matemáticas Puras y Aplicadas",
		)

		self.programa4 = Programa.objects.create(
			codigo = "FS1112",
			denominacion = "Física II",
			periodo = "intensivo",
			año = "1970",
			horas_practica = 0,
			horas_teoria = 20,
			horas_laboratorio = 20,
			creditos = 1,
			requisitos = "FS1111",
			objetivos_generales = "Extender el conocimiento de física básico con conceptos como el torque y el momento angular.",
			objetivos_especificos = "Aprender dinámica rotacional, aspectos de gravitación universal y termodinámica.",
			sinopticos = "Física maravillosa.",
			estrategias_metodologicas = "Clases magistrales.",
			estrategias_evaluacion = "Tres exámenes parciales de 33,3%.",
			ftes_info_recomendadas = "Sears, Feynman.",
			encargado = "Departamento de Física",
		)

		# Prefijos de prueba.

		self.prefijo1 = Prefijo.objects.create(
			siglas = "EP",
			asociacion = "Cursos en Cooperación(Carreras Largas)",
			aprobado = True,
		)

		self.prefijo2 = Prefijo.objects.create(
			siglas = "BC",
			asociacion = "Departamento de Biología Celular",
			aprobado = False,
		)

		self.prefijo3 = Prefijo.objects.create(
			siglas = "CEA",
			asociacion = "Departamento de Ciencias Económicas y Administrativas",
			aprobado = False,
		)

		self.prefijo4 = Prefijo.objects.create(
			siglas = "CT",
			asociacion = "Departamento de Conversión y Transporte de Energía",
			aprobado = False,
		)

		# Decanatos de prueba.

		self.decanato1 = Decanato.objects.create(
			nombre = "Decanato de Estudios Generales",
		)

		self.decanato2 = Decanato.objects.create(
			nombre = "Decanato de Estudios Profesionales",
		)

		self.decanato3 = Decanato.objects.create(
			nombre = "Decanato de Estudios de Postgrado",
		)

		self.decanato4 = Decanato.objects.create(
			nombre = "Decanato de Estudios Tecnológicos",
		)

		# Coordinaciones de prueba.

		self.coordinacion1 = Coordinacion.objects.create(
			decanato = self.decanato2,
			nombre = "Coordinación de Comercio Exterior y Licenciatura en Comercio Internacional",
		)

		self.coordinacion2 = Coordinacion.objects.create(
			decanato = self.decanato3,
			nombre = "Coordinación de Ingeniería en Telecomunicaciones/Biomédica",
		)

		self.coordinacion3 = Coordinacion.objects.create(
			decanato = self.decanato1,
			nombre = "Coordinación de Formación General",
		)

		self.coordinacion4 = Coordinacion.objects.create(
			decanato = self.decanato4,
			nombre = "Coordinación de Tecnología Eléctrica y Electrónica",
		)

	# PRUEBAS UNITARIAS

	# PRUEBAS DE LA CLASE "Transcripcion"

	# Se prueba el campo "texto" y su correctitud.
	def test_texto(self):
		self.assertEqual(self.transcripcion1.texto, "Texto de prueba 1")
		self.assertEqual(self.transcripcion2.texto, "Texto de prueba 2")
		self.assertEqual(self.transcripcion3.texto, "Texto de prueba 3")
		self.assertEqual(self.transcripcion4.texto, "Texto de prueba 4")

	# Se prueba el campo "codigo" y su correctitud.
	def test_codigo(self):
		self.assertEqual(self.transcripcion1.codigo, "CI2345")
		self.assertEqual(self.transcripcion2.codigo, "CI4891")
		self.assertEqual(self.transcripcion3.codigo, "CI1790")
		self.assertEqual(self.transcripcion4.codigo, "CI1010")

	# Se prueba el campo "denominacion" y su correctitud.
	def test_denominacion(self):
		self.assertEqual(self.transcripcion1.denominacion, "Primero")
		self.assertEqual(self.transcripcion2.denominacion, "Segundo")
		self.assertEqual(self.transcripcion3.denominacion, "Tercero")
		self.assertEqual(self.transcripcion4.denominacion, "Cuarto")

	# Se prueba el campo "periodo" y su correctitud.
	def test_periodo(self):
		self.assertEqual(self.transcripcion1.periodo, "sep-dic")
		self.assertEqual(self.transcripcion1.SEP_DIC, "sep-dic")

		self.assertEqual(self.transcripcion2.periodo, "ene-mar")
		self.assertEqual(self.transcripcion2.ENE_MAR, "ene-mar")

		self.assertEqual(self.transcripcion3.periodo, "abr-jul")
		self.assertEqual(self.transcripcion3.ABR_JUL, "abr-jul")

		self.assertEqual(self.transcripcion4.periodo, "intensivo")
		self.assertEqual(self.transcripcion4.VERANO, "intensivo")

	# Se prueba el campo "año" y su correctitud.
	def test_año(self):
		self.assertEqual(self.transcripcion1.año, "1969")
		self.assertEqual(self.transcripcion2.año, "1999")
		self.assertEqual(self.transcripcion3.año, "2014")
		self.assertEqual(self.transcripcion4.año, "2017")

	# Se prueba el campo "horas_practica" y su correctitud.
	def test_horas_practica(self):
		self.assertEqual(self.transcripcion1.horas_practica, 10)
		self.assertEqual(self.transcripcion2.horas_practica, 0)
		self.assertEqual(self.transcripcion3.horas_practica, 40)
		self.assertEqual(self.transcripcion4.horas_practica, 0)

	# Se prueba el campo "horas_teoria" y su correctitud.
	def test_horas_teoria(self):
		self.assertEqual(self.transcripcion1.horas_teoria, 20)
		self.assertEqual(self.transcripcion2.horas_teoria, 0)
		self.assertEqual(self.transcripcion3.horas_teoria, 0)
		self.assertEqual(self.transcripcion4.horas_teoria, 0)

	# Se prueba el campo "horas_laboratorio" y su correctitud.
	def test_horas_laboratorio(self):
		self.assertEqual(self.transcripcion1.horas_laboratorio, 10)
		self.assertEqual(self.transcripcion2.horas_laboratorio, 0)
		self.assertEqual(self.transcripcion3.horas_laboratorio, 0)
		self.assertEqual(self.transcripcion4.horas_laboratorio, 40)

	# Se prueba el campo "creditos" y su correctitud.
	def test_creditos(self):
		self.assertEqual(self.transcripcion1.creditos, 3)
		self.assertEqual(self.transcripcion2.creditos, 16)
		self.assertEqual(self.transcripcion3.creditos, 0)
		self.assertEqual(self.transcripcion4.creditos, 12)

	# Se prueba el campo "requisitos" y su correctitud.
	def test_requisitos(self):
		self.assertEqual(self.transcripcion1.requisitos, "CI1234, PS1234")
		self.assertEqual(self.transcripcion2.requisitos, "Estructuras discretas III, Interfaces con el usuario")
		self.assertEqual(self.transcripcion3.requisitos, "Algoritmos y estructuras II")
		self.assertEqual(self.transcripcion4.requisitos, "CI9876")

	# Se prueba el campo "objetivos" y su correctitud.
	def test_objetivos(self):
		self.assertEqual(self.transcripcion1.objetivos, "Desarrollar competencias en el área de bases de datos.")
		self.assertEqual(self.transcripcion2.objetivos, "Desarrollar competencias en el área de mecánica cuántica.")
		self.assertEqual(self.transcripcion3.objetivos, "Desarrollar competencias en el área de palíndromos.")
		self.assertEqual(self.transcripcion4.objetivos, "Desarrollar competencias en el área de suma y resta.")

	# Se prueba el campo "sinopticos" y su correctitud.
	def test_sinopticos(self):
		self.assertEqual(self.transcripcion1.sinopticos, "Un contenido maravilloso.")
		self.assertEqual(self.transcripcion2.sinopticos, "Contenido entretenido.")
		self.assertEqual(self.transcripcion3.sinopticos, "Aspectos varios de cualquier cosa.")
		self.assertEqual(self.transcripcion4.sinopticos, "Contenidos diversos e interesantes.")

	# Se prueba el campo "estartegias_metodologicas" y su correctitud.
	def test_estrategias_metodologicas(self):
		self.assertEqual(self.transcripcion1.estrategias_metodologicas, "Clases magistrales.")
		self.assertEqual(self.transcripcion2.estrategias_metodologicas, "Clases en línea.")
		self.assertEqual(self.transcripcion3.estrategias_metodologicas, "Clases a distancia y algunas sesiones personales.")
		self.assertEqual(self.transcripcion4.estrategias_metodologicas, "Clases magistrales una vez al mes.")

	# Se prueba el campo "estrategias_evaluacion" y su correctitud.
	def test_estrategias_evaluacion(self):
		self.assertEqual(self.transcripcion1.estrategias_evaluacion, "Ocho exámenes parciales.")
		self.assertEqual(self.transcripcion2.estrategias_evaluacion, "Un trabajo, una exposición y veinte mini-proyectos.")
		self.assertEqual(self.transcripcion3.estrategias_evaluacion, "Un parcial de 100%.")
		self.assertEqual(self.transcripcion4.estrategias_evaluacion, "Tres parciales de 33,3%. 0,1% por asistencias.")

	# Se prueba el campo "ftes_info_recomendadas" y su correctitud.
	def test_fuentes_informacion(self):
		self.assertEqual(self.transcripcion1.ftes_info_recomendadas, "Aho, A., Lam, M., Sethi, R., y Ullman, J. Compilers.")
		self.assertEqual(self.transcripcion2.ftes_info_recomendadas, "PURCELL. Octava edición.")
		self.assertEqual(self.transcripcion3.ftes_info_recomendadas, "Tanembaum, A. (2000). Redes de computadores.")
		self.assertEqual(self.transcripcion4.ftes_info_recomendadas, "Holy Bible.")

	# Se prueba el campo "observaciones" y su correctitud.
	def test_observaciones(self):
		self.assertEqual(self.transcripcion1.observaciones, "Primer curso de la cadena de realidad aumentada.")
		self.assertEqual(self.transcripcion2.observaciones, "Curso sujeto a cambios.")
		self.assertEqual(self.transcripcion3.observaciones, "-")
		self.assertEqual(self.transcripcion4.observaciones, "Nada particular.")

	# Se prueba el campo "encargado" y su correctitud.
	def test_encargado(self):
		self.assertEqual(self.transcripcion1.encargado, "Departamento de Computación y Tecnología de la Información")
		self.assertEqual(self.transcripcion2.encargado, "Departamento de Computación y Tecnología de la Información")
		self.assertEqual(self.transcripcion3.encargado, "Departamento de Computación y Tecnología de la Información")
		self.assertEqual(self.transcripcion4.encargado, "Departamento de Computación y Tecnología de la Información")

	# Se prueba el campo "fecha_modificacion" y su correctitud.
	def test_fecha_modificacion(self):
		self.assertLess(self.transcripcion1.fecha_modificacion, datetime.now(timezone.utc))
		self.assertLess(self.transcripcion2.fecha_modificacion, datetime.now(timezone.utc))
		self.assertLess(self.transcripcion3.fecha_modificacion, datetime.now(timezone.utc))
		self.assertLess(self.transcripcion4.fecha_modificacion, datetime.now(timezone.utc))

	"""
	# Se prueba el campo "departamento" y su correctitud.
	def test_departamento(self):
		self.assertEqual(self.transcripcion1.departamento.__str__(), "Departamento de Física")
		self.assertEqual(self.transcripcion2.departamento.__str__(), "Departamento de Computación y Tecnología de Información")
		self.assertEqual(self.transcripcion3.departamento.__str__(), "Departamento de Termodinámica y Fenómenos de Transferencia")
		self.assertEqual(self.transcripcion4.departamento.__str__(), "Departamento de Electrónica y Circuitos")
	"""

	# PRUEBAS DE LA CLASE "Departamento"

	# Se prueba el campo "nombre" y su correctitud.
	def test_nombre_departamento(self):
		self.assertEqual(self.departamento1.nombre, "Departamento de Física")
		self.assertEqual(self.departamento2.nombre, "Departamento de Computación y Tecnología de Información")
		self.assertEqual(self.departamento3.nombre, "Departamento de Termodinámica y Fenómenos de Transferencia")
		self.assertEqual(self.departamento4.nombre, "Departamento de Electrónica y Circuitos")

	# Se prueba el método "__str__" y su correcto funcionamiento.
	def test_str_method_dpto(self):
		self.assertEqual(self.departamento1.nombre, self.departamento1.__str__())
		self.assertEqual(self.departamento2.nombre, self.departamento2.__str__())
		self.assertEqual(self.departamento3.nombre, self.departamento3.__str__())
		self.assertEqual(self.departamento4.nombre, self.departamento4.__str__())

	# PRUEBAS DE LA CLASE "Prefijo"

	# Se prueba el campo "siglas" y su correctitud.
	def test_siglas(self):
		self.assertEqual(self.prefijo1.siglas, "EP")
		self.assertEqual(self.prefijo2.siglas, "BC")
		self.assertEqual(self.prefijo3.siglas, "CEA")
		self.assertEqual(self.prefijo4.siglas, "CT")

	# Se prueba el campo "asociacion" y su correctitud.
	def test_asociacion(self):
		self.assertEqual(self.prefijo1.asociacion, "Cursos en Cooperación(Carreras Largas)")
		self.assertEqual(self.prefijo2.asociacion, "Departamento de Biología Celular")
		self.assertEqual(self.prefijo3.asociacion, "Departamento de Ciencias Económicas y Administrativas")
		self.assertEqual(self.prefijo4.asociacion, "Departamento de Conversión y Transporte de Energía")

	# Se prueba el campo "aprobado" y su correctitud.
	def test_aprobacion(self):
		self.assertEqual(self.prefijo1.aprobado, True)
		self.assertEqual(self.prefijo2.aprobado, False)
		self.assertEqual(self.prefijo3.aprobado, False)
		self.assertEqual(self.prefijo4.aprobado, False)

	# PRUEBAS DE LA CLASE "Decanato"

	# Se prueba el campo "nombre" y su correctitud.
	def test_nombre_decanato(self):
		self.assertEqual(self.decanato1.nombre, "Decanato de Estudios Generales")
		self.assertEqual(self.decanato2.nombre, "Decanato de Estudios Profesionales")
		self.assertEqual(self.decanato3.nombre, "Decanato de Estudios de Postgrado")
		self.assertEqual(self.decanato4.nombre, "Decanato de Estudios Tecnológicos")

	# Se prueba el método "__str__" y su correcto funcionamiento.
	def test_str_method_decanato(self):
		self.assertEqual(self.decanato1.nombre, self.decanato1.__str__())
		self.assertEqual(self.decanato2.nombre, self.decanato2.__str__())
		self.assertEqual(self.decanato3.nombre, self.decanato3.__str__())
		self.assertEqual(self.decanato4.nombre, self.decanato4.__str__())

	# PRUEBAS DE LA CLASE "Coordinacion"

	# Se prueba el campo "decanato", el cual es una clave foránea de otra clase, para determinar su correcto funcionamiento.
	def test_decanato_coord(self):
		self.assertEqual(self.coordinacion1.decanato.__str__(), "Decanato de Estudios Profesionales")
		self.assertEqual(self.coordinacion2.decanato.__str__(), "Decanato de Estudios de Postgrado")
		self.assertEqual(self.coordinacion3.decanato.__str__(), "Decanato de Estudios Generales")
		self.assertEqual(self.coordinacion4.decanato.__str__(), "Decanato de Estudios Tecnológicos")

	# Se prueba el campo "nombre" y su correcto funcionamiento.
	def test_nombre_coord(self):
		self.assertEqual(self.coordinacion1.nombre, "Coordinación de Comercio Exterior y Licenciatura en Comercio Internacional")
		self.assertEqual(self.coordinacion2.nombre, "Coordinación de Ingeniería en Telecomunicaciones/Biomédica")
		self.assertEqual(self.coordinacion3.nombre, "Coordinación de Formación General")
		self.assertEqual(self.coordinacion4.nombre, "Coordinación de Tecnología Eléctrica y Electrónica")

	# Se prueba el método "__str__" y su correcto funcionamiento.
	def test_str_method_coord(self):
		self.assertEqual(self.coordinacion1.nombre, self.coordinacion1.__str__())
		self.assertEqual(self.coordinacion2.nombre, self.coordinacion2.__str__())
		self.assertEqual(self.coordinacion3.nombre, self.coordinacion3.__str__())
		self.assertEqual(self.coordinacion4.nombre, self.coordinacion4.__str__())

	# PRUEBAS DE LA CLASE "Programa"

	# Se prueba el campo "codigo" y su correctitud.
	def test_codigo_prog(self):
		self.assertEqual(self.programa1.codigo, "PS1111")
		self.assertEqual(self.programa2.codigo, "CSA212")
		self.assertEqual(self.programa3.codigo, "MA2115")
		self.assertEqual(self.programa4.codigo, "FS1112")

	# Se prueba el campo "denominacion" y su correctitud.
	def test_denominacion_prog(self):
		self.assertEqual(self.programa1.denominacion, "Modelos lineales I")
		self.assertEqual(self.programa2.denominacion, "Venezuela ante el siglo XXI")
		self.assertEqual(self.programa3.denominacion, "Matemáticas 4")
		self.assertEqual(self.programa4.denominacion, "Física II")

	# Se prueba el campo "periodo" y su correctitud.
	def test_periodo_prog(self):
		self.assertEqual(self.programa1.periodo, "ene-mar")
		self.assertEqual(self.programa1.ENE_MAR, "ene-mar")

		self.assertEqual(self.programa2.periodo, "abr-jul")
		self.assertEqual(self.programa2.ABR_JUL, "abr-jul")

		self.assertEqual(self.programa3.periodo, "sep-dic")
		self.assertEqual(self.programa3.SEP_DIC, "sep-dic")

		self.assertEqual(self.programa4.periodo, "intensivo")
		self.assertEqual(self.programa4.VERANO, "intensivo")

	# Se prueba el campo "año" y su correctitud.
	def test_año_prog(self):
		self.assertEqual(self.programa1.año, "1983")
		self.assertEqual(self.programa2.año, "2013")
		self.assertEqual(self.programa3.año, "2010")
		self.assertEqual(self.programa4.año, "1970")

	# Se prueba el campo "horas_practica" y su correctitud.
	def test_horas_practica_prog(self):
		self.assertEqual(self.programa1.horas_practica, 0)
		self.assertEqual(self.programa2.horas_practica, 20)
		self.assertEqual(self.programa3.horas_practica, 20)
		self.assertEqual(self.programa4.horas_practica, 0)

	# Se prueba el campo "horas_teoria" y su correctitud.
	def test_horas_teoria_prog(self):
		self.assertEqual(self.programa1.horas_teoria, 40)
		self.assertEqual(self.programa2.horas_teoria, 0)
		self.assertEqual(self.programa3.horas_teoria, 20)
		self.assertEqual(self.programa4.horas_teoria, 20)

	# Se prueba el campo "horas_laboratorio" y su correctitud.
	def test_horas_laboratorio_prog(self):
		self.assertEqual(self.programa1.horas_laboratorio, 0)
		self.assertEqual(self.programa2.horas_laboratorio, 20)
		self.assertEqual(self.programa3.horas_laboratorio, 0)
		self.assertEqual(self.programa4.horas_laboratorio, 20)

	# Se prueba el campo "creditos" y su correctitud.
	def test_creditos_prog(self):
		self.assertEqual(self.programa1.creditos, 4)
		self.assertEqual(self.programa2.creditos, 15)
		self.assertEqual(self.programa3.creditos, 4)
		self.assertEqual(self.programa4.creditos, 1)

	# Se prueba el campo "requisitos" y su correctitud.
	def test_requisitos_prog(self):
		self.assertEqual(self.programa1.requisitos, "CO3211")
		self.assertEqual(self.programa2.requisitos, "Ninguno.")
		self.assertEqual(self.programa3.requisitos, "MA1113")
		self.assertEqual(self.programa4.requisitos, "FS1111")

	# Se prueba el campo "objetivos_generales" y su correctitud.
	def test_objetivos_generales(self):
		self.assertEqual(self.programa1.objetivos_generales, "Desallorar competencias a nivel de optimización de recursos y recorrido óptimo de caminos.")
		self.assertEqual(self.programa2.objetivos_generales, "Aprender sobre el desarrollo de la humanidad como civilización.")
		self.assertEqual(self.programa3.objetivos_generales, "Utilizar serie y sucesiones, además de ecuaciones diferenciales.")
		self.assertEqual(self.programa4.objetivos_generales, "Extender el conocimiento de física básico con conceptos como el torque y el momento angular.")

	# Se prueba el campo "objetivos_especificos" y su correctitud.
	def test_objetivos_especificos(self):
		self.assertEqual(self.programa1.objetivos_especificos, "Aprender el método SIMPLEX, aprender sobre problemas de transporte y trasbordo.")
		self.assertEqual(self.programa2.objetivos_especificos, "Leer 'Ética para Amador' y otras lecturas random.")
		self.assertEqual(self.programa3.objetivos_especificos, "Aprender serie de McLaurin, la de Taylor y los métodos para resolver ecuaciones diferenciales ordinarias.")
		self.assertEqual(self.programa4.objetivos_especificos, "Aprender dinámica rotacional, aspectos de gravitación universal y termodinámica.")

	# Se prueba el campo "sinopticos" y su correctitud.
	def test_sinopticos_prog(self):
		self.assertEqual(self.programa1.sinopticos, "Métodos de optimización en general.")
		self.assertEqual(self.programa2.sinopticos, "Mucha historia.")
		self.assertEqual(self.programa3.sinopticos, "Matemática de la buena.")
		self.assertEqual(self.programa4.sinopticos, "Física maravillosa.")

	# Se prueba el campo "estartegias_metodologicas" y su correctitud.
	def test_estrategias_metodologicas_prog(self):
		self.assertEqual(self.programa1.estrategias_metodologicas, "Clases magistrales y realización de numerosos ejercicios.")
		self.assertEqual(self.programa2.estrategias_metodologicas, "Clases magistrales y asignación de innumerables lecturas.")
		self.assertEqual(self.programa3.estrategias_metodologicas, "Clases magistrales y preparadurías.")
		self.assertEqual(self.programa4.estrategias_metodologicas, "Clases magistrales.")

	# Se prueba el campo "estrategias_evaluacion" y su correctitud.
	def test_estrategias_evaluacion_prog(self):
		self.assertEqual(self.programa1.estrategias_evaluacion, "Tres exámenes parciales: 1) 30 %, 2) 30 %, 3) 40 %.")
		self.assertEqual(self.programa2.estrategias_evaluacion, "Tres exámenes parciales, el primero y el segundo de 35 %, el último de 30 %.")
		self.assertEqual(self.programa3.estrategias_evaluacion, "Dos exámenes parciales de 50 %.")
		self.assertEqual(self.programa4.estrategias_evaluacion, "Tres exámenes parciales de 33,3%.")

	# Se prueba el campo "ftes_info_recomendadas" y su correctitud.
	def test_fuentes_informacion_prog(self):
		self.assertEqual(self.programa1.ftes_info_recomendadas, "Taha, A. Programación lineal.")
		self.assertEqual(self.programa2.ftes_info_recomendadas, "Todas las lecturas que el profesor mande.")
		self.assertEqual(self.programa3.ftes_info_recomendadas, "Viola, Proli")
		self.assertEqual(self.programa4.ftes_info_recomendadas, "Sears, Feynman.")

	# Se prueba el campo "encargado" y su correctitud.
	def test_encargado_prog(self):
		self.assertEqual(self.programa1.encargado, "Departamento de Cómputo Científico y Estadística")
		self.assertEqual(self.programa2.encargado, "Departamento de Ciencias Sociales")
		self.assertEqual(self.programa3.encargado, "Departamento de Matemáticas Puras y Aplicadas")
		self.assertEqual(self.programa4.encargado, "Departamento de Física")

	# Se prueba el método "__str__" y su correcto funcionamiento.
	def test_str_method_prog(self):
		self.assertEqual(self.programa1.denominacion, self.programa1.__str__())
		self.assertEqual(self.programa2.denominacion, self.programa2.__str__())
		self.assertEqual(self.programa3.denominacion, self.programa3.__str__())
		self.assertEqual(self.programa4.denominacion, self.programa4.__str__())
