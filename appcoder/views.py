from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.template import loader

from appcoder.forms import *

# Create your views here.


def curso(request):
    cursito = Curso(nombre="Python", comision=34234)
    cursito.save()
    cadena = f"curso guardado: nombre {cursito.nombre}, comisión: {cursito.comision}"
    return HttpResponse(cadena)


def familiar(request):

    hermano = Familiar(nombre="Pablo", apellido="Blanco",
                       edad=32, fecha="1990-09-23")
    hermana = Familiar(nombre="Belén", apellido="Blanco",
                       edad=33, fecha="1989-09-19")
    mama = Familiar(nombre="Eleonora", apellido="Carelle",
                    edad=57, fecha="1965-03-09")
    hermano.save()
    hermana.save()
    mama.save()
    cadena = f"familiares: nombre {hermano.nombre}, apellido: {hermano.apellido}, edad: {hermano.edad}, fecha: {hermano.fecha}, nombre {hermana.nombre}, apellido: {hermana.apellido}, edad: {hermana.edad}, fecha: {hermana.fecha}, nombre {mama.nombre}, apellido: {mama.apellido}, edad: {mama.edad}, fecha: {mama.fecha}"
    return HttpResponse(cadena)


def cursos(request):
    return render(request, "appcoder/cursos.html")


def estudiantes(request):
    return render(request, "appcoder/estudiantes.html")


def profesores(request):
    return render(request, "appcoder/profesores.html")


def entregables(request):
    return render(request, "appcoder/entregables.html")


def inicio(request):
    return render(request, "appcoder/inicio.html")


"""
def cursoFormulario(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        comision = request.POST["comision"]
        curso = Curso(nombre=nombre, comision=comision)
        curso.save()
        return render(request, "appcoder/inicio.html", {"mensaje": "Curso guardado satisfatoriamente"})
    else:
        return render(request, "appcoder/cursoFormulario.html")
"""


def cursoFormulario(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data  # Convierte el html en un diccionario
            nombre = informacion["nombre"]
            comision = informacion["comision"]
            curso = Curso(nombre=nombre, comision=comision)
            curso.save()
            return render(request, "appcoder/inicio.html", {"mensaje": "Curso guardado"})
        else:
            return render(request, "appcoder/inicio.html", {"form": form, "mensaje": "Error"})
    else:
        formulario = CursoForm()
        return render(request, "appcoder/cursoFormulario.html", {"form": formulario})


def profeFormulario(request):
    if request.method == "POST":
        form = ProfeForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            nombre = informacion["nombre"]
            apellido = informacion["apellido"]
            email = informacion["email"]
            profesion = informacion["profesion"]
            profe = Profesor(nombre=nombre, apellido=apellido,
                             email=email, profesion=profesion)
            profe.save()
            return render(request, "appcoder/inicio.html", {"mensaje": "Profesor guardado"})
        else:
            return render(request, "appcoder/profeFormulario.html", {"form": form, "mensaje": "Información no válida"})
    else:
        formulario = ProfeForm()
        return render(request, "appcoder/profeFormulario.html", {"form": formulario})


def busquedaComision(request):
    return render(request, "appcoder/busquedaComision.html")


def buscar(request):
    comision = request.GET["comision"]
    if comision != "":

        cursos = Curso.objects.filter(comision__icontains=comision)
        return render(request, "appcoder/resultadosBusqueda.html", {"cursos": cursos})
    else:
        return render(request, "appcoder/busquedaComision.html", {"mensaje": "Ingrese una comisión"})
