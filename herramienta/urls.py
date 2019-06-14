from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login_rest, name='login'),
    url(r'^loginview$', views.login_view, name='loginview'),
    url(r'^logout$', views.logout_view, name='logout'),
    url(r'^cursosprerequisito$', views.cursos_prerequisito, name='cursosprerequisito'),
    url(r'^cursosprerequisitorest$', views.cursos_prerequisito_rest, name='cursosprerequisitorest'),
    url(r'^cursosoutcome$', views.cursos_outcome, name='cursosoutcome'),
    url(r'^cursosoutcomerest$', views.cursos_outcome_rest, name='cursosoutcomerest'),
    url(r'^medidasoutcome$', views.medidas_outcome, name='medidasoutcome'),
    url(r'^medidasoutcomeCurso$', views.medidas_outcome_curso, name='medidasoutcomeCurso'),
    url(r'^analisisCursosrest', views.analisis_cursos_rest, name='analisisCursosrest'),
    url(r'^curso/(?P<id>\d+)$', views.curso, name='curso'),
    url(r'^herramientas/(?P<id>\d+)$', views.herramientas, name='herramientas'),
    url(r'^planesMejora/(?P<id>\d+)$', views.planes_mejora, name='planesMejora'),
    url(r'^instrumento/(?P<id>\d+)$', views.herramienta, name='herramienta'),
    url(r'^herramientaAnalisis$', views.herramienta_analisis, name='herramientaAnalisis'),
    url(r'^analisisNuevo/(?P<id1>\d+)/(?P<id2>\d+)/(?P<outcome>.+)/(?P<periodo>.+)$', views.analisis_nuevo, name='analisisNuevo'),
    url(r'^agregarAnalisis/(?P<id1>\d+)/(?P<id2>\d+)/(?P<outcome>.+)/(?P<periodo>.+)$', views.agregar_analisis, name='agregarAnalisis')


]
