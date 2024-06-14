#from django.conf.url import url

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login, name='login'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('login_ingreso/', views.login_ingreso, name='login_ingreso'),
    path('olvidocontraseña/', views.olvidocontraseña, name='olvidocontraseña'),
     path('ingreso/', views.ingreso, name='ingreso'),
    
    
]