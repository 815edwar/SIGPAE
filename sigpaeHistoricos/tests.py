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
			año=1969,
			horas_practica = 10,
			horas_teoria = 20,
			horas_laboratorio = 10,
			creditos=3,
			sinopticos="Un contenido maravilloso.",
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
			año=1999,
			horas_practica = 0,
			horas_teoria = 0,
			horas_laboratorio = 0,
			creditos=16,
			sinopticos="Contenido entretenido.",
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
			año=2014,
			horas_practica = 40,
			horas_teoria = 0,
			horas_laboratorio = 0,
			creditos=0,
			sinopticos="Aspectos varios de cualquier cosa.",
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
			año=2017,
			horas_practica = 0,
			horas_teoria = 0,
			horas_laboratorio = 40,
			creditos=12,
			sinopticos="Contenidos diversos e interesantes.",
			ftes_info_recomendadas="Holy Bible.",
			observaciones="Nada particular.",
			encargado = "Departamento de Computación y Tecnología de la Información",
			fecha_modificacion=datetime.now(timezone.utc),
		)

		# Programas de prueba.

		self.programa1 = Programa.objects.create(
			#codigo = "PS1111",
			#denominacion = "Modelos lineales I",
			fecha_vigTrim = "ene-mar",
			fecha_vigAno = 1983,
			h_prac = 0,
			h_teoria = 40,
			h_lab = 0,
			#creditos = 4,
			#requisitos = "CO3211",
			obj_g = "Desallorar competencias a nivel de optimización de recursos y recorrido óptimo de caminos.",
			obj_e = "Aprender el método SIMPLEX, aprender sobre problemas de transporte y trasbordo.",
			contenidos = "Departamento de Cómputo Científico y Estadística",
			sinoptico = "Métodos de optimización en general.",
			estrategias = "Clases magistrales y realización de numerosos ejercicios.",
			estrat_eval = "Tres exámenes parciales: 1) 30 %, 2) 30 %, 3) 40 %.",
			fuentes = "Taha, A. Programación lineal.",
			cronograma = "Martes 5-6, Jueves 5-6.",
			#encargado = "Departamento de Cómputo Científico y Estadística",
		)

		self.programa2 = Programa.objects.create(
			#codigo = "CSA212",
			#denominacion = "Venezuela ante el siglo XXI",
			fecha_vigTrim = "abr-jul",
			fecha_vigAno = 2013,
			h_prac = 20,
			h_teoria = 0,
			h_lab = 20,
			#creditos = 15,
			#requisitos = "Ninguno.",
			obj_g = "Aprender sobre el desarrollo de la humanidad como civilización.",
			obj_e = "Leer 'Ética para Amador' y otras lecturas random.",
			contenidos = "Departamento de Ciencias Sociales",
			sinoptico = "Mucha historia.",
			estrategias = "Clases magistrales y asignación de innumerables lecturas.",
			estrat_eval = "Tres exámenes parciales, el primero y el segundo de 35 %, el último de 30 %.",
			fuentes = "Todas las lecturas que el profesor mande.",
			cronograma = "Lunes 1-2, Miércoles 1-2.",
			#encargado = "Departamento de Ciencias Sociales",
		)

		self.programa3 = Programa.objects.create(
			#codigo = "MA2115",
			#denominacion = "Matemáticas 4",
			fecha_vigTrim = "sep-dic",
			fecha_vigAno = 2010,
			h_prac = 20,
			h_teoria = 20,
			h_lab = 0,
			#creditos = 4,
			#requisitos = "MA1113",
			obj_g = "Utilizar serie y sucesiones, además de ecuaciones diferenciales.",
			obj_e = "Aprender serie de McLaurin, la de Taylor y los métodos para resolver ecuaciones diferenciales ordinarias.",
			contenidos = "Departamento de Matemáticas Puras y Aplicadas",
			sinoptico = "Matemática de la buena.",
			estrategias = "Clases magistrales y preparadurías.",
			estrat_eval = "Dos exámenes parciales de 50 %.",
			fuentes = "Viola, Proli",
			cronograma = "Lunes 1-2, Miércoles 1-2, Viernes 1-2.",
			#encargado = "Departamento de Matemáticas Puras y Aplicadas",
		)

		self.programa4 = Programa.objects.create(
			#codigo = "FS1112",
			#denominacion = "Física II",
			fecha_vigTrim = "intensivo",
			fecha_vigAno = 1970,
			h_prac = 0,
			h_teoria = 20,
			h_lab = 20,
			#creditos = 1,
			#requisitos = "FS1111",
			obj_g = "Extender el conocimiento de física básico con conceptos como el torque y el momento angular.",
			obj_e= "Aprender dinámica rotacional, aspectos de gravitación universal y termodinámica.",
			contenidos = "Departamento de Física",
			sinoptico = "Física maravillosa.",
			estrategias = "Clases magistrales.",
			estrat_eval = "Tres exámenes parciales de 33,3%.",
			fuentes = "Sears, Feynman.",
			cronograma = "Lunes 3-4, Miércoles 3-4, Viernes 3-4.",
			#encargado = "Departamento de Física",
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

		# Campos adicionales de prueba.

		self.campoAd1 = CampoAdicional.objects.create(
			nombre = "Estrategias prácticas.",
		)

		self.campoAd2 = CampoAdicional.objects.create(
			nombre = "Objetivos a largo plazo.",
		)

		self.campoAd3 = CampoAdicional.objects.create(
			nombre = "Requisitos adicionales.",
		)

		self.campoAd4 = CampoAdicional.objects.create(
			nombre = "Fundamentos.",
		)

		# Contenidos extra de prueba.

		self.contenidoExtra1 = ContenidoExtra.objects.create(
			transcripcion = self.transcripcion1,
			campo_adicional = self.campoAd1,
			contenido = "Información 1.",
		)

		self.contenidoExtra2 = ContenidoExtra.objects.create(
			transcripcion = self.transcripcion2,
			campo_adicional = self.campoAd2,
			contenido = "Información 2.",
		)

		self.contenidoExtra3 = ContenidoExtra.objects.create(
			transcripcion = self.transcripcion3,
			campo_adicional = self.campoAd3,
			contenido = "Información 3.",
		)

		self.contenidoExtra4 = ContenidoExtra.objects.create(
			transcripcion = self.transcripcion4,
			campo_adicional = self.campoAd4,
			contenido = "Información 4.",
		)

		# Solicitudes de prueba.

		self.solicitud1 = Solicitud.objects.create(
    		coordinacion = "Coordinación de Matemáticas Aplicadas",
    		porasignar = False,
    		porrevisarD = True,
    		porrevisarP = True,
    		rechazadoC = False,
    		validadoC = False,
    		enviadoD = True,
    		devueltoD = False,
    		fecha_elaboracion = datetime.now(timezone.utc),
    		tipo_solicitud = "Normal",
    		subtipo_solicitud = "Graduación",
    		nivel = "Alto",
    		codigo = "PS1111",
        	codigo_anterior = "-",
    		denominacion = "Modelos lineales I",
    		creditos = 4,
    		tipo_aula = "Grande",
    		horas_teoria = True,
    		horas_practica = True,
    		horas_laboratorio = True,
    		trim = "ene-mar",
    		año = "1983",
    		accion = "Envío",
    		carrera = "Ingeniería de computación.",
    		trim_pensum = True,
    		requisitos_cred =  False,
    		permiso_coord = False,
    		tipo_materia = "Teórico-práctica",
    		clase_materia = "Profesional",
    		observaciones = "Ninguna.",
    		vigente = True,
    		validadodace= False,
    		especial = False,
    		imparticion = "Ana Borges",
    		decanato = "No adscrito.",
    		obsanul = "-",
    		programa = self.programa1,
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
		self.assertEqual(self.transcripcion1.año, 1969)
		self.assertEqual(self.transcripcion2.año, 1999)
		self.assertEqual(self.transcripcion3.año, 2014)
		self.assertEqual(self.transcripcion4.año, 2017)

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

	"""
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
	"""

	# Se prueba el campo "sinopticos" y su correctitud.
	def test_sinopticos(self):
		self.assertEqual(self.transcripcion1.sinopticos, "Un contenido maravilloso.")
		self.assertEqual(self.transcripcion2.sinopticos, "Contenido entretenido.")
		self.assertEqual(self.transcripcion3.sinopticos, "Aspectos varios de cualquier cosa.")
		self.assertEqual(self.transcripcion4.sinopticos, "Contenidos diversos e interesantes.")

	"""
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
	"""

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
	"""
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
	"""

	# Se prueba el campo "fecha_vigTrim" y su correctitud.
	def test_fecha_VigTrim(self):
		self.assertEqual(self.programa1.fecha_vigTrim, "ene-mar")
		self.assertEqual(self.programa1.ENE_MAR, "ene-mar")

		self.assertEqual(self.programa2.fecha_vigTrim, "abr-jul")
		self.assertEqual(self.programa2.ABR_JUL, "abr-jul")

		self.assertEqual(self.programa3.fecha_vigTrim, "sep-dic")
		self.assertEqual(self.programa3.SEP_DIC, "sep-dic")

		self.assertEqual(self.programa4.fecha_vigTrim, "intensivo")
		self.assertEqual(self.programa4.VERANO, "intensivo")

	# Se prueba el campo "fecha_vigAno" y su correctitud.
	def test_fecha_VigAno(self):
		self.assertEqual(self.programa1.fecha_vigAno, 1983)
		self.assertEqual(self.programa2.fecha_vigAno, 2013)
		self.assertEqual(self.programa3.fecha_vigAno, 2010)
		self.assertEqual(self.programa4.fecha_vigAno, 1970)

	# Se prueba el campo "horas_practica" y su correctitud.
	def test_horas_practica_prog(self):
		self.assertEqual(self.programa1.h_prac, 0)
		self.assertEqual(self.programa2.h_prac, 20)
		self.assertEqual(self.programa3.h_prac, 20)
		self.assertEqual(self.programa4.h_prac, 0)

	# Se prueba el campo "horas_teoria" y su correctitud.
	def test_horas_teoria_prog(self):
		self.assertEqual(self.programa1.h_teoria, 40)
		self.assertEqual(self.programa2.h_teoria, 0)
		self.assertEqual(self.programa3.h_teoria, 20)
		self.assertEqual(self.programa4.h_teoria, 20)

	# Se prueba el campo "horas_laboratorio" y su correctitud.
	def test_horas_laboratorio_prog(self):
		self.assertEqual(self.programa1.h_lab, 0)
		self.assertEqual(self.programa2.h_lab, 20)
		self.assertEqual(self.programa3.h_lab, 0)
		self.assertEqual(self.programa4.h_lab, 20)

	"""
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
	"""

	# Se prueba el campo "objetivos_generales" y su correctitud.
	def test_objetivos_generales(self):
		self.assertEqual(self.programa1.obj_g, "Desallorar competencias a nivel de optimización de recursos y recorrido óptimo de caminos.")
		self.assertEqual(self.programa2.obj_g, "Aprender sobre el desarrollo de la humanidad como civilización.")
		self.assertEqual(self.programa3.obj_g, "Utilizar serie y sucesiones, además de ecuaciones diferenciales.")
		self.assertEqual(self.programa4.obj_g, "Extender el conocimiento de física básico con conceptos como el torque y el momento angular.")

	# Se prueba el campo "objetivos_especificos" y su correctitud.
	def test_objetivos_especificos(self):
		self.assertEqual(self.programa1.obj_e, "Aprender el método SIMPLEX, aprender sobre problemas de transporte y trasbordo.")
		self.assertEqual(self.programa2.obj_e, "Leer 'Ética para Amador' y otras lecturas random.")
		self.assertEqual(self.programa3.obj_e, "Aprender serie de McLaurin, la de Taylor y los métodos para resolver ecuaciones diferenciales ordinarias.")
		self.assertEqual(self.programa4.obj_e, "Aprender dinámica rotacional, aspectos de gravitación universal y termodinámica.")

	# Se prueba el campo "sinopticos" y su correctitud.
	def test_sinopticos_prog(self):
		self.assertEqual(self.programa1.sinoptico, "Métodos de optimización en general.")
		self.assertEqual(self.programa2.sinoptico, "Mucha historia.")
		self.assertEqual(self.programa3.sinoptico, "Matemática de la buena.")
		self.assertEqual(self.programa4.sinoptico, "Física maravillosa.")

	# Se prueba el campo "estartegias_metodologicas" y su correctitud.
	def test_estrategias_metodologicas_prog(self):
		self.assertEqual(self.programa1.estrategias, "Clases magistrales y realización de numerosos ejercicios.")
		self.assertEqual(self.programa2.estrategias, "Clases magistrales y asignación de innumerables lecturas.")
		self.assertEqual(self.programa3.estrategias, "Clases magistrales y preparadurías.")
		self.assertEqual(self.programa4.estrategias, "Clases magistrales.")

	# Se prueba el campo "estrategias_evaluacion" y su correctitud.
	def test_estrategias_evaluacion_prog(self):
		self.assertEqual(self.programa1.estrat_eval, "Tres exámenes parciales: 1) 30 %, 2) 30 %, 3) 40 %.")
		self.assertEqual(self.programa2.estrat_eval, "Tres exámenes parciales, el primero y el segundo de 35 %, el último de 30 %.")
		self.assertEqual(self.programa3.estrat_eval, "Dos exámenes parciales de 50 %.")
		self.assertEqual(self.programa4.estrat_eval, "Tres exámenes parciales de 33,3%.")

	# Se prueba el campo "ftes_info_recomendadas" y su correctitud.
	def test_fuentes_informacion_prog(self):
		self.assertEqual(self.programa1.fuentes, "Taha, A. Programación lineal.")
		self.assertEqual(self.programa2.fuentes, "Todas las lecturas que el profesor mande.")
		self.assertEqual(self.programa3.fuentes, "Viola, Proli")
		self.assertEqual(self.programa4.fuentes, "Sears, Feynman.")

	# Se prueba el campo "contenidos" y su correctitud.
	def test_contenido(self):
		self.assertEqual(self.programa1.contenidos, "Departamento de Cómputo Científico y Estadística")
		self.assertEqual(self.programa2.contenidos, "Departamento de Ciencias Sociales")
		self.assertEqual(self.programa3.contenidos, "Departamento de Matemáticas Puras y Aplicadas")
		self.assertEqual(self.programa4.contenidos, "Departamento de Física")

	# Se prueba el campo "cronograma" y su correctitud.
	def test_cronograma(self):
		self.assertEqual(self.programa1.cronograma, "Martes 5-6, Jueves 5-6.")
		self.assertEqual(self.programa2.cronograma, "Lunes 1-2, Miércoles 1-2.")
		self.assertEqual(self.programa3.cronograma, "Lunes 1-2, Miércoles 1-2, Viernes 1-2.")
		self.assertEqual(self.programa4.cronograma, "Lunes 3-4, Miércoles 3-4, Viernes 3-4.")	

	"""
	# Se prueba el campo "encargado" y su correctitud.
	def test_encargado_prog(self):
		self.assertEqual(self.programa1.encargado, "Departamento de Cómputo Científico y Estadística")
		self.assertEqual(self.programa2.encargado, "Departamento de Ciencias Sociales")
		self.assertEqual(self.programa3.encargado, "Departamento de Matemáticas Puras y Aplicadas")
		self.assertEqual(self.programa4.encargado, "Departamento de Física")
	"""

	# Se prueba el método "__str__" y su correcto funcionamiento.
	def test_str_method_prog(self):
		self.assertEqual(self.programa1.contenidos, self.programa1.__str__())
		self.assertEqual(self.programa2.contenidos, self.programa2.__str__())
		self.assertEqual(self.programa3.contenidos, self.programa3.__str__())
		self.assertEqual(self.programa4.contenidos, self.programa4.__str__())

	# PRUEBAS DE LA CLASE "CampoAdicional"

	# Se prueba el campo "nombre" y su correctitud.
	def test_nombre_campAd(self):
		self.assertEqual(self.campoAd1.nombre, "Estrategias prácticas.")
		self.assertEqual(self.campoAd2.nombre, "Objetivos a largo plazo.")
		self.assertEqual(self.campoAd3.nombre, "Requisitos adicionales.")
		self.assertEqual(self.campoAd4.nombre, "Fundamentos.")

	# Se prueba el método "__str__" y su correcto funcionamiento.
	def test_str_method_campAd(self):
		self.assertEqual(self.campoAd1.nombre, self.campoAd1.__str__())
		self.assertEqual(self.campoAd2.nombre, self.campoAd2.__str__())
		self.assertEqual(self.campoAd3.nombre, self.campoAd3.__str__())
		self.assertEqual(self.campoAd4.nombre, self.campoAd4.__str__())

	# PRUEBAS DE LA CLASE "ContenidoExtra"

	# Se prueba el campo "transcripcion", el cual es una referencia a las transcripciones, y su correctitud.
	def test_transcripcion_contEx(self):
		self.assertEqual(self.contenidoExtra1.transcripcion, self.transcripcion1)
		self.assertEqual(self.contenidoExtra2.transcripcion, self.transcripcion2)
		self.assertEqual(self.contenidoExtra3.transcripcion, self.transcripcion3)
		self.assertEqual(self.contenidoExtra4.transcripcion, self.transcripcion4)

	# Se prueba el campo "campo_adicional", el cual es una referencia a los campos adicionales, y su correctitud.
	def test_campoAd_contEx(self):
		self.assertEqual(self.contenidoExtra1.campo_adicional, self.campoAd1)
		self.assertEqual(self.contenidoExtra2.campo_adicional, self.campoAd2)
		self.assertEqual(self.contenidoExtra3.campo_adicional, self.campoAd3)
		self.assertEqual(self.contenidoExtra4.campo_adicional, self.campoAd4)

	# Se prueba el campo "contenido" y su correctitud.
	def test_contenido_contEx(self):
		self.assertEqual(self.contenidoExtra1.contenido, "Información 1.")
		self.assertEqual(self.contenidoExtra2.contenido, "Información 2.")
		self.assertEqual(self.contenidoExtra3.contenido, "Información 3.")
		self.assertEqual(self.contenidoExtra4.contenido, "Información 4.")

	# PRUEBAS DE LA CLASE "Solicitud"

	# Se prueba el campo "coordinacion" y su correctitud.
	def test_coord_sol(self):
		self.assertEqual(self.solicitud1.coordinacion, "Coordinación de Matemáticas Aplicadas")

	# Se prueba el campo "porasignar" y su correctitud.
	def test_porasig_sol(self):
		if (self.solicitud1.porasignar == True):
			self.assertEqual(self.solicitud1.porasignar, True)
		else:
			self.assertEqual(self.solicitud1.porasignar, False)

	# Se prueba el campo "porrevisarD" y su correctitud.
	def test_porrevisarD_sol(self):
		if (self.solicitud1.porrevisarD == True):
			self.assertEqual(self.solicitud1.porrevisarD, True)
		else:
			self.assertEqual(self.solicitud1.porrevisarD, False)

	# Se prueba el campo "porrevisarP" y su correctitud.
	def test_porrevisarP_sol(self):
		if (self.solicitud1.porrevisarP == True):
			self.assertEqual(self.solicitud1.porrevisarP, True)
		else:
			self.assertEqual(self.solicitud1.porrevisarP, False)

	# Se prueba el campo "rechazadoC" y su correctitud.
	def test_rechazadoC_sol(self):
		if (self.solicitud1.rechazadoC == True):
			self.assertEqual(self.solicitud1.rechazadoC, True)
		else:
			self.assertEqual(self.solicitud1.rechazadoC, False)

	# Se prueba el campo "validadoC" y su correctitud.
	def test_validadoC_sol(self):
		if (self.solicitud1.validadoC == True):
			self.assertEqual(self.solicitud1.validadoC, True)
		else:
			self.assertEqual(self.solicitud1.validadoC, False)

	# Se prueba el campo "enviadoD" y su correctitud.
	def test_enviadoD_sol(self):
		if (self.solicitud1.enviadoD == True):
			self.assertEqual(self.solicitud1.enviadoD, True)
		else:
			self.assertEqual(self.solicitud1.enviadoD, False)

	# Se prueba el campo "devueltoD" y su correctitud.
	def test_devueltoD_sol(self):
		if (self.solicitud1.devueltoD == True):
			self.assertEqual(self.solicitud1.devueltoD, True)
		else:
			self.assertEqual(self.solicitud1.devueltoD, False)

	# Se prueba el campo "fecha_elaboracion" y su correctitud.
	def test_fecha_elaboracion_sol(self):
		self.assertLess(self.solicitud1.fecha_elaboracion, datetime.now(timezone.utc))

	# Se prueba el campo "tipo_solicitud" y su correctitud.
	def test_tipo_solicitud_sol(self):
		self.assertEqual(self.solicitud1.tipo_solicitud, "Normal")

	# Se prueba el campo "subtipo_solicitud" y su correctitud.
	def test_subtipo_solicitud_sol(self):
		self.assertEqual(self.solicitud1.subtipo_solicitud, "Graduación")

	# Se prueba el campo "nivel" y su correctitud.
	def test_nivel_sol(self):
		self.assertEqual(self.solicitud1.nivel, "Alto")

	# Se prueba el campo "codigo" y su correctitud.
	def test_codigo_sol(self):
		self.assertEqual(self.solicitud1.codigo, "PS1111")

	# Se prueba el campo "codigo_anterior" y su correctitud.
	def test_codigo_anterior_sol(self):
		self.assertEqual(self.solicitud1.codigo_anterior, "-")

	# Se prueba el campo "denominacion" y su correctitud.
	def test_denominacion_sol(self):
		self.assertEqual(self.solicitud1.denominacion, "Modelos lineales I")

	# Se prueba el campo "creditos" y su correctitud.
	def test_creditos_sol(self):
		self.assertEqual(self.solicitud1.creditos, 4)

	# Se prueba el campo "tipo_aula" y su correctitud.
	def test_tipo_aula_sol(self):
		self.assertEqual(self.solicitud1.tipo_aula, "Grande")

	# Se prueba el campo "horas_teoria" y su correctitud.
	def test_horas_teoria_sol(self):
		if (self.solicitud1.horas_teoria == True):
			self.assertEqual(self.solicitud1.horas_teoria, True)
		else:
			self.assertEqual(self.solicitud1.horas_teoria, False)

	# Se prueba el campo "horas_practica" y su correctitud.
	def test_horas_practica_sol(self):
		if (self.solicitud1.horas_practica == True):
			self.assertEqual(self.solicitud1.horas_practica, True)
		else:
			self.assertEqual(self.solicitud1.horas_practica, False)

	# Se prueba el campo "horas_laboratorio" y su correctitud.
	def test_horas_laboratorio_sol(self):
		if (self.solicitud1.horas_laboratorio == True):
			self.assertEqual(self.solicitud1.horas_laboratorio, True)
		else:
			self.assertEqual(self.solicitud1.horas_laboratorio, False)

	# Se prueba el campo "trim" y su correctitud.
	def test_trim_sol(self):
		self.assertEqual(self.solicitud1.trim, "ene-mar")

	# Se prueba el campo "año" y su correctitud.
	def test_año_sol(self):
		self.assertEqual(self.solicitud1.año, "1983")

	# Se prueba el campo "accion" y su correctitud.
	def test_accion_sol(self):
		self.assertEqual(self.solicitud1.accion, "Envío")

	# Se prueba el campo "carrera" y su correctitud.
	def test_carrera_sol(self):
		self.assertEqual(self.solicitud1.carrera, "Ingeniería de computación.")

	# Se prueba el campo "trim_pensum" y su correctitud.
	def test_trim_pensum_sol(self):
		if (self.solicitud1.trim_pensum == True):
			self.assertEqual(self.solicitud1.trim_pensum, True)
		else:
			self.assertEqual(self.solicitud1.trim_pensum, False)

	# Se prueba el campo "requisitos_cred" y su correctitud.
	def test_requisitos_cred_sol(self):
		if (self.solicitud1.requisitos_cred == True):
			self.assertEqual(self.solicitud1.requisitos_cred, True)
		else:
			self.assertEqual(self.solicitud1.requisitos_cred, False)

	# Se prueba el campo "permiso_coord" y su correctitud.
	def test_permiso_coord_sol(self):
		if (self.solicitud1.permiso_coord == True):
			self.assertEqual(self.solicitud1.permiso_coord, True)
		else:
			self.assertEqual(self.solicitud1.permiso_coord, False)

	# Se prueba el campo "tipo_materia" y su correctitud.
	def test_tipo_materia_sol(self):
		self.assertEqual(self.solicitud1.tipo_materia, "Teórico-práctica")

	# Se prueba el campo "clase_materia" y su correctitud.
	def test_clase_materia_sol(self):
		self.assertEqual(self.solicitud1.clase_materia, "Profesional")

	# Se prueba el campo "observaciones" y su correctitud.
	def test_observaciones_sol(self):
		self.assertEqual(self.solicitud1.observaciones, "Ninguna.")

	# Se prueba el campo "vigente" y su correctitud.
	def test_vigente_sol(self):
		if (self.solicitud1.vigente == True):
			self.assertEqual(self.solicitud1.vigente, True)
		else:
			self.assertEqual(self.solicitud1.vigente, False)

	# Se prueba el campo "validadodace" y su correctitud.
	def test_validadodace_sol(self):
		if (self.solicitud1.validadodace == True):
			self.assertEqual(self.solicitud1.validadodace, True)
		else:
			self.assertEqual(self.solicitud1.validadodace, False)

	# Se prueba el campo "especial" y su correctitud.
	def test_permiso_coord_sol(self):
		if (self.solicitud1.especial == True):
			self.assertEqual(self.solicitud1.especial, True)
		else:
			self.assertEqual(self.solicitud1.especial, False)

	# Se prueba el campo "imparticion" y su correctitud.
	def test_imparticion_sol(self):
		self.assertEqual(self.solicitud1.imparticion, "Ana Borges")

	# Se prueba el campo "decanato" y su correctitud.
	def test_decanato_sol(self):
		self.assertEqual(self.solicitud1.decanato, "No adscrito.")

	# Se prueba el campo "obsanul" y su correctitud.
	def test_obsanul_sol(self):
		self.assertEqual(self.solicitud1.obsanul, "-")

	# Se prueba el campo "programa", el cual es una referencia a los programas, y su correctitud.
	def test_programa_sol(self):
		self.assertEqual(self.solicitud1.programa, self.programa1)