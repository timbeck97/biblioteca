from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes', views.gerenciar_clientes, name='gerenciar_clientes'),
    path('funcionarios', views.gerenciar_funcionarios, name='gerenciar_funcionarios'),
    path('funcionarios/cadastrar', views.cadastrar_funcionario, name='cadastrar_funcionario'),
    path('funcionarios/editar<int:id>', views.editar_funcionario, name='editar_funcionario'),
    path('funcionarios/deletar/<int:id>', views.deletar_funcionario, name='deletar_funcionario'),
    path('clientes/cadastrar', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('clientes/editar/<int:id>', views.editar_cliente, name='editar_cliente'),
    path('clientes/deletar/<int:id>', views.deletar_cliente, name='deletar_cliente'),
    path('clientes/bloquear/<int:id>', views.bloquear_cliente, name='bloquear_cliente'),
    path('clientes/desbloquear/<int:id>', views.desbloquear_cliente, name='desbloquear_cliente')
  
]
