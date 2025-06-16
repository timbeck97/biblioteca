from django.urls import path
from . import views

urlpatterns = [
    path('', views.livros, name='livros'),
    path('gerenciarLivros', views.gerenciar_livros, name='gerenciar_livros'),
    path('gerenciarLivros/ordenar/<ordem>', views.ordenar_livros, name='ordenar_livros'),
    path('cadastro', views.cadastrar_livro, name='cadastrar_livro'),
    path('editar/<int:id>', views.editar_livro, name='editar_livro'),
    path('deletar/<int:id>', views.deletar_livro, name='deletar_livro'),
    path('reservar/<int:id>', views.reservar, name='reservar'),
]
