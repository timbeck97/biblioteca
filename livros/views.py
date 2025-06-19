from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.utils.dateparse import parse_date
from datetime import date
from .models import Livro, Emprestimo, Reserva
from usuarios.models import Cliente
from .forms import LivroForm, RenovarEmprestimoForm

ORDENACAO_LIVROS_LOOKUP = {
    'nome': 'nome',
    'autor': 'autor',
    'descricao': 'descricao',
    'ano_publicacao': 'ano_publicacao',
    'quantidade':'quantidade',
    'isbn':'isbn',
    'genero':'genero'
}

def index(request):
    return render(request, 'livros/index.html')

def livros(request):
    livros = Livro.objects.all()
    dados = {
        'livros':livros
    }
    return render(request, 'livros/lista_livros.html', dados)
def livro_detalhes(request, id):
    livro = get_object_or_404(Livro, id=id)
    return render(request, 'livros/detalhe_livro.html', {'livro': livro})

def gerenciar_livros(request):
    busca = request.GET.get('busca', '')
    livros = Livro.objects.all()
    if busca:
        livros = livros.filter(nome__icontains=busca)
    dados = {
        'livros': livros,
        'query': busca,
    }
    return render(request, 'livros/gerenciar_livros.html', dados)
def ordenar_livros(request, ordem):
    busca = request.GET.get('busca', '')
    direcao = request.GET.get('ordenacao', 'asc')

    livros = Livro.objects.all()
    if busca:
        livros = livros.filter(nome__icontains=busca)
    campo_ordenacao = ORDENACAO_LIVROS_LOOKUP.get(ordem)
    if direcao=='desc':
        campo_ordenacao = f'-{campo_ordenacao}'

    print(f'campo ordenadao: {campo_ordenacao}')
    livros = livros.order_by(campo_ordenacao)
    dados = {
        'livros': livros,
        'query': busca,
    }
    return render(request, 'livros/gerenciar_livros.html', dados)
def cadastrar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gerenciar_livros')  # ajuste para a sua URL de destino
    else:
        form = LivroForm()

    return render(request, 'livros/cadastrar_livro.html', {'form': form})
def editar_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('gerenciar_livros')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'livros/cadastrar_livro.html', {'form': form})

def deletar_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    livro.delete()
    return redirect('gerenciar_livros')

@login_required
def gerenciar_emprestimos(request):
    busca = request.GET.get('busca', '')
    if busca:
        emprestimos = Emprestimo.objects.filter(
            Q(cliente__nome__icontains=busca) | Q(livro__nome__icontains=busca)
        )
    else:
        emprestimos = Emprestimo.objects.all()
    return render(request, 'emprestimos/gerenciar_emprestimos.html', {'emprestimos': emprestimos})
@login_required
def selecionar_livro_emprestimo(request):
    busca = request.GET.get('busca','')
    livros = Livro.objects.all()
    if busca:
        livros = livros.filter(nome__icontains=busca)
    dados = {
        'livros':livros,
    }

    return render(request, 'emprestimos/selecionar_livro.html', dados)
@login_required
def selecionar_cliente_emprestimo(request, id):
    livro = get_object_or_404(Livro, id=id)
    if livro.exemplares_disponiveis()<=0:
        messages.error(request, 'Não existem exemplares disponíveis da obra selecionada.')
        return redirect('selecionar_livro_emprestimo')
    clientes = Cliente.objects.all()
    dados = {
        'livro': livro,
        'clientes': clientes
    }
    return render(request, 'emprestimos/selecionar_cliente.html', dados)

@login_required
def realizar_emprestimo(request, livro_id, cliente_id):
    livro = get_object_or_404(Livro, id=livro_id)
    cliente = get_object_or_404(Cliente, id=cliente_id)

    if request.method == 'POST':
        data_emprestimo = request.POST.get('data_emprestimo')
        data_devolucao = request.POST.get('data_devolucao')

        # Sua validação aqui
        erros = []
        if not data_emprestimo:
            erros.append('Data de empréstimo é obrigatória.')
        if not data_devolucao:
            erros.append('Data de devolução é obrigatória.')
        # Exemplo de validação simples de datas (string para comparar)
        if data_emprestimo and data_devolucao and data_devolucao <= data_emprestimo:
            erros.append('Data de devolução deve ser posterior à data de empréstimo.')

        if erros:
            for erro in erros:
                messages.error(request, erro)
            return render(request, 'emprestimos/finalizar_emprestimo.html', {
                'livro': livro,
                'cliente': cliente,
                'data_emprestimo': data_emprestimo,
                'data_devolucao': data_devolucao,
            })

        # Se passou nas validações, cria o empréstimo
        Emprestimo.objects.create(
            cliente=cliente,
            livro=livro,
            data_emprestimo=data_emprestimo,
            data_devolucao=data_devolucao,
            status='EM_ANDAMENTO'
        )
        return redirect('gerenciar_emprestimos')

    # GET inicial (sem valores)
    return render(request, 'emprestimos/finalizar_emprestimo.html', {
        'livro': livro,
        'cliente': cliente,
        'data_emprestimo': '',
        'data_devolucao': '',
    })

@login_required
def gerenciar_emprestimos(request):
    busca = request.GET.get('busca', '')
    if busca:
        emprestimos = Emprestimo.objects.filter(
            Q(cliente__nome__icontains=busca) | Q(livro__nome__icontains=busca)
        )
    else:
        emprestimos = Emprestimo.objects.all()
    return render(request, 'emprestimos/gerenciar_emprestimos.html', {'emprestimos': emprestimos})

@login_required
def deletar_emprestimo(request, id):
    emprestimo = get_object_or_404(Emprestimo, id=id)
    emprestimo.delete()
    return redirect('gerenciar_emprestimos')


@login_required
def renovar(request, id_emprestimo):
    emprestimo = get_object_or_404(Emprestimo, id=id_emprestimo)
    print(emprestimo.cliente, emprestimo.livro)
    existe_reserva = Reserva.objects.filter(livro=emprestimo.livro, status='AGUARDANDO').exists()
    print(f'reserva: {existe_reserva}')
    if existe_reserva and emprestimo.livro.exemplares_disponiveis()<=0:
        messages.error(request, 'Existe outro cliente na fila de espera para o empréstimo deste livro, não é possível realizar a renovação.')
        return redirect('gerenciar_emprestimos')
    if request.method == 'POST':
        form = RenovarEmprestimoForm(request.POST)
        if form.is_valid():
            nova_data = form.cleaned_data['nova_data_devolucao']
            data_atual = emprestimo.data_devolucao

            if nova_data <= data_atual:
                messages.error(request, 'A nova data de devolução deve ser posterior à data atual.')
            elif nova_data == data_atual:
                messages.warning(request, 'A nova data não pode ser igual à data atual.')
            else:
                emprestimo.data_devolucao = nova_data
                emprestimo.save()
                messages.success(request, 'Empréstimo renovado com sucesso.')
                return redirect('gerenciar_emprestimos')
            
    else:
        form = RenovarEmprestimoForm(initial={
            'nova_data_devolucao': emprestimo.data_devolucao
        })

    return render(request, 'emprestimos/confirmar_renovacao.html', {
        'cliente': emprestimo.cliente,
        'livro':emprestimo.livro,
        'form': form
    })
@login_required
def gerenciar_reservas(request):
    busca = request.GET.get('busca', '')
    if busca:
        reservas = Reserva.objects.filter(
            Q(cliente__nome__icontains=busca) | Q(livro__nome__icontains=busca)
        )
    else:
        reservas = Reserva.objects.all()
    return render(request, 'reservas/gerenciar_reservas.html', {'reservas': reservas})
@login_required
def cadastrar_reserva(request):
   return render(request, 'reservas/cadastrar_reserva.html')


