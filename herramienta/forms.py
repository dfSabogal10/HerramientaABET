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

class AnalisisForm(forms.Form):
    CHOICES = [('bueno', 'bueno'),
               ('regular', 'regular'),
               ('malo', 'malo')]
    calificacion=forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    descripcion = forms.CharField(widget=forms.Textarea(attrs={"rows": 10, "cols": 20,'class' : 'form-control'}))
