from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse

# Create your views here.


def curso(request):
    cursito = Curso(nombre="Python", comision=34234)
    cursito.save()
    cadena = f"curso guardado: nombre {cursito.nombre}, comisión: {cursito.comision}"
    return HttpResponse(cadena)
