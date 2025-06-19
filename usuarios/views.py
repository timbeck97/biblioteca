from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente, Funcionario
from .forms import FuncionarioForm, ClienteForm


# Create your views here.
def index(request):
    return render(request, 'usuarios/index.html')

@login_required
def gerenciar_funcionarios(request):
    busca = request.GET.get('busca', '')  
    if busca:
        funcionarios = Funcionario.objects.filter(nome__icontains=busca)
    else:
        funcionarios = Funcionario.objects.all()
    return render(request, 'usuarios/gerenciar_funcionarios.html', {'funcionarios': funcionarios})
@login_required
def cadastrar_funcionario(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gerenciar_funcionarios')
    else:
        form = FuncionarioForm()
    return render(request, 'usuarios/cadastrar_funcionario.html', {'form': form})
@login_required
def editar_funcionario(request, id):
    funcionario = get_object_or_404(Funcionario, id=id)
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('gerenciar_funcionarios')
    else:
        form = FuncionarioForm(instance=funcionario)
    return render(request, 'usuarios/cadastrar_funcionario.html', {'form': form,})
@login_required
def deletar_funcionario(request, id):
    funcionario = get_object_or_404(Funcionario, id=id)
    funcionario.delete()
    return redirect('gerenciar_funcionarios')
   
@login_required
def gerenciar_clientes(request):
    busca = request.GET.get('busca', '')  
    if busca:
        clientes = Cliente.objects.filter(nome__icontains=busca)
    else:
        clientes = Cliente.objects.all()
    return render(request, 'usuarios/gerenciar_clientes.html', {'clientes': clientes})
@login_required
def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gerenciar_clientes')  # ou outra view
    else:
        form = ClienteForm()
    return render(request, 'usuarios/cadastrar_cliente.html', {'form': form})
@login_required
def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('gerenciar_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'usuarios/cadastrar_cliente.html', {'form': form})
@login_required
def deletar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    return redirect('gerenciar_clientes')
  