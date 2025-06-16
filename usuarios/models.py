from django.db import models

# Create your models here.
class Usuario(models.Model):
    
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=30)
    logradouro = models.CharField(max_length=20)
    bairro = models.CharField(max_length=30)


    def __str__(self):
        return self.nome