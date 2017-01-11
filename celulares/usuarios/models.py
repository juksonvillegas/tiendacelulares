from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.
class ManagerUsuarios(BaseUserManager):
	def _create_user(self, usuario, email, password, is_staff,
	 is_superuser, **extra_fields):
		if not email:
			raise ValueError("El email es obligatorio")
		email = self.normalize_email(email)
		user = self.model(usuario = usuario, email = email, is_active = True,
			is_staff = is_staff, is_superuser = is_superuser, **extra_fields)
		user.set_password(password)
		user.save(using = self._db)
		return user

	def create_user(self, usuario, email, password = None, **extra_fields):
		return self._create_user(usuario, email, password, False, False, **extra_fields)

	def create_superuser(self, usuario, email, password = None, **extra_fields):
		return self._create_user(usuario, email, password, True, True, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
	usuario = models.CharField(max_length = 50, unique = True) #ok
	email = models.EmailField(max_length = 50, unique = True) #ok
	nombre = models.CharField(max_length = 200) #ok
	direccion = models.CharField(max_length = 250, default = "su casa")
	telefono = models.CharField(max_length = 9, default = "968072613") #ok
	foto = models.URLField() #ok

	is_active = models.BooleanField(default = True)
	is_staff = models.BooleanField(default = False)
	is_mayorista = models.BooleanField(default = False)

	objects = ManagerUsuarios()

	USERNAME_FIELD = 'usuario'
	REQUIRED_FIELDS = ['email']

	def get_short_name(self):
		return self.nombre

	class Meta:
		verbose_name = 'user'
		verbose_name_plural = 'users'
