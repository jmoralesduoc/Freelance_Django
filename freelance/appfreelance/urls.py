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
]
