# appfreelance/backends.py
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import Usuario

class UsuarioBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = Usuario.objects.get(email=username)
        except Usuario.DoesNotExist:
            try:
                user = Usuario.objects.get(rut=username)
            except Usuario.DoesNotExist:
                return None

        if check_password(password, user.password) and user.is_active:
            return user
        return None

    def get_user(self, user_id):
        try:
            return Usuario.objects.get(pk=user_id)
        except Usuario.DoesNotExist:
            return None
