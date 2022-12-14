from django import forms


class CursoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=50)
    comision = forms.IntegerField(label="Comisión")


class ProfeForm(forms.Form):
    nombre = forms.CharField(label="Nombre Profesor", max_length=50)
    apellido = forms.CharField(label="Apellido Profesor", max_length=50)
    email = forms.EmailField(label="Email Profesor")
    profesion = forms.CharField(label="Profesión", max_length=50)
