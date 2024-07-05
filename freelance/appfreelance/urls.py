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
    
    path('appfreelance/lista_servicios', views.lista_servicios, name='lista_servicios'),
    path('appfreelance/detalle_servicio', views.detalle_servicio, name='detalle_servicio'),
    path('appfreelance/editar_servicio', views.crear_servicio, name='crear_servicio'),
    path('appfreelance/edit_servicio', views.editar_servicio, name='editar_servicio'),
    path('<int:id>/eliminar/', views.eliminar_servicio, name='eliminar_servicio'),
]
