from django.contrib import admin
from .models import Livro, Emprestimo, Reserva, Infracao

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'autor', 'ano_publicacao', 'genero', 'quantidade', 'isbn')
    search_fields = ('nome', 'autor', 'isbn')
    list_filter = ('genero', 'ano_publicacao')
    ordering = ('nome',)

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'livro', 'data_emprestimo', 'data_devolucao', 'status')
    search_fields = ('cliente__nome', 'livro__nome')
    list_filter = ('status', 'data_emprestimo')
    ordering = ('-data_emprestimo',)

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'livro', 'data_solicitacao', 'status')
    search_fields = ('cliente__nome', 'livro__nome')
    list_filter = ('status', 'data_solicitacao')
    ordering = ('-data_solicitacao',)
@admin.register(Infracao)
class InfracaoAdmin(admin.ModelAdmin):
    list_display = ('emprestimo', 'ocorrencia', 'bloquear_cliente')

