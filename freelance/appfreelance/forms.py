from django import forms
from .models import CodigoPais, Usuario, Proyecto, Oferta, Mensaje

class CodigoPaisForm(forms.ModelForm):
    class Meta:
        model = CodigoPais
        fields = ['codigo_pais', 'descripcion']


class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    id_codigo = forms.ModelChoiceField(queryset=CodigoPais.objects.all(), empty_label="Seleccione el código de país")
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido_paterno', 'apellido_materno', 'rut', 'email', 'id_codigo', 'password']


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['usuario', 'titulo', 'descripcion', 'estado']

class OfertaForm(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = ['proyecto', 'freelancer', 'monto', 'descripción', 'estado']

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['remitente', 'destinatario', 'proyecto', 'contenido', 'leido']


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Nombre de Usuario o Correo Electronico",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'username', 'required': 'required'})
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password', 'required': 'required'})
    )