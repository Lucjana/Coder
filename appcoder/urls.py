from django.urls import path
from .views import *


urlpatterns = [
    path("cursos/", cursos, name="cursos"),
    path("profesores/", profesores, name="profesores"),
    path("entregables/", entregables, name="entregables"),
    path("estudiantes/", estudiantes, name="estudiantes"),
    # se pone "" sin nada porque será el inicio de la página, automáticamente irá a este
    path("", inicio, name="inicio"),

    path("cursoFormulario/", cursoFormulario, name="cursoFormulario"),
    path("profeFormulario/", profeFormulario, name="profeFormulario"),
    path("busquedaComision/", busquedaComision, name="busquedaComision"),
    path("buscar/", buscar, name="buscar"),

]
