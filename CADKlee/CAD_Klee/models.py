from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UsuarioAdmin(BaseUserManager):

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("USUARIOS DEVEM TER UM E-MAIL")
        if not username:
            raise ValueError("USUARIOS DEVEM TER UM NOME DE USUARIO")
        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser):
    # clientes                                = models.ForeignKey(Clientes, on_delete=models.CASCADE, blank=True, null=True)
    # produtos                                = models.ForeignKey(Produtos, on_delete=models.CASCADE, blank=True, null=True)
    email                                   = models.EmailField(verbose_name="email", max_length=100, unique=True)
    username                                = models.CharField(max_length=100)
    date_joined                             = models.DateTimeField(verbose_name="Data de entrada", auto_now_add=True)
    last_login                              = models.DateTimeField(verbose_name="Último login", auto_now=True)
    is_admin                                = models.BooleanField(default=False)
    is_active                               = models.BooleanField(default=True)
    is_staff                                = models.BooleanField(default=False)
    is_superuser                            = models.BooleanField(default=False)

    objects = UsuarioAdmin()

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return  self.is_admin

    def has_module_perms(self, app_label):
        return True


class Clientes(models.Model):
    user                                    = models.ForeignKey(Usuario, on_delete=models.PROTECT) # clientes.user
    nome_CLIENTE                            = models.TextField()
    CPF_CNPJ_CLIENTE                        = models.TextField()
    endereco_1_CLIENTE                      = models.TextField()
    endereco_2_CLIENTE                      = models.TextField(blank=True, null=True)
    contato_telefone_comercial_CLIENTE      = models.TextField()
    contato_telefone_residencial_CLIENTE    = models.TextField(blank=True, null=True)
    contato_email_CLIENTE                   = models.TextField(blank=True, null=True)
    descricao_CLIENTE                       = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome_CLIENTE

class Produtos(models.Model):
    user                                    = models.ForeignKey(Usuario, on_delete=models.PROTECT) #  produtos.user
    id_PRODUTO                              = models.TextField()
    nome_PRODUTO                            = models.TextField()
    descricao_PRODUTO                       = models.TextField(blank=True, null=True)
    codigo_PRODUTO                          = models.TextField(blank=True, null=True)
    quantidade_PRODUTO                      = models.IntegerField

    def __str__(self):
        return self.nome_PRODUTO

# class Usuario(models.Model):
#     clientes = models.ForeignKey(Clientes, on_delete=models.CASCADE)
#     produtos = models.ForeignKey(Produtos, on_delete=models.CASCADE)
#     email_USUARIO = models.CharField(max_length=100)
#     senha_USUARIO = models.CharField(max_length=100)
#     nome_USUARIO = models.CharField(max_length=100)

# Create your models here.
