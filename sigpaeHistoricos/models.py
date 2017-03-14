# -*- coding: utf-8 -*-
from django.db import models
from django.core.exceptions import ValidationError
from datetime import date
from django.core.validators import MinValueValidator, MaxValueValidator


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


class Decanato(models.Model):
    nombre = models.CharField('Nombre', max_length=100, null=True)

    def __str__(self):
        return self.nombre


class Coordinacion(models.Model):
    decanato = models.ForeignKey(Decanato, verbose_name='Decanato', null=True)
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

    denominacion = models.TextField('Denominación', null=True)

    periodo = models.CharField(
        'Período',
        max_length=9,
        null=True,
        choices=PERIODOS,
    )

    año = models.PositiveIntegerField('Año', choices=AÑOS, null=True)

    horas_practica = models.PositiveIntegerField('Horas de práctica', null=True, default=0)

    horas_teoria = models.PositiveIntegerField('Horas de teoría', null=True, default=0)

    horas_laboratorio = models.PositiveIntegerField('Horas de laboratorio', null=True, default=0)

    creditos = models.PositiveIntegerField('Créditos', null=True, validators=[MinValueValidator(0),
                                                                              MaxValueValidator(16)])

    requisitos = models.TextField('Requisitos', null=True)

    objetivos = models.TextField('Objetivos', null=True)

    sinopticos = models.TextField('Contenidos Sinópticos', null=True)

    estrategias_metodologicas = models.TextField('Estrategias Metodológicas', null=True)

    estrategias_evaluacion = models.TextField('Estrategias de Evaluación', null=True)

    ftes_info_recomendadas = models.TextField('Fuentes de Información Recomendadas', null=True)

    observaciones = models.TextField('Observaciones', null=True)

    encargado = models.CharField('Encargado', max_length=100, null=True)

    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)


'''
class Asignatura(models.Model):
    codasig = models.CharField(primary_key=True, max_length=500)
    nombre = models.CharField(max_length=500)
    tipo = models.CharField(max_length=15)

    class Meta:
        db_table = 'asignatura'


class Bitacora(models.Model):
    usbid = models.CharField(max_length=60)
    comentario = models.CharField(max_length=500)
    fecha = models.DateTimeField()

    class Meta:
        db_table = 'bitacora'
        unique_together = (('usbid', 'id', 'fecha', 'comentario'),)


class CampoImpartir(models.Model):
    nombre = models.CharField(primary_key=True, max_length=50)

    class Meta:
        db_table = 'campo_impartir'


class CampoNivel(models.Model):
    nombre = models.CharField(primary_key=True, max_length=50)

    class Meta:
        db_table = 'campo_nivel'


class Carrera(models.Model):
    codigo = models.CharField(primary_key=True, max_length=500)
    nombre = models.CharField(max_length=500)

    class Meta:
        db_table = 'carrera'


class ClaseMateria(models.Model):
    nombre = models.CharField(primary_key=True, max_length=50)

    class Meta:
        db_table = 'clase_materia'


class Coordinacion(models.Model):
    usbid = models.CharField(primary_key=True, max_length=50)
    codcar = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'coordinacion'


class Decanato(models.Model):
    usbid = models.CharField(primary_key=True, max_length=50)
    obligatorio = models.BooleanField()

    class Meta:
        db_table = 'decanato'


class Departamento(models.Model):
    usbid = models.CharField(primary_key=True, max_length=50)

    class Meta:
        db_table = 'departamento'


class Devueltosdace(models.Model):
    usbidda = models.CharField(max_length=50)
    usbidr = models.CharField(max_length=50)
    
    observacionesrd = models.CharField(max_length=500)
    num = models.AutoField(primary_key=True)

    class Meta:
        db_table = 'devueltosdace'


class EsRequisito(models.Model):
    codpre = models.CharField(max_length=500)
    cod = models.CharField(max_length=500)

    class Meta:
        db_table = 'es_requisito'
        unique_together = (('codpre', 'cod'),)


class Estudiante(models.Model):
    usbid = models.CharField(primary_key=True, max_length=50)
    cedula = models.CharField(max_length=20)
    tipo_estudiante = models.CharField(max_length=50)

    class Meta:
        db_table = 'estudiante'


class Generados(models.Model):
    fecha = models.DateField()
    nro_pag = models.IntegerField()
    nro_prog = models.IntegerField()

    class Meta:
        db_table = 'generados'


class Historico(models.Model):
    codasig = models.CharField(max_length=8)
    nomasig = models.CharField(max_length=500)
    trimestrei = models.CharField(max_length=8)
    anoi = models.IntegerField()
    trimestref = models.CharField(max_length=8, blank=True, null=True)
    anof = models.IntegerField(blank=True, null=True)
    ruta = models.CharField(max_length=500)

    class Meta:
        db_table = 'historico'


class Profesor(models.Model):
    usbid = models.CharField(primary_key=True, max_length=50)

    class Meta:
        db_table = 'profesor'


class ProgTemp(models.Model):
    idprog = models.IntegerField()
    idtemp = models.IntegerField()
    idpla = models.IntegerField()

    class Meta:
        db_table = 'prog_temp'
        unique_together = (('idprog', 'idtemp', 'idpla'),)


class Programa(models.Model):
    h_teoria = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    h_prac = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    h_lab = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    fecha_vigtrim = models.CharField(max_length=8, blank=True, null=True)
    fecha_vigano = models.IntegerField(blank=True, null=True)
    obj_g = models.CharField(max_length=500, blank=True, null=True)
    obj_e = models.CharField(max_length=500, blank=True, null=True)
    contenidos = models.CharField(max_length=500, blank=True, null=True)
    estrategias = models.CharField(max_length=500, blank=True, null=True)
    estrat_eval = models.CharField(max_length=500, blank=True, null=True)
    fuentes = models.CharField(max_length=500, blank=True, null=True)
    cronograma = models.CharField(max_length=500, blank=True, null=True)
    sinoptico = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'programa'


class Programat(models.Model):
    h_teoria = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    h_prac = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    h_lab = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    fecha_vigtrim = models.CharField(max_length=8, blank=True, null=True)
    fecha_vigano = models.IntegerField(blank=True, null=True)
    obj_g = models.CharField(max_length=500, blank=True, null=True)
    obj_e = models.CharField(max_length=500, blank=True, null=True)
    contenidos = models.CharField(max_length=500, blank=True, null=True)
    estrategias = models.CharField(max_length=500, blank=True, null=True)
    estrat_eval = models.CharField(max_length=500, blank=True, null=True)
    fuentes = models.CharField(max_length=500, blank=True, null=True)
    cronograma = models.CharField(max_length=500, blank=True, null=True)
    sinoptico = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'programat'


class RBitPlan(models.Model):
    idplanilla = models.IntegerField()
    idbitacora = models.IntegerField()

    class Meta:
        db_table = 'r_bit_plan'
        unique_together = (('idplanilla', 'idbitacora'),)


class RCarMat(models.Model):
    codasig = models.CharField(max_length=8)
    codcar = models.CharField(max_length=500)

    class Meta:
        db_table = 'r_car_mat'
        unique_together = (('codasig', 'codcar'),)


class RCoordPl(models.Model):
    usbid = models.CharField(max_length=50)
    

    class Meta:
        db_table = 'r_coord_pl'
        unique_together = (('usbid', 'id'),)


class RDecCoor(models.Model):
    usbiddec = models.CharField(max_length=50)
    usbidcoor = models.CharField(max_length=50)

    class Meta:
        db_table = 'r_dec_coor'
        unique_together = (('usbiddec', 'usbidcoor'),)


class RDecPl(models.Model):
    idplanilla = models.IntegerField()
    usbiddec = models.CharField(max_length=50)

    class Meta:
        db_table = 'r_dec_pl'
        unique_together = (('idplanilla', 'usbiddec'),)


class RDepPl(models.Model):
    idplanilla = models.IntegerField()
    usbidd = models.CharField(max_length=50)

    class Meta:
        db_table = 'r_dep_pl'
        unique_together = (('idplanilla', 'usbidd'),)


class REstHist(models.Model):
    usbid = models.CharField(max_length=50)
    

    class Meta:
        db_table = 'r_est_hist'
        unique_together = (('usbid', 'id'),)


class REstProg(models.Model):
    usbid = models.CharField(max_length=500)
    

    class Meta:
        db_table = 'r_est_prog'
        unique_together = (('usbid', 'id'),)


class RProfDep(models.Model):
    usbidp = models.CharField(max_length=50)
    usbidd = models.CharField(max_length=50)

    class Meta:
        db_table = 'r_prof_dep'
        unique_together = (('usbidp', 'usbidd'),)


class RProfPl(models.Model):
    usbid = models.CharField(max_length=50)
    
    idplanilla = models.IntegerField()

    class Meta:
        db_table = 'r_prof_pl'
        unique_together = (('usbid', 'id'),)


class RProfTemp(models.Model):
    idtemp = models.IntegerField()
    usbid = models.CharField(max_length=30)
    idplanilla = models.IntegerField()

    class Meta:
        db_table = 'r_prof_temp'
        unique_together = (('idtemp', 'usbid'),)


class RProgPl(models.Model):
    idplanilla = models.IntegerField()
    idprograma = models.IntegerField()

    class Meta:
        db_table = 'r_prog_pl'
        unique_together = (('idplanilla', 'idprograma'),)


class Rechazadoscad(models.Model):
    usbidc = models.CharField(max_length=50)
    usbidd = models.CharField(max_length=50)
    id = models.IntegerField()
    observacionesrd = models.CharField(max_length=500)
    num = models.AutoField(primary_key=True)

    class Meta:
        db_table = 'rechazadoscad'


class Rechazadosd(models.Model):
    usbidd = models.CharField(max_length=50)
    usbidp = models.CharField(max_length=50)
    
    observacionesrd = models.CharField(max_length=500)
    num = models.AutoField(primary_key=True)

    class Meta:
        db_table = 'rechazadosd'


class Rechazadosdac(models.Model):
    usbidd = models.CharField(max_length=50)
    usbidc = models.CharField(max_length=50)
    
    observacionesrd = models.CharField(max_length=500)
    num = models.AutoField(primary_key=True)

    class Meta:
        db_table = 'rechazadosdac'


class Rechazadosdecac(models.Model):
    usbiddec = models.CharField(max_length=50)
    usbidcor = models.CharField(max_length=50)
    
    observacionesrd = models.CharField(max_length=500)
    num = models.AutoField(primary_key=True)

    class Meta:
        db_table = 'rechazadosdecac'


class Rechazadosp(models.Model):
    usbidd = models.CharField(max_length=50)
    usbidp = models.CharField(max_length=50)
    
    observacionesrd = models.CharField(max_length=500)
    num = models.AutoField(primary_key=True)

    class Meta:
        db_table = 'rechazadosp'


class Solicitud(models.Model):
    nomcoord = models.CharField(max_length=50)
    porasignar = models.BooleanField()
    porvalidard = models.BooleanField()
    porrevisarp = models.BooleanField()
    rechazadoc = models.BooleanField()
    validadoc = models.BooleanField()
    enviadod = models.BooleanField()
    devueltodace = models.BooleanField()
    fechaelab = models.DateField()
    tipo_solicitud = models.CharField(max_length=20)
    subtipo_solicitud = models.CharField(max_length=30)
    nivel = models.CharField(max_length=20)
    cod = models.CharField(max_length=7)
    cod_anterior = models.CharField(max_length=7, blank=True, null=True)
    denominacion = models.CharField(max_length=70)
    creditos = models.DecimalField(max_digits=2, decimal_places=0)
    tipo_aula = models.CharField(max_length=20)
    hteoria = models.BooleanField()
    hpractica = models.BooleanField()
    hlab = models.BooleanField()
    trime = models.CharField(max_length=8)
    ano = models.CharField(max_length=4)
    accion = models.CharField(max_length=20)
    afecta_carrera = models.CharField(max_length=35)
    trimestrep = models.BooleanField()
    requisito_cre = models.BooleanField()
    permiso_coord = models.BooleanField()
    tipo_materia = models.CharField(max_length=20)
    clase_materia = models.CharField(max_length=25)
    observaciones = models.CharField(max_length=500, blank=True, null=True)
    vigente = models.NullBooleanField()
    validadodace = models.BooleanField()
    especial = models.BooleanField()
    imparticion = models.CharField(max_length=15)
    usbidec = models.CharField(max_length=50, blank=True, null=True)
    obsanul = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'solicitud'


class TipoAula(models.Model):
    nombre = models.CharField(primary_key=True, max_length=50)

    class Meta:
        db_table = 'tipo_aula'


class TipoMateria(models.Model):
    nombre = models.CharField(primary_key=True, max_length=50)

    class Meta:
        db_table = 'tipo_materia'


class TrimestreVigencia(models.Model):
    mes_inicio = models.IntegerField()
    mes_fin = models.IntegerField()
    nombre = models.CharField(primary_key=True, max_length=50)

    class Meta:
        db_table = 'trimestre_vigencia'


class Usuario(models.Model):
    usbid = models.CharField(primary_key=True, max_length=50)
    clave = models.CharField(max_length=16)
    nombre = models.CharField(max_length=60)
    email = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)

    class Meta:
        db_table = 'usuario'
'''
