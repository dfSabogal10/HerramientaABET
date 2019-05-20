# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Curso, OutcomeAbet, PlanesDeMejora, InstrumentoMedicion, Profesor, medidaOutcome

admin.site.register(Curso)
admin.site.register(OutcomeAbet)
admin.site.register(InstrumentoMedicion)
admin.site.register(PlanesDeMejora)
admin.site.register(Profesor)
admin.site.register(medidaOutcome)