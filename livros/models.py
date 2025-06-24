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
CHOICE_OCORRENCIA = [
    ('PERDIDO', 'Perdido'),
    ('DANIFICADO', 'Danificado')
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
        emprestimos_ativos = self.emprestimo_set.exclude(status='FINALIZADO').count()
        return max(self.quantidade - emprestimos_ativos, 0)
    def esta_disponivel_para_cliente(self, cliente):
        if self.exemplares_disponiveis() <= 0:
            return False
        primeira_reserva = self.reserva_set.filter(status='AGUARDANDO').order_by('data_solicitacao').first()
        if not primeira_reserva:
            return True
        return primeira_reserva.cliente == cliente
    def esta_reservado_para_outro(self, cliente):
        reserva = self.reserva_set.filter(status='AGUARDANDO').order_by('data_solicitacao').first()
        return reserva and reserva.cliente != cliente
    def esta_reservado_para_alguem(self):
        return self.reserva_set.filter(status='AGUARDANDO').exists()
    def proxima_reserva(self):
        return self.reserva_set.filter(status='AGUARDANDO').order_by('data_solicitacao').first()
    def exemplares_nao_reservados(self):
        reservas_ativas = self.reserva_set.filter(status='AGUARDANDO').count()
        return max(self.exemplares_disponiveis() - reservas_ativas, 0)
    def pode_ser_reservado(self):
        return self.exemplares_nao_reservados() <= 0
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
class Emprestimo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro,on_delete=models.CASCADE)
    data_emprestimo= models.DateField()
    data_devolucao = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_EMPRESTIMO, default='EM_ANDAMENTO')

    def __str__(self):
        return f'{self.cliente.nome} locou o livro {self.livro.nome} no dia {self.data_emprestimo} e devolve no dia {self.data_devolucao} - Status - {self.status}'

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro,on_delete=models.CASCADE)
    data_solicitacao = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_RESERVA, default='AGUARDANDO')

    def __str__(self):
        return f'Cliente {self.cliente.nome} reservou o livro {self.livro.nome} no dia {self.data_solicitacao}'
class Infracao(models.Model):
    emprestimo = models.ForeignKey(Emprestimo, on_delete=models.CASCADE)
    ocorrencia = models.CharField(max_length=20, choices=CHOICE_OCORRENCIA)
    bloquear_cliente = models.BooleanField(default=True)
    data_infracao = models.DateField(auto_now_add=True)