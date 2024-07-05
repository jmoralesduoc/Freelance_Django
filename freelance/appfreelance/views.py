from django.shortcuts import render,redirect, get_object_or_404
from .forms import UsuarioForm,CodigoPaisForm
from .models import CodigoPais

# Create your views here.


def index(request):
    context={}
    return render(request, 'appfreelance/index.html',context)

def registro(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro_exitoso')
    else:
        form = UsuarioForm()
    return render(request, 'registro.html', {'form': form})
    
    

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