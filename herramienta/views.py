# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
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






# Create your views here.
def index(request):
    if(request.user.is_authenticated):
        cursos=models.Profesor.objects.get(username=request.user.username).cursos.all()
        for curso in cursos:
            print(curso.profesor_set.all())
        return render(request, 'cursos.html', {'cursos':cursos})
    else:
        outcomes = models.OutcomeAbet.objects.all()
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
    print(cursos)
    return HttpResponse(serializers.serialize("json", cursos))

#servicio rest que retorna las medidas de un outcome
@csrf_exempt
def medidas_outcome(request):
    outcome = request.POST.get("outcome")
    medidas = models.medidaOutcome.objects.filter(outcome__literal=outcome)
    return HttpResponse(serializers.serialize("json", medidas))


def cursos_outcome(request):
    cursos = models.Profesor.objects.get(username=request.user.username).cursos.all()
    outcomes = models.OutcomeAbet.objects.all()
    return render(request, 'cursosOutcome.html',{'outcomes':outcomes,'cursos':cursos })

#servicio rest que retorna los cursos por outcome
@csrf_exempt
def cursos_outcome_rest(request):
    outcome = request.POST.get("outcome")
    cursos = models.Profesor.objects.get(username=request.user.username).cursos.all().filter(outcomes__literal=outcome)
    print(outcome, cursos)
    return HttpResponse(serializers.serialize("json", cursos))


def curso(request, id):
    curso=models.Curso.objects.get(id=id)
    cursos = models.Profesor.objects.get(username=request.user.username).cursos.all()
    periodos = models.medidaOutcome.objects.all().values_list('periodo', flat=True).distinct()
    return render(request, 'curso.html',{'curso':curso,'cursos':cursos,'periodos':periodos})

#servicio rest que retorna las medidas de un outcome por curso
@csrf_exempt
def medidas_outcome_curso(request):
    outcome = request.POST.get("outcome")
    curso= request.POST.get("curso")
    medidas = models.medidaOutcome.objects.filter(outcome__literal=outcome, curso__nombre=curso)
    return HttpResponse(serializers.serialize("json", medidas))