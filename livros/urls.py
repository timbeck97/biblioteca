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
  

    path('emprestimos', views.gerenciar_emprestimos, name='gerenciar_emprestimos'),
    path('emprestimos/selecionar-livro', views.selecionar_livro_emprestimo, name='selecionar_livro_emprestimo'),
    path('emprestimos/<int:id>/selecionar-cliente', views.selecionar_cliente_emprestimo, name='selecionar_cliente_emprestimo'),
    path('emprestimos/realizar/<int:livro_id>/<int:cliente_id>', views.realizar_emprestimo, name='realizar_emprestimo'),
    path('emprestimos/deletar/<int:id>', views.deletar_emprestimo, name='deletar_emprestimo'),
    path('emprestimos/<int:id_emprestimo>/editar', views.editar_emprestimo, name='editar_emprestimo'),
    path('emprestimos/<int:id_emprestimo>/renovar', views.renovar, name='renovar'),
    path('emprestimos/<int:id_emprestimo>/devolver', views.devolver_emprestimo, name='devolver_emprestimo'),

    path('reservas', views.gerenciar_reservas, name='gerenciar_reservas'),
    path('reservas/selecionar-livro', views.selecionar_livro_reserva, name='selecionar_livro_reserva'),
    path('reservas/<int:id>/selecionar-cliente', views.selecionar_cliente_reserva, name='selecionar_cliente_reserva'),
    path('reservas/realizar/<int:livro_id>/<int:cliente_id>', views.realizar_reserva, name='realizar_reserva'),
    path('reservas/deletar/<int:id>', views.deletar_reserva, name='deletar_reserva'),

    path('infracaoes', views.infracoes, name='infracoes'),
    path('infracao/<int:emprestimo_id>', views.registrar_infracao, name='registrar_infracao'),
    path('infracao/<int:id>/deletar', views.deletar_infracao, name='deletar_infracao'),
    path('relatorios/CLIENTE', views.relatorio_emprestimos_cliente, name='relatorio_emprestimos_cliente'),
    path('relatorios/LIVRO', views.relatorio_livros_mais_emprestados, name='relatorio_livros_mais_emprestados'),
]
