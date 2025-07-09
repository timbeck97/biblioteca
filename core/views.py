from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.forms.models import model_to_dict

def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.ativado is False:
                messages.error(request, "Funcionário desativado")
                return render(request, 'registration/login.html') 
            login(request, user)
            return redirect('home')  
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    
    return render(request, 'registration/login.html') 

def logout_view(request):
    logout(request)
    return redirect('login') 