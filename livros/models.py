from django.db import models
from usuarios.models import Cliente
from datetime import datetime

GENEROS = [
        ('FICCAO', 'Ficção'),
        ('ROMANCE', 'Romance'),
        ('AVENTURA', 'Aventura'),
        ('FANTASIA', 'Fantasia'),
        ('BIOFRAFIA', 'Biografia'),
        ('AUTOAJUDA', 'Autoajuda'),
        ('TECNICO', 'Técnico'),
    ]
STATUS_EMPRESTIMO = [
    ('EM_ANDAMENTO', 'Em Andamento'),
    ('FINALIZADO', 'Finalizado'),
    ('EM_ATRASO', 'Em Atraso')
]
STATUS_RESERVA = [
    ('AGUARDANDO','Aguardando'),
    ('FINALIZADA','Finalizada')
]
class Livro(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    descricao = models.TextField()
    ano_publicacao = models.IntegerField(default=datetime.now().year)
    url = models.URLField(blank=True, null=True)
    isbn = models.CharField(max_length=17, blank=True, null=True, unique=True,
                            help_text="ISBN do livro (ex: 978-3-16-148410-0)")
    genero = models.CharField(max_length=20, choices=GENEROS, default='ficcao')
    quantidade = models.PositiveIntegerField(default=0)
    def exemplares_disponiveis(self):
        quantidade_emprestimos = self.emprestimo_set.count()
        disponiveis = self.quantidade - quantidade_emprestimos
        print('teste')
        return max(disponiveis, 0)
    def __str__(self):
        return self.nome
class Emprestimo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro,on_delete=models.CASCADE)
    data_emprestimo= models.DateField()
    data_devolucao = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_EMPRESTIMO, default='EM_ANDAMENTO')

    def __str__(self):
        return f'{self.cliente.nome} locou o livro {self.livro.titulo} no dia {self.data_emprestimo} e devolve no dia {self.data_devolucao} - Status - {self.status}'

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro,on_delete=models.CASCADE)
    data_solicitacao = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_RESERVA, default='AGUARDANDO')

    def __str__(self):
        return f'Cliente {self.cliente.nome} reservou o livro {self.livro.nome} no dia {self.data_solicitacao}'