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

    path("profesores", profesores, name="profesores"),
    path("eliminarProfesor/<id>", eliminarProfesor, name="eliminarProfesor"),
    path("editarProfesor/<id>", editarProfesor, name="editarProfesor"),

    path("estudiante/list/", EstudianteList.as_view(), name="estudiante_list"),
    path('estudiante/nuevo/', EstudianteCreacion.as_view(), name='estudiante_crear'),
    path('estudiante/<pk>', EstudianteDetalle.as_view(), name='estudiante_detalle'),
    path('estudiante/borrar/<pk>', EstudianteDelete.as_view(),
         name='estudiante_borrar'),
    path('estudiante/editar/<pk>', EstudianteUpdate.as_view(),
         name='estudiante_editar'),

    path("register/", register, name="register"),
    path("login/", login_request, name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('editarPerfil/', editarPerfil, name='editarPerfil'),
    path('agregarAvatar/', agregarAvatar, name='agregarAvatar'),

]
