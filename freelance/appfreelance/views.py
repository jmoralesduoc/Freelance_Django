from django.shortcuts import render

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