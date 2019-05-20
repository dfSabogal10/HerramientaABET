# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# modelo de usuario generico que sera utilizado en la aplicacion.
class Profesor(User):
    cursos=models.ManyToManyField('Curso')
    def __str__(self):
        return self.username
    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'

    def __unicode__(self):

        return '%s'%self.username

    def __str__(self):
        return '%s' % self.username

# Create your models here.
#modelo de un curso
class Curso (models.Model):
    nombre = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    outcomes= models.ManyToManyField('OutcomeAbet')
    prerequisitos= models.ManyToManyField('Curso',blank=True)

    def __unicode__(self):

        return '%s'%self.nombre

    def __str__(self):
        return '%s' % self.nombre

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

class OutcomeAbet (models.Model):
    literal= models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'Outcome Abet'
        verbose_name_plural = 'Outcomes Abet'

    def __unicode__(self):

        return '%s'%self.literal

    def __str__(self):
        return '%s' % self.literal

class medidaOutcome(models.Model):
    tipo = models.BooleanField()
    periodo = models.CharField(max_length=100)
    valor=models.DecimalField(decimal_places=2,max_digits=3)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    outcome = models.ForeignKey(OutcomeAbet, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Medida Outcome'
        verbose_name_plural = 'Medidas Outcomes'

class InstrumentoMedicion (models.Model):
    tipo=models.BooleanField()
    descripcion = models.CharField(max_length=100)
    valor= models.DecimalField(decimal_places=2,max_digits=3)
    periodo = models.CharField(max_length=100)
    medidaOutcome= models.ForeignKey(medidaOutcome, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Instrumento de medicion'
        verbose_name_plural = 'Instrumentos de medicion'


class PlanesDeMejora (models.Model):
    descripcion=models.CharField(max_length=100)
    periodo=models.CharField(max_length=100)
    curso=models.ForeignKey(Curso,on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Plan de mejora'
        verbose_name_plural = 'Planes de mejora'

