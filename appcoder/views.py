from django.shortcuts import render
from .models import Curso, Familiar
from django.http import HttpResponse
from django.template import loader

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
