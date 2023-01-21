from django import forms


class CursoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=50)
    comision = forms.IntegerField(label="Comisión")


class ProfeForm(forms.Form):
    nombre = forms.CharField(label="Nombre Profesor", max_length=50)
    apellido = forms.CharField(label="Apellido Profesor", max_length=50)
    email = forms.EmailField(label="Email Profesor")
    profesion = forms.CharField(label="Profesión", max_length=50)


class RegistroUsuarioForm(UserCreationForm):

    email = forms.EmailField(label="Email Profesor")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        # para cada uno de los campos del formulario, le asigna un valor vacio
        help_texts = {k: "" for k in fields}


class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Email Usuario")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirmar Contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label='Modificar Nombre')
    last_name = forms.CharField(label='Modificar Apellido')

    class Meta:
        model = User
        fields = ["email", "password1", "password2", "first_name", "last_name"]
        # para cada uno de los campos del formulario, le asigna un valor vacio
        help_texts = {k: "" for k in fields}


class AvatarForm(forms.Form):
    imagen = forms.ImageField(label="Imagen")
