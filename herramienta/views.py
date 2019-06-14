#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import  login, get_user_model, logout
from django.core import serializers
from django.http import Http404
from django.contrib.auth.decorators import  user_passes_test
from django.contrib.auth.models import Group, User

from herramienta import models
from models import Profesor
from django.urls import reverse
from .forms import HerramientasForm, PlanesForm, AnalisisForm






# Create your views here.
def index(request):
    if(request.user.is_authenticated):
        cursos=models.Profesor.objects.get(username=request.user.username).cursos.all()
        return render(request, 'cursos.html', {'cursos':cursos})
    else:
        outcomes = models.OutcomeAbet.objects.all().order_by('literal')
        return render(request, 'cursos.html', {'outcomes':outcomes })

#servicio rest para autenticar un usuario
@csrf_exempt
def login_rest(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(password)
        UserModel=get_user_model()
        try:
            usuario=UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            mensaje = 'Nombre de usuario no valido'
            raise Http404(mensaje)
        else:
            if usuario.check_password(password):
                login(request, usuario)
                return HttpResponse(serializers.serialize("json", [usuario]))
            else:
                mensaje = 'clave no valida'
                print(mensaje)
                raise Http404(mensaje)

#metodo encargado de renderizar la pantalla de login
def login_view(request):
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def cursos_prerequisito(request):
    cursos = models.Profesor.objects.get(username=request.user.username).cursos.all()
    return render(request, 'cursosPrerequisitos.html',{'cursos':cursos})

#servicio rest que retorna los prerequisitos de un curso
@csrf_exempt
def cursos_prerequisito_rest(request):
    curso = request.POST.get("curso")
    cursos = models.Profesor.objects.get(username=request.user.username).cursos.all().get(nombre=curso).prerequisitos.all()
    return HttpResponse(serializers.serialize("json", cursos))

#servicio rest que retorna las medidas de un outcome
@csrf_exempt
def medidas_outcome(request):
    outcome = request.POST.get("outcome")
    medidas = models.medidaOutcome.objects.filter(outcome__literal=outcome, tipo=0)
    return HttpResponse(serializers.serialize("json", medidas))


def cursos_outcome(request):
    cursos = models.Profesor.objects.get(username=request.user.username).cursos.all()
    outcomes = models.OutcomeAbet.objects.all().order_by('literal')
    return render(request, 'cursosOutcome.html',{'outcomes':outcomes,'cursos':cursos })

#servicio rest que retorna los cursos por outcome
@csrf_exempt
def cursos_outcome_rest(request):
    outcome = request.POST.get("outcome")
    cursos = models.Curso.objects.filter(medidas__outcome__literal=outcome).distinct()
    return HttpResponse(serializers.serialize("json", cursos))


def curso(request, id):
    curso=models.Curso.objects.get(id=id)
    outcomes= models.OutcomeAbet.objects.filter(medidas__curso__id=id).distinct().order_by('literal')
    herramientasform=HerramientasForm()
    planesform=PlanesForm()
    cursos = models.Profesor.objects.get(username=request.user.username).cursos.all()
    return render(request, 'curso.html',{'curso':curso,'cursos':cursos, 'outcomes':outcomes, 'herramientasform':herramientasform,'planesform':planesform})

#servicio rest que retorna las medidas de un outcome por curso
@csrf_exempt
def medidas_outcome_curso(request):
    outcome = request.POST.get("outcome")
    curso= request.POST.get("curso")
    medidas = models.medidaOutcome.objects.filter(outcome__literal=outcome, curso__nombre=curso)
    return HttpResponse(serializers.serialize("json", medidas))


def herramientas(request, id):
    if request.method=='POST':
        form = HerramientasForm(request.POST)

        if form.is_valid():
            herramientas= models.InstrumentoMedicion.objects.filter(medidaOutcome__curso__id= id,periodo=request.POST.get("periodo"))
            curso=models.Curso.objects.get(id=id)
            cursos = models.Profesor.objects.get(username=request.user.username).cursos.all()
            return render(request, 'herramientasDeMedicion.html',{'herramientas': herramientas,'cursos':cursos, 'curso':curso, 'periodo':request.POST.get("periodo")})


def planes_mejora(request, id):
    if request.method=='POST':
        form = PlanesForm(request.POST)
        if form.is_valid():
            planes= models.PlanesDeMejora.objects.filter(curso__id= id,periodo=request.POST.get("periodo"))
            curso = models.Curso.objects.get(id=id)
            cursos = models.Profesor.objects.get(username=request.user.username).cursos.all()
            return render(request, 'planesDeMejora.html',{'planes': planes,'cursos':cursos, 'curso':curso, 'periodo':request.POST.get("periodo")})


def herramienta(request, id):
    cursos = models.Profesor.objects.get(username=request.user.username).cursos.all()
    herramienta = models.InstrumentoMedicion.objects.get(id=id)
    return render(request, 'herramienta.html',{'cursos':cursos,'herramienta':herramienta})


def herramienta_analisis(request):
    cursos = models.Profesor.objects.get(username=request.user.username).cursos.all()
    outcomes = models.OutcomeAbet.objects.all().order_by('literal')
    periodos= models.InstrumentoMedicion.objects.all().values_list('periodo', flat=True).distinct().order_by('periodo').reverse()
    return render(request, 'herramientaAnalisis.html',{'outcomes':outcomes, 'periodos':periodos,'cursos':cursos})


def analisis_nuevo(request, id1, id2,outcome,periodo):
    cursos = models.Profesor.objects.get(username=request.user.username).cursos.all()
    curso1=models.Curso.objects.get(id=id1);
    curso2=models.Curso.objects.get(id=id2);
    instrumentoCurso1 = models.InstrumentoMedicion.objects.filter(medidaOutcome__curso__id=id1, medidaOutcome__outcome__literal=outcome, periodo=periodo)
    instrumentoCurso2 = models.InstrumentoMedicion.objects.filter(medidaOutcome__curso__id=id2, medidaOutcome__outcome__literal=outcome, periodo=periodo)
    instrumentos=map(None, instrumentoCurso1,instrumentoCurso2)
    outcome= models.OutcomeAbet.objects.get(literal=outcome)
    analisisForm = AnalisisForm()
    return render(request, 'analisisNuevo.html',{'cursos':cursos,'curso1':curso1, 'curso2':curso2, 'instrumentos':instrumentos,'periodo': periodo, 'outcome':outcome, 'analisisForm':analisisForm})


def agregar_analisis(request, id1, id2,outcome,periodo):
    if request.method=='POST':
        form = AnalisisForm(request.POST)
        if form.is_valid():
            outcomee=models.OutcomeAbet.objects.get(literal=outcome)
            models.AnalisisIntercurso.objects.create(calificacion=request.POST.get("calificacion"),
                                                     descripcion=request.POST.get("descripcion"),
                                                     periodo=periodo,
                                                     curso1_id=id1,
                                                     curso2_id=id2,
                                                     outcome_id=outcomee.id)
            return redirect('herramientaAnalisis')

@csrf_exempt
def analisis_cursos_rest(request):
    outcome = request.POST.get("outcome")
    periodo = request.POST.get("periodo")
    print(outcome,periodo)
    analisis = models.AnalisisIntercurso.objects.filter(outcome__literal=outcome,periodo=periodo)
    return HttpResponse(serializers.serialize("json", analisis))


def analisis_cambiar(request, id1, id2,outcome,periodo):
    cursos = models.Profesor.objects.get(username=request.user.username).cursos.all()
    curso1 = models.Curso.objects.get(id=id1);
    curso2 = models.Curso.objects.get(id=id2);
    instrumentoCurso1 = models.InstrumentoMedicion.objects.filter(medidaOutcome__curso__id=id1,
                                                                  medidaOutcome__outcome__literal=outcome,
                                                                  periodo=periodo)
    instrumentoCurso2 = models.InstrumentoMedicion.objects.filter(medidaOutcome__curso__id=id2,
                                                                  medidaOutcome__outcome__literal=outcome,
                                                                  periodo=periodo)
    instrumentos = map(None, instrumentoCurso1, instrumentoCurso2)
    analisis= models.AnalisisIntercurso.objects.get(outcome__literal=outcome, periodo=periodo, curso1__id=id1,curso2__id=id2)
    outcome = models.OutcomeAbet.objects.get(literal=outcome)
    analisisForm = AnalisisForm({'calificacion':analisis.calificacion,'descripcion':analisis.descripcion})
    return render(request, 'analisisCambiar.html',
                  {'cursos': cursos, 'curso1': curso1, 'curso2': curso2, 'instrumentos': instrumentos,
                   'periodo': periodo, 'outcome': outcome, 'analisisForm': analisisForm})


def cambiar_analisis(request, id1, id2,outcome,periodo):
    if request.method=='POST':
        form = AnalisisForm(request.POST)
        if form.is_valid():
            outcomee=models.OutcomeAbet.objects.get(literal=outcome)
            models.AnalisisIntercurso.objects.filter(periodo=periodo,
                                                  curso1_id=id1,
                                                  curso2_id=id2,
                                                  outcome_id=outcomee.id).update(calificacion=request.POST.get("calificacion"),
                                                                                 descripcion=request.POST.get("descripcion"))
            return redirect('herramientaAnalisis')