from django import forms
from .models import Livro

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['nome', 'autor', 'descricao', 'url']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'block w-full rounded-md border-gray-300 shadow-sm focus:ring focus:ring-indigo-200 focus:border-indigo-300 px-2 py-2',
                'placeholder': 'Título do livro'
            }),
            'autor': forms.TextInput(attrs={
                'class': 'block w-full rounded-md border-gray-300 shadow-sm focus:ring focus:ring-indigo-200 focus:border-indigo-300 px-2 py-2 ',
                'placeholder': 'Nome do autor'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'block w-full rounded-md border-gray-300 shadow-sm focus:ring focus:ring-indigo-200 focus:border-indigo-300 px-2 py-2',
                'placeholder': 'Descrição do livro',
                'rows': 4,
            }),
            'url': forms.URLInput(attrs={
                'class': 'block w-full rounded-md border-gray-300 shadow-sm focus:ring focus:ring-indigo-200 focus:border-indigo-300 px-2 py-2',
                'placeholder': 'URL da imagem do livro',
            }),
        }
