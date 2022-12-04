from django.db import models

# Create your models here.
# Char= string interger= numero
# Siempre se crean las clases hay que hacer python manage.py makemigrations python manage.py migrate y cada vez que se realiza un cambio python manage.py migrate


class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()


class Estudiante (models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()


class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)


class Entregable (models.Model):
    nombre = models.CharField(max_length=50)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()
