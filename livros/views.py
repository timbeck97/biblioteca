from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro
from .forms import LivroForm
# Create your views here.
ORDENACAO_LIVROS_LOOKUP = {
    'nome': 'nome',
    'autor': 'autor',
    'descricao': 'descricao',
    'data_publicacao': 'data_publicacao',
}

def index(request):
    return render(request, 'livros/index.html')

def livros(request):
    livros = Livro.objects.all()
    dados = {
        'livros':livros
    }
    return render(request, 'livros/lista_livros.html', dados)

def reservar(request, id):
    print(id)
    return render(request, 'livros/reservar_livro.html')


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

    livros = Livro.objects.all()
    if busca:
        livros = livros.filter(nome__icontains=busca)
    campo_ordenacao = ORDENACAO_LIVROS_LOOKUP.get(ordem)
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
