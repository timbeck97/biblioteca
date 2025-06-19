from django.contrib.auth.models import AbstractUser
from django.db import models


class Funcionario(AbstractUser):
    ativado = models.BooleanField(default=True)
    def __str__(self):
        return self.username
class Cliente(models.Model):
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField()
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=30)
    logradouro = models.CharField(max_length=20)
    bairro = models.CharField(max_length=30)


    def __str__(self):
        return self.nome