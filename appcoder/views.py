from django.shortcuts import render
from .models import Curso, Profesor, Estudiante, Avatar
from django.http import HttpResponse

from django.urls import reverse_lazy

from AppCoder.forms import CursoForm, ProfeForm, RegistroUsuarioForm, UserEditForm, AvatarForm

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def obtenerAvatar(request):
    lista = Avatar.objects.filter(user=request.user)
    if len(lista) != 0:
        avatar = lista[0].imagen.url
    else:
        avatar = "/media/avatars/avatarpordefecto.png"
    return avatar

# Create your views here.


@login_required
def curso(request):
    cursito = Curso(nombre="Python", comision=34234)
    cursito.save()
    cadena = f"curso guardado: nombre {cursito.nombre}, comisión: {cursito.comision}"
    return HttpResponse(cadena)


@login_required
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


@login_required
def cursos(request):
    return render(request, "appcoder/cursos.html")


@login_required
def estudiantes(request):
    return render(request, "appcoder/estudiantes.html")


@login_required
def profesores(request):
    return render(request, "appcoder/profesores.html")


@login_required
def entregables(request):
    return render(request, "appcoder/entregables.html")


@login_required
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


@login_required
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


@login_required
def profeFormulario(request):
    if request.method == "POST":
        form = ProfeForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            nombre = informacion["nombre"]
            apellido = informacion["apellido"]
            email = informacion["email"]
            profesion = informacion["profesion"]
            profesores = Profesor.objects.all()
            profe = Profesor(nombre=nombre, apellido=apellido,
                             email=email, profesion=profesion)
            profe.save()
            return render(request, "appcoder/inicio.html", {"mensaje": "Profesor guardado"})
        else:

            return render(request, "appcoder/profeFormulario.html", {"form": form, "mensaje": "Información no válida"})

    else:
        formulario = ProfeForm()
        return render(request, "appcoder/profeFormulario.html", {"form": formulario})


@login_required
def busquedaComision(request):
    return render(request, "appcoder/busquedaComision.html")


@login_required
def buscar(request):
    comision = request.GET["comision"]
    if comision != "":

        cursos = Curso.objects.filter(comision__icontains=comision)
        return render(request, "appcoder/resultadosBusqueda.html", {"cursos": cursos})
    else:
        return render(request, "appcoder/busquedaComision.html", {"mensaje": "Ingrese una comisión"})


@login_required
def leerProfesores(request):
    profesores = Profesor.objects.all()
    return render(request, "AppCoder/profesores.html", {"profesores": profesores})


@login_required
def eliminarProfesor(request, id):
    profesor = Profesor.objects.get(id=id)
    profesor.delete()
    profesores = Profesor.objects.all()
    return render(request, "AppCoder/profesores.html", {"profesores": profesores, "mensaje": "Eliminado con éxito"})


@login_required
def editarProfesor(request, id):
    profesor = Profesor.objects.get(id=id)
    if request.method == "POST":
        form = ProfeForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            profesor.nombre = info["nombre"]
            profesor.apellido = info["apellido"]
            profesor.email = info["email"]
            profesor.profesion = info["profesion"]
            profesor.save()
            profesores = Profesor.objects.all()
            return render(request, "AppCoder/Profesores.html", {"profesores": profesores, "mensaje": "Profesor editado correctamente"})
        pass
    else:
        formulario = ProfeForm(initial={"nombre": profesor.nombre, "apellido": profesor.apellido,
                               "email": profesor.email, "profesion": profesor.profesion})
        return render(request, "AppCoder/editarProfesor.html", {"form": formulario, "profesor": profesor})


# ....... VISTAS BASADAS EN CLASES

class EstudianteList(LoginRequiredMixin, ListView):  # vista usada para LISTAR
    model = Estudiante
    template_name = "AppCoder/estudiantes.html"


class EstudianteCreacion(LoginRequiredMixin, CreateView):  # vista usada para CREAR
    model = Estudiante
    success_url = reverse_lazy("estudiante_list")
    fields = ['nombre', 'apellido', 'email']


class EstudianteUpdate(LoginRequiredMixin, UpdateView):  # vista usada para EDITAR
    model = Estudiante
    success_url = reverse_lazy('estudiante_list')
    fields = ['nombre', 'apellido', 'email']


# vista usada para MOSTRAR DATOS
class EstudianteDetalle(LoginRequiredMixin, DetailView):
    model = Estudiante
    template_name = "Appcoder/estudiante_detalle.html"


class EstudianteDelete(LoginRequiredMixin, DeleteView):  # vista usada para ELIMINAR
    model = Estudiante
    success_url = reverse_lazy('estudiante_list')


# vista de registro

def register(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            return render(request, "AppCoder/inicio.html", {"mensaje": f"Usuario {username} creado correctamente"})
        else:
            return render(request, "AppCoder/register.html", {"form": form, "mensaje": "Error al crear el usuario"})
    else:
        form = RegistroUsuarioForm()
        return render(request, "AppCoder/register.html", {"form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usu = info["username"]
            clave = info["password"]
            # verifica si el usuario existe, si existe, lo devuelve, y si no devuelve None
            usuario = authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "AppCoder/inicio.html", {"mensaje": f"Usuario {usu} logueado correctamente"})
            else:
                return render(request, "AppCoder/login.html", {"form": form, "mensaje": "Usuario o contraseña incorrectos"})
        else:
            return render(request, "AppCoder/login.html", {"form": form, "mensaje": "Usuario o contraseña incorrectos"})
    else:
        form = AuthenticationForm()
        return render(request, "AppCoder/login.html", {"form": form})


@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usuario.email = info["email"]
            usuario.password1 = info["password1"]
            usuario.password2 = info["password2"]
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]
            usuario.save()
            return render(request, "AppCoder/inicio.html", {"mensaje": f"Usuario {usuario.username} editado correctamente"})
        else:
            return render(request, "AppCoder/editarPerfil.html", {"form": form, "nombreusuario": usuario.username})
    else:
        form = UserEditForm(instance=usuario)
        return render(request, "AppCoder/editarPerfil.html", {"form": form, "nombreusuario": usuario.username})


def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar = Avatar(user=request.user, imagen=request.FILES["imagen"])
            avatarViejo = Avatar.objects.filter(user=request.user)
            if len(avatarViejo) > 0:
                avatarViejo[0].delete()
            avatar.save()
            return render(request, "AppCoder/inicio.html", {"mensaje": f"Avatar agregado correctamente"})
        else:
            return render(request, "AppCoder/agregarAvatar.html", {"form": form, "usuario": request.user, "mensaje": "Error al agregar el avatar"})
    else:
        form = AvatarForm()
        return render(request, "AppCoder/agregarAvatar.html", {"form": form, "usuario": request.user})
