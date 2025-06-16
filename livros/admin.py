from django.contrib import admin
from .models import Livro, Reserva

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'autor', 'data_publicacao') 
    search_fields = ('nome', 'autor')                  
    list_filter = ('data_publicacao',)                  
    ordering = ('-data_publicacao',)                     

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'livro', 'data_reserva')
    search_fields = ('usuario__nome', 'livro__nome')  
    list_filter = ('data_reserva',)
    ordering = ('-data_reserva',)