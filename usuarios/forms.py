from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente, Funcionario

class FuncionarioForm(UserCreationForm):
    class Meta:
        model = Funcionario
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cpf', 'nome', 'endereco', 'logradouro', 'bairro']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'