# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import User


# modelo de usuario generico que sera utilizado en la aplicacion.
class Profesor(User):
    cursos=models.ManyToManyField('Curso')

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
    prerequisitos= models.ManyToManyField('Curso',blank=True)

    def __unicode__(self):

        return '%s' % self.nombre

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

        return '%s %s' % ("outcome ",self.literal)

    def __str__(self):
        return '%s %s' % ("outcome ",self.literal)

TIPO_CHOICES = (
    (1, "Media"),
    (0, "Mediana"),
)
class medidaOutcome(models.Model):
    tipo = models.BooleanField(choices=TIPO_CHOICES, default=1)
    periodo = models.CharField(max_length=100)
    valor=models.DecimalField(decimal_places=2,max_digits=3)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='medidas')
    outcome = models.ForeignKey(OutcomeAbet, on_delete=models.CASCADE, related_name='medidas')
    class Meta:
        verbose_name = 'Medida Outcome'
        verbose_name_plural = 'Medidas Outcomes'

    def __unicode__(self):

        return '%s %s %s' % (self.curso, self.outcome, self.periodo)

    def __str__(self):
        return '%s %s %s' % (self.curso, self.outcome, self.periodo)
    def clean(self):
        if self.valor < 0 or self.valor>5:
            raise ValidationError(_('El valor tiene que estar entre 0 y 5'))


class InstrumentoMedicion (models.Model):
    tipo=models.BooleanField(choices=TIPO_CHOICES, default=1)
    descripcion = models.CharField(max_length=100)
    valor= models.DecimalField(decimal_places=2,max_digits=3)
    periodo = models.CharField(max_length=100)
    medidaOutcome= models.ForeignKey(medidaOutcome, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Instrumento de medicion'
        verbose_name_plural = 'Instrumentos de medicion'

    def __unicode__(self):
        if self.tipo == 0:
            return '%s %s' % (self.medidaOutcome, "mediana")
        else:
            return '%s %s' % (self.medidaOutcome, "media")

    def __str__(self):
        if self.tipo == 0:
            return '%s %s' % (self.medidaOutcome, "mediana")
        else:
            return '%s %s' % (self.medidaOutcome, "media")

    def clean(self):
        if self.periodo !=  self.medidaOutcome.periodo:
            raise ValidationError(_('El periodo del instrumento de medicion no corresponde con el periodo de la medida del outcome'))
        if self.valor < 0 or self.valor>5:
            raise ValidationError(_('El valor tiene que estar entre 0 y 5'))



class PlanesDeMejora (models.Model):
    descripcion=models.CharField(max_length=100)
    periodo=models.CharField(max_length=100)
    curso=models.ForeignKey(Curso,on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Plan de mejora'
        verbose_name_plural = 'Planes de mejora'

    def __unicode__(self):

        return '%s %s' % (self.curso, "- " +self.periodo)

    def __str__(self):
        return '%s %s' % (self.curso, "- " +self.periodo)

