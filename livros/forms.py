from django import forms
from .models import Livro
from datetime import date

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['nome', 'autor', 'descricao', 'ano_publicacao', 'url', 'isbn', 'genero', 'quantidade']
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
            'ano_publicacao': forms.NumberInput(attrs={
                'class': 'block w-full rounded-md border-gray-300 shadow-sm focus:ring focus:ring-indigo-200 focus:border-indigo-300 px-2 py-2',
                'placeholder': 'Ano de publicação',
                'min': '0'
            }),
            'url': forms.URLInput(attrs={
                'class': 'block w-full rounded-md border-gray-300 shadow-sm focus:ring focus:ring-indigo-200 focus:border-indigo-300 px-2 py-2',
                'placeholder': 'URL da imagem do livro',
            }),
            'isbn': forms.TextInput(attrs={
                'class': 'block w-full rounded-md border-gray-300 shadow-sm focus:ring focus:ring-indigo-200 focus:border-indigo-300 px-2 py-2',
                'placeholder': 'ISBN do livro',
            }),
            'quantidade': forms.NumberInput(attrs={
                'class': 'block w-full rounded-md border-gray-300 shadow-sm focus:ring focus:ring-indigo-200 focus:border-indigo-300 px-2 py-2',
                'min': '0',
                'placeholder': 'Quantidade em estoque',
            }),
            # 'genero' usa select padrão
        }
class RenovarEmprestimoForm(forms.Form):
    nova_data_devolucao = forms.DateField(
        label='Nova data de devolução',
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control'
            },
            format='%Y-%m-%d'
        ),
        input_formats=['%Y-%m-%d']
    )
class InfracaoForm(forms.Form):
    ocorrencia = forms.ChoiceField(
        choices=[
            ('', 'Selecione uma opção'),
            ('PERDIDO', 'Livro perdido'),
            ('DANIFICADO', 'Livro danificado')
        ],
        required=True,
        error_messages={'required': 'Por favor, selecione uma ocorrência.'},
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    bloquear_cliente = forms.BooleanField(
        initial=True,
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )