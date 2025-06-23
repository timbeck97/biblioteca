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
    bloqueado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
    def save(self, *args, **kwargs):
        if self.nome:
            self.nome = self.formatar_nome_curso(self.nome)
        super().save(*args, **kwargs)

    def formatar_nome_curso(self, nome):
        partes = nome.lower().split()
        minusculas = ['da', 'de', 'do', 'das', 'dos', 'e',
                      'em', 'a', 'o', 'as', 'os', 'para', 'com']

        return ' '.join([
            p if p in minusculas else p.capitalize()
            for p in partes
        ])