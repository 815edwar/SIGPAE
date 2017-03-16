# -*- coding: utf-8 -*-

from django.test import TestCase
from datetime import datetime, timezone
from sigpaeHistoricos.models import *


# Create your tests here.

class PDFTestCase(TestCase):
    def setUp(self):
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

        self.pdf1 = Transcripcion.objects.create(
            titulo="Programa 1",
            texto="Texto de prueba 1",
            denominacion="Primero",
            periodo="sep-dic",
            año="1969",
            horas_semanales=0,
            creditos=3,
            requisitos="CI1234, PS1234",
            objetivos="Desarrollar competencias en el área de bases de datos.",
            sinopticos="Un contenido maravilloso.",
            estrategias_metodologicas="Clases magistrales.",
            estrategias_evaluacion="Ocho exámenes parciales.",
            ftes_info_recomendadas="Aho, A., Lam, M., Sethi, R., y Ullman, J. Compilers.",
            observaciones="Primer curso de la cadena de realidad aumentada.",
            departamento=self.departamento1,
            fecha_modificacion=datetime.now(timezone.utc),
        )

        self.pdf2 = Transcripcion.objects.create(
            titulo="Programa 2",
            texto="Texto de prueba 2",
            denominacion="Segundo",
            periodo="ene-mar",
            año="1999",
            horas_semanales=40,
            creditos=16,
            requisitos="Estrcuturas discretas III, Interfaces con el usuario",
            objetivos="Desarrollar competencias en el área de mecánica cuántica.",
            sinopticos="Contenido entretenido.",
            estrategias_metodologicas="Clases en línea.",
            estrategias_evaluacion="Un trabajo, una exposición y veinte mini-proyectos.",
            ftes_info_recomendadas="PURCELL. Octava edición.",
            observaciones="Curso sujeto a cambios.",
            departamento=self.departamento2,
            fecha_modificacion=datetime.now(timezone.utc),
        )

        self.pdf3 = Transcripcion.objects.create(
            titulo="Programa 3",
            texto="Texto de prueba 3",
            denominacion="Tercero",
            periodo="abr-jul",
            año="2014",
            horas_semanales=12,
            creditos=0,
            requisitos="Algoritmos y estructuras II",
            objetivos="Desarrollar competencias en el área de palíndromos.",
            sinopticos="Aspectos varios de cualquier cosa.",
            estrategias_metodologicas="Clases a distancia y algunas sesiones personales.",
            estrategias_evaluacion="Un parcial de 100%.",
            ftes_info_recomendadas="Tanembaum, A. (2000). Redes de computadores.",
            observaciones="-",
            departamento=self.departamento3,
            fecha_modificacion=datetime.now(timezone.utc),
        )

        self.pdf4 = Transcripcion.objects.create(
            titulo="Programa 4",
            texto="Texto de prueba 4",
            denominacion="Cuarto",
            periodo="intensivo",
            año="2017",
            horas_semanales=25,
            creditos=12,
            requisitos="CI9876",
            objetivos="Desarrollar competencias en el área de suma y resta.",
            sinopticos="Contenidos diversos e interesantes.",
            estrategias_metodologicas="Clases magistrales una vez al mes.",
            estrategias_evaluacion="Tres parciales de 33,3%. 0,1% por asistencias.",
            ftes_info_recomendadas="Holy Bible.",
            observaciones="Nada particular.",
            departamento=self.departamento4,
            fecha_modificacion=datetime.now(timezone.utc),
        )

    # PRUEBAS UNITARIAS

    # PRUEBAS DE LA CLASE "Transcripcion"

    # Se prueba el campo "titulo" y su correctitud.
    def test_titulo(self):
        self.assertEqual(self.pdf1.titulo, "Programa 1")
        self.assertEqual(self.pdf2.titulo, "Programa 2")
        self.assertEqual(self.pdf3.titulo, "Programa 3")
        self.assertEqual(self.pdf4.titulo, "Programa 4")

    # Se prueba el campo "texto" y su correctitud.
    def test_texto(self):
        self.assertEqual(self.pdf1.texto, "Texto de prueba 1")
        self.assertEqual(self.pdf2.texto, "Texto de prueba 2")
        self.assertEqual(self.pdf3.texto, "Texto de prueba 3")
        self.assertEqual(self.pdf4.texto, "Texto de prueba 4")

    # Se prueba el campo "denominacion" y su correctitud.
    def test_denominacion(self):
        self.assertEqual(self.pdf1.denominacion, "Primero")
        self.assertEqual(self.pdf2.denominacion, "Segundo")
        self.assertEqual(self.pdf3.denominacion, "Tercero")
        self.assertEqual(self.pdf4.denominacion, "Cuarto")

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

    # Se prueba el campo "año" y su correctitud.
    def test_año(self):
        self.assertEqual(self.pdf1.año, "1969")
        self.assertEqual(self.pdf2.año, "1999")
        self.assertEqual(self.pdf3.año, "2014")
        self.assertEqual(self.pdf4.año, "2017")

    # Se prueba el campo "horas_semanales" y su correctitud.
    def test_horas_semanales(self):
        self.assertEqual(self.pdf1.horas_semanales, 0)
        self.assertEqual(self.pdf2.horas_semanales, 40)
        self.assertEqual(self.pdf3.horas_semanales, 12)
        self.assertEqual(self.pdf4.horas_semanales, 25)

    # Se prueba el campo "creditos" y su correctitud.
    def test_creditos(self):
        self.assertEqual(self.pdf1.creditos, 3)
        self.assertEqual(self.pdf2.creditos, 16)
        self.assertEqual(self.pdf3.creditos, 0)
        self.assertEqual(self.pdf4.creditos, 12)

    # Se prueba el campo "requisitos" y su correctitud.
    def test_requisitos(self):
        self.assertEqual(self.pdf1.requisitos, "CI1234, PS1234")
        self.assertEqual(self.pdf2.requisitos, "Estrcuturas discretas III, Interfaces con el usuario")
        self.assertEqual(self.pdf3.requisitos, "Algoritmos y estructuras II")
        self.assertEqual(self.pdf4.requisitos, "CI9876")

    # Se prueba el campo "objetivos" y su correctitud.
    def test_objetivos(self):
        self.assertEqual(self.pdf1.objetivos, "Desarrollar competencias en el área de bases de datos.")
        self.assertEqual(self.pdf2.objetivos, "Desarrollar competencias en el área de mecánica cuántica.")
        self.assertEqual(self.pdf3.objetivos, "Desarrollar competencias en el área de palíndromos.")
        self.assertEqual(self.pdf4.objetivos, "Desarrollar competencias en el área de suma y resta.")

    # Se prueba el campo "sinopticos" y su correctitud.
    def test_sinopticos(self):
        self.assertEqual(self.pdf1.sinopticos, "Un contenido maravilloso.")
        self.assertEqual(self.pdf2.sinopticos, "Contenido entretenido.")
        self.assertEqual(self.pdf3.sinopticos, "Aspectos varios de cualquier cosa.")
        self.assertEqual(self.pdf4.sinopticos, "Contenidos diversos e interesantes.")

    # Se prueba el campo "estartegias_metodologicas" y su correctitud.
    def test_estrategias_metodologicas(self):
        self.assertEqual(self.pdf1.estrategias_metodologicas, "Clases magistrales.")
        self.assertEqual(self.pdf2.estrategias_metodologicas, "Clases en línea.")
        self.assertEqual(self.pdf3.estrategias_metodologicas, "Clases a distancia y algunas sesiones personales.")
        self.assertEqual(self.pdf4.estrategias_metodologicas, "Clases magistrales una vez al mes.")

    # Se prueba el campo "estrategias_evaluacion" y su correctitud.
    def test_estrategias_evaluacion(self):
        self.assertEqual(self.pdf1.estrategias_evaluacion, "Ocho exámenes parciales.")
        self.assertEqual(self.pdf2.estrategias_evaluacion, "Un trabajo, una exposición y veinte mini-proyectos.")
        self.assertEqual(self.pdf3.estrategias_evaluacion, "Un parcial de 100%.")
        self.assertEqual(self.pdf4.estrategias_evaluacion, "Tres parciales de 33,3%. 0,1% por asistencias.")

    # Se prueba el campo "ftes_info_recomendadas" y su correctitud.
    def test_fuentes_informacion(self):
        self.assertEqual(self.pdf1.ftes_info_recomendadas, "Aho, A., Lam, M., Sethi, R., y Ullman, J. Compilers.")
        self.assertEqual(self.pdf2.ftes_info_recomendadas, "PURCELL. Octava edición.")
        self.assertEqual(self.pdf3.ftes_info_recomendadas, "Tanembaum, A. (2000). Redes de computadores.")
        self.assertEqual(self.pdf4.ftes_info_recomendadas, "Holy Bible.")

    # Se prueba el campo "observaciones" y su correctitud.
    def test_observaciones(self):
        self.assertEqual(self.pdf1.observaciones, "Primer curso de la cadena de realidad aumentada.")
        self.assertEqual(self.pdf2.observaciones, "Curso sujeto a cambios.")
        self.assertEqual(self.pdf3.observaciones, "-")
        self.assertEqual(self.pdf4.observaciones, "Nada particular.")

    # Se prueba el campo "fecha_modificacion" y su correctitud.
    def test_fecha_modificacion(self):
        self.assertLess(self.pdf1.fecha_modificacion, datetime.now(timezone.utc))
        self.assertLess(self.pdf2.fecha_modificacion, datetime.now(timezone.utc))
        self.assertLess(self.pdf3.fecha_modificacion, datetime.now(timezone.utc))
        self.assertLess(self.pdf4.fecha_modificacion, datetime.now(timezone.utc))

    # Se prueba el campo "departamento" y su correctitud.
    def test_departamento(self):
        self.assertEqual(self.pdf1.departamento.__str__(), "Departamento de Física")
        self.assertEqual(self.pdf2.departamento.__str__(), "Departamento de Computación y Tecnología de Información")
        self.assertEqual(self.pdf3.departamento.__str__(), "Departamento de Termodinámica y Fenómenos de Transferencia")
        self.assertEqual(self.pdf4.departamento.__str__(), "Departamento de Electrónica y Circuitos")

    # PRUEBAS DE LA CLASE "Departamentos"

    # Se prueba el campo "nombre" y su correctitud.
    def test_nombre_departamento(self):
        self.assertEqual(self.departamento1.nombre, "Departamento de Física")
        self.assertEqual(self.departamento2.nombre, "Departamento de Computación y Tecnología de Información")
        self.assertEqual(self.departamento3.nombre, "Departamento de Termodinámica y Fenómenos de Transferencia")
        self.assertEqual(self.departamento4.nombre, "Departamento de Electrónica y Circuitos")
