from django.db import models
from django.contrib.auth.hashers import make_password


class CodigoPais(models.Model):
    id_codigo = models.AutoField(db_column="idCodigo", primary_key=True)
    codigo_pais = models.CharField(max_length=8)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.descripcion} ({self.codigo_pais})"



class Usuario(models.Model):
    TIPOS_USUARIO = [
        ('admin', 'Administrador'),
        ('cliente', 'Cliente'),
    ]
    id = models.AutoField(db_column='idUsuario', primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    rut = models.CharField(blank=False, null=False, max_length=12)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    id_codigo = models.ForeignKey('CodigoPais', on_delete=models.CASCADE, db_column='idCodigo')
    password = models.CharField(max_length=20)
    last_login = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    tipo_usuario = models.CharField(max_length=10, choices=TIPOS_USUARIO)

    USERNAME_FIELD = 'email'  # O puedes usar 'rut'
    REQUIRED_FIELDS = ['nombre', 'apellido_paterno', 'apellido_materno', 'rut', 'id_codigo']

    def save(self, *args, **kwargs):
        if not self.pk or self.password != Usuario.objects.get(pk=self.pk).password:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno}"

class Proyecto(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, db_column='idUsuario')
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo

class Oferta(models.Model):
    proyecto = models.ForeignKey('Proyecto', on_delete=models.CASCADE, related_name='ofertas')
    freelancer = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='ofertas_realizadas',db_column='idUsuario')
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    descripción = models.TextField()
    fecha_oferta = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, choices=[('aceptada', 'Aceptada'), ('rechazada', 'Rechazada'), ('pendiente', 'Pendiente')])
    
class Mensaje(models.Model):
    remitente = models.ForeignKey('Usuario', related_name='mensajes_enviados', on_delete=models.CASCADE, db_column='idUsuarioRemitente')
    destinatario = models.ForeignKey('Usuario', related_name='mensajes_recibidos', on_delete=models.CASCADE, db_column='idUsuarioDestinatario')
    proyecto = models.ForeignKey(Proyecto, null=True, blank=True, on_delete=models.CASCADE, db_column='idProyecto')
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    def __str__(self):
        return self.contenido[:20]
