from django import forms
from herramienta import models

class HerramientasForm(forms.Form):
    periodosMedicion = models.InstrumentoMedicion.objects.all().values_list('periodo', flat=True).distinct().order_by('periodo')
    CHOICES=[]
    for i,p in enumerate(periodosMedicion):
        CHOICES.append((p,p))
    periodo = forms.ChoiceField(label='Escoge el periodo del que deseas ver las herramientas de medicion:',widget=forms.Select(attrs={'class' : 'form-control'}),choices=CHOICES)

class PlanesForm(forms.Form):
    periodosPlanes = models.PlanesDeMejora.objects.all().values_list('periodo', flat=True).distinct().order_by('periodo')
    CHOICES=[]
    for i,p in enumerate(periodosPlanes):
        CHOICES.append((p,p))
    periodo = forms.ChoiceField(label='Escoge el periodo del que deseas ver los planes de medicion:',widget=forms.Select(attrs={'class' : 'form-control'}),choices=CHOICES)