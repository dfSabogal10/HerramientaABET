# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django import forms

# Register your models here.
from .models import Curso, OutcomeAbet, PlanesDeMejora, InstrumentoMedicion, medidaOutcome, Profesor
admin.site.register(Curso)
admin.site.register(OutcomeAbet)
admin.site.register(InstrumentoMedicion)
admin.site.register(PlanesDeMejora)
admin.site.register(Profesor)

#
# class MedidaOutcomeForm(forms.ModelForm):
#
#     class Meta:
#         model = medidaOutcome
#         fields = ['tipo','periodo','valor','curso','outcome']
#
#     def __init__(self, *args, **kwargs):
#         super(MedidaOutcomeForm, self).__init__(*args, **kwargs)
#         if self.instance:
#             print self.instance
#             fields=Curso.objects.get(id=self.instance.curso.id).outcomes.all()
#             self.fields['outcome'].queryset = fields
#
#
# class MedidaOutcomeAdmin(admin.ModelAdmin):
#     """
#     Admin Class for 'MedidaOutcome'.
#     """
#     # fieldsets = [
#     #     ('Tipo',      {'fields': ['tipo']}),
#     #     ('Periodo',         {'fields': ['periodo']}),
#     #     ('Valor',        {'fields': ['valor']}),
#     #     ('Curso',        {'fields': ['curso']}),
#     #     ('Outcome', {'fields': ['outcome']}),
#     #
#     # ]
#     form = MedidaOutcomeForm
#
# admin.site.register(medidaOutcome, MedidaOutcomeAdmin)
admin.site.register(medidaOutcome)