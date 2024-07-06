from django.shortcuts import render,redirect, get_object_or_404
from .forms import UsuarioForm,CodigoPaisForm,LoginForm
from .models import CodigoPais,Usuario
from django.contrib.auth import login,logout
from .backends import UsuarioBackend
from django.urls import reverse
from .utils import nombre_usuario_global

# Create your views here.


def index(request):
    nombre_usuario = nombre_usuario_global 

    return render(request, 'appfreelance/index.html', {'nombre_usuario': nombre_usuario})

def registro(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro_exitoso')
    else:
        form = UsuarioForm()
    return render(request, 'appfreelance/registro.html', {'form': form})
    
    


def login_view(request):
    error_message = None
    global nombre_usuario_global
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            backend = UsuarioBackend()
            user = backend.authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user, backend='appfreelance.backends.UsuarioBackend')
                usuario = Usuario.objects.get(email=username)  
                nombre_usuario_global = usuario.nombre

                return redirect('index')
                
                
            else:
                error_message = 'Nombre de usuario o contraseña incorrectos'
    else:
        form = LoginForm()

    return render(request, 'appfreelance/login.html', {'form': form, 'error_message': error_message})
    


def get_nombre_usuario(request):
    global nombre_usuario_global
    return nombre_usuario_global 


def logout_view(request):
    global nombre_usuario_global
    nombre_usuario_global = None
    nombre_usuario = None 

    return render(request, 'appfreelance/index.html', {'nombre_usuario': nombre_usuario})
     


def nosotros(request):
    context={}
    return render(request,'appfreelance/nosotros.html',context)

def login_ingreso(request):
    context={}
    return render(request,'appfreelance/Login_ingreso.html',context)

def ingreso(request):
    context={}
    return render(request,'appfreelance/ingreso.html',context)

def olvidocontraseña(request):
    context={}
    return render(request,'appfreelance/olvidocontraseña.html',context)



def codigo_pais_list(request):
    codigos = CodigoPais.objects.all()
    context={}
    return render(request, 'appfreelance/codigo_pais_list.html', {'codigos': codigos})

def codigo_pais_create(request):
    if request.method == 'POST':
        form = CodigoPaisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('codigo_pais_list')
    else:
        form = CodigoPaisForm()
    return render(request, 'appfreelance/codigo_pais_form.html', {'form': form})

def codigo_pais_update(request, id):
    codigo = get_object_or_404(CodigoPais, id_codigo=id)
    if request.method == 'POST':
        form = CodigoPaisForm(request.POST, instance=codigo)
        if form.is_valid():
            form.save()
            return redirect('codigo_pais_list')
    else:
        form = CodigoPaisForm(instance=codigo)
    return render(request, 'appfreelance/codigo_pais_form.html', {'form': form})

def codigo_pais_delete(request, id):
    codigo = get_object_or_404(CodigoPais, id_codigo=id)
    if request.method == 'POST':
        codigo.delete()
        return redirect('codigo_pais_list')
    return render(request, 'appfreelance/codigo_pais_confirm_delete.html', {'codigo': codigo})



