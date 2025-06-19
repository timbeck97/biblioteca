from django.urls import path
from . import views

urlpatterns = [
    path('', views.livros, name='livros'),
    path('gerenciarLivros', views.gerenciar_livros, name='gerenciar_livros'),
    path('gerenciarLivros/ordenar/<ordem>', views.ordenar_livros, name='ordenar_livros'),
    path('cadastro', views.cadastrar_livro, name='cadastrar_livro'),
    path('editar/<int:id>', views.editar_livro, name='editar_livro'),
    path('deletar/<int:id>', views.deletar_livro, name='deletar_livro'),
    path('livro_detalhes/<int:id>', views.livro_detalhes, name='livro_detalhes'),
    path('reservas', views.gerenciar_reservas, name='gerenciar_reservas'),
    path('reservar', views.cadastrar_reserva, name='cadastrar_reserva'),

    path('emprestimos', views.gerenciar_emprestimos, name='gerenciar_emprestimos'),
    path('emprestimos/selecionar-livro', views.selecionar_livro_emprestimo, name='selecionar_livro_emprestimo'),
    path('emprestimos/<int:id>/selecionar-cliente', views.selecionar_cliente_emprestimo, name='selecionar_cliente_emprestimo'),
    path('emprestimos/realizar/<int:livro_id>/<int:cliente_id>', views.realizar_emprestimo, name='realizar_emprestimo'),
    path('emprestimos/deletar/<int:id>', views.deletar_emprestimo, name='deletar_emprestimo'),

    path('emprestimos/<int:id_emprestimo>/renovar', views.renovar, name='renovar'),
]
