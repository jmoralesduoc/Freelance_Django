from django.urls import path
from django.views.generic import TemplateView
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.index, name='index'),
    path('registro/', views.registro, name='registro'),
    path('registro/exitoso/', TemplateView.as_view(template_name='appfreelance/registro_exitoso.html'), name='registro_exitoso'),
    path('login/', views.login_view, name='login'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('login_ingreso/', views.login_ingreso, name='login_ingreso'),
    path('olvidocontraseña/', views.olvidocontraseña, name='olvidocontraseña'),
    path('ingreso/', views.ingreso, name='ingreso'),
    path('logout/', views.logout_view, name='logout'),
    path('codigo_pais/', views.codigo_pais_list, name='codigo_pais_list'),
    path('codigo_pais/new/', views.codigo_pais_create, name='codigo_pais_create'),
    path('codigo_pais/edit/<int:id>/', views.codigo_pais_update, name='codigo_pais_update'),
    path('codigo_pais/delete/<int:id>/', views.codigo_pais_delete, name='codigo_pais_delete'),
    path('proyectos/', views.proyecto_list, name='proyecto_list'),
    path('proyectos/<int:pk>/', views.proyecto_detail, name='proyecto_detail'),
    path('proyectos/crear/', views.proyecto_create, name='proyecto_create'),
    path('proyectos/<int:pk>/editar/', views.proyecto_update, name='proyecto_update'),
    path('proyectos/<int:pk>/eliminar/', views.proyecto_delete, name='proyecto_delete'),
    path('mensajes/', views.mensaje_list, name='mensaje_list'),
    path('mensajes/<int:pk>/', views.mensaje_detail, name='mensaje_detail'),
    path('mensajes/crear/', views.mensaje_create, name='mensaje_create'),
    path('mensajes/<int:pk>/editar/', views.mensaje_update, name='mensaje_update'),
    path('mensajes/<int:pk>/eliminar/', views.mensaje_delete, name='mensaje_delete'),
    path('oferta/create/', views.oferta_create, name='oferta_create'),
    path('oferta/', views.oferta_list, name='oferta_list'),
    path('oferta/<int:pk>/', views.oferta_detail, name='oferta_detail'),
    path('oferta/<int:pk>/editar/', views.oferta_update, name='oferta_update'),
    path('oferta/<int:pk>/eliminar/', views.oferta_delete, name='oferta_delete'),

]


