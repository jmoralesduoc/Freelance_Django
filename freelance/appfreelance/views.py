from django.shortcuts import render, get_object_or_404, redirect
from .models import Servicio
from .forms import ServicioForm 

# Create your views here.


def index(request):
    context={}
    return render(request, 'appfreelance/index.html',context)

def registro(request):
    context={}
    return render(request,'appfreelance/registro.html',context)

def login(request):
    context={}
    return render(request,'appfreelance/login.html',context)

def nosotros(request):
    context={}
    return render(request,'appfreelance/nosotros.html',context)

def login_ingreso(request):
    context={}
    return render(request,'appfreelance/login_ingreso.html',context)

def ingreso(request):
    context={}
    return render(request,'appfreelance/ingreso.html',context)

def olvidocontraseña(request):
    context={}
    return render(request,'appfreelance/olvidocontraseña.html',context)


def lista_servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'appfreelance/lista_servicios.html', {'servicios': servicios})

def detalle_servicio(request, id):
    servicio = get_object_or_404(Servicio, id=id)
    return render(request, 'appfreelance/detalle_servicio.html', {'servicio': servicio})

def crear_servicio(request):
    if request.method == "POST":
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_servicios')
    else:
        form = ServicioForm()
    return render(request, 'appfreelance/edit_servicio.html', {'form': form})

def editar_servicio(request, id):
    servicio = get_object_or_404(Servicio, id=id)
    if request.method == "POST":
        form = ServicioForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            return redirect('lista_servicios')
    else:
        form = ServicioForm(instance=servicio)
    return render(request, 'appfreelance/edit_servicio.html', {'form': form})

def eliminar_servicio(request, id):
    servicio = get_object_or_404(Servicio, id=id)
    servicio.delete()
    return redirect('lista_servicios')
