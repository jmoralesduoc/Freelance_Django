from django.shortcuts import render,redirect, get_object_or_404
from .forms import UsuarioForm,CodigoPaisForm,LoginForm,ProyectoForm,MensajeForm,OfertaForm
from .models import CodigoPais,Usuario,Proyecto,Mensaje,Oferta
from django.contrib.auth import login,logout
from .backends import UsuarioBackend
from django.urls import reverse
from .utils import nombre_usuario_global, tipo_usuario_global

# Create your views here.


def index(request):
    nombre_usuario = nombre_usuario_global 
    tipo_usuario = tipo_usuario_global 

    return render(request, 'appfreelance/index.html', {'nombre_usuario': nombre_usuario,'tipo_usuario': tipo_usuario})

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
    global tipo_usuario_global
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
                nombre_usuario_global = usuario.nombre + ' ' +  usuario.apellido_paterno
                tipo_usuario_global = usuario.tipo_usuario

                return redirect('index')
                
                
            else:
                error_message = 'Nombre de usuario o contraseña incorrectos'
    else:
        form = LoginForm()

    return render(request, 'appfreelance/login.html', {'form': form, 'error_message': error_message})
    


def get_nombre_usuario(request):
    global nombre_usuario_global
    
    return nombre_usuario_global 

def get_tipo_usuario(request):
    global tipo_usuario_global
    
    return tipo_usuario_global 



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

def proyecto_list(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'appfreelance/proyecto_list.html', {'proyectos': proyectos})

def proyecto_detail(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    return render(request, 'appfreelance/proyecto_detail.html', {'proyecto': proyecto})

def proyecto_create(request):
    if request.method == "POST":
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proyecto_list')
    else:
        form = ProyectoForm()
    return render(request, 'appfreelance/proyecto_form.html', {'form': form})

def proyecto_update(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    if request.method == "POST":
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect('proyecto_list')
    else:
        form = ProyectoForm(instance=proyecto)
    return render(request, 'appfreelance/proyecto_form.html', {'form': form})

def proyecto_delete(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    if request.method == "POST":
        proyecto.delete()
        return redirect('proyecto_list')
    return render(request, 'appfreelance/proyecto_confirm_delete.html', {'proyecto': proyecto})

def mensaje_list(request):
    mensajes = Mensaje.objects.all()
    return render(request, 'appfreelance/mensaje_list.html', {'mensajes': mensajes})

def mensaje_detail(request, pk):
    mensaje = get_object_or_404(Mensaje, pk=pk)
    return render(request, 'appfreelance/mensaje_detail.html', {'mensaje': mensaje})

def mensaje_create(request):
    if request.method == "POST":
        form = MensajeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mensaje_list')
    else:
        form = MensajeForm()
    return render(request, 'appfreelance/mensaje_form.html', {'form': form})

def mensaje_update(request, pk):
    mensaje = get_object_or_404(Mensaje, pk=pk)
    if request.method == "POST":
        form = MensajeForm(request.POST, instance=mensaje)
        if form.is_valid():
            form.save()
            return redirect('mensaje_list')
    else:
        form = MensajeForm(instance=mensaje)
    return render(request, 'appfreelance/mensaje_form.html', {'form': form})

def mensaje_delete(request, pk):
    mensaje = get_object_or_404(Mensaje, pk=pk)
    if request.method == "POST":
        mensaje.delete()
        return redirect('mensaje_list')
    return render(request, 'appfreelance/mensaje_confirm_delete.html', {'mensaje': mensaje})

def oferta_create(request):
    if request.method == 'POST':
        form = OfertaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('oferta_list')  # Ajusta esto según la URL de tu lista de ofertas
    else:
        form = OfertaForm()
    return render(request, 'appfreelance/oferta_create.html', {'form': form})

def oferta_list(request):
    ofertas = Oferta.objects.all()
    return render(request, 'appfreelance/oferta_list.html', {'ofertas': ofertas})

def oferta_detail(request, pk):
    oferta = get_object_or_404(Oferta, pk=pk)
    return render(request, 'appfreelance/oferta_detail.html', {'oferta': oferta})


def oferta_update(request, pk):
    oferta = get_object_or_404(Oferta, pk=pk)
    if request.method == "POST":
        form = OfertaForm(request.POST, instance=oferta)
        if form.is_valid():
            form.save()
            return redirect('oferta_list')
    else:
        form = OfertaForm(instance=oferta)
    return render(request, 'appfreelance/oferta_form.html', {'form': form})

def oferta_delete(request, pk):
    oferta = get_object_or_404(Oferta, pk=pk)
    if request.method == "POST":
        oferta.delete()
        return redirect('oferta_list')
    return render(request, 'appfreelance/oferta_confirm_delete.html', {'oferta': oferta})