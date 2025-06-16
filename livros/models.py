from django.db import models
from usuarios.models import Usuario
# Create your models here.

class Livro(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    descricao = models.TextField()
    data_publicacao = models.DateField(auto_now_add=True)
    url = models.URLField(blank=True, null=True)
    def __str__(self):
        return self.nome
class Reserva(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro,on_delete=models.CASCADE)
    data_reserva = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario.nome} reservou {self.livro.titulo} no dia {self.data_reserva}'