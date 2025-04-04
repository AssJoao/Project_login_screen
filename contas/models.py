from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UsuarioManager(BaseUserManager):
    def create_user(self, email, senha=None, permissao=1, **extra_fields):
        if not email:
            raise ValueError("O usuário precisa de um email")
        email = self.normalize_email(email)
        usuario = self.model(email=email, permissao=permissao, **extra_fields)
        usuario.set_password(senha)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, email, senha, **extra_fields):
        extra_fields.setdefault("permissao", 5)
        usuario = self.create_user(email, senha, **extra_fields)
        usuario.is_staff = True
        usuario.is_superuser = True
        usuario.save(using=self._db)
        return usuario

class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=100)
    idade = models.IntegerField(null=True, blank=True)
    permissao = models.IntegerField(default=1)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nome"]

    def __str__(self):
        return f"{self.nome} ({self.email}) - Permissão: {self.permissao}"

    def tem_permissao(self, nivel):
        return self.permissao >= nivel
