from django.db import models

class Clientes(models.Model):
    nome_CLIENTE = models.CharField(max_length=250)
    CPF_CNPJ_CLIENTE = models.CharField(max_length=50)
    endereco_1_CLIENTE = models.CharField(max_length=250)
    endereco_2_CLIENTE = models.CharField(max_length=250, blank=True, null=True)
    contato_telefone_comercial_CLIENTE = models.CharField(max_length=10)
    contato_telefone_residencial_CLIENTE = models.CharField(max_length=10, blank=True, null=True)
    contato_email_CLIENTE = models.CharField(max_length=20, blank=True, null=True)
    descricao_CLIENTE = models.CharField(max_length=500, blank=True, null=True)

class Produtos(models.Model):
    id_PRODUTO = models.CharField(max_length=1000)
    nome_PRODUTO = models.CharField(max_length=1000)
    descricao_PRODUTO = models.CharField(max_length=1000, blank=True, null=True)
    codigo_PRODUTO = models.CharField(max_length=1000, blank=True, null=True)
    quantidade_PRODUTO = models.IntegerField

class Usuario(models.Model):
    clientes = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    produtos = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    email_USUARIO = models.CharField(max_length=100)
    senha_USUARIO = models.CharField(max_length=100)
    nome_USUARIO = models.CharField(max_length=100)

# Create your models here.
