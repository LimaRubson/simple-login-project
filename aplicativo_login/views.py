# meu_aplicativo/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, SignInForm
from django.shortcuts import redirect
from django.contrib.auth import get_user_model


def default_redirect(request):
    return redirect('signup')  # ou 'signin' dependendo da sua lógica

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Salva o usuário
            login(request, user)  # Faz o login do usuário
            return redirect('home')  # Redireciona para a página inicial após o cadastro
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        print("user", request.POST.get('username'))
        print("password", request.POST.get('password'))
        User = get_user_model()
        user_exists = User.objects.filter(username=request.POST.get('username')).exists()
        print("USERS:", user_exists)
        if user_exists:
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redireciona para a página inicial após o login
        else:
            print("ERRO", form.is_valid())
    else:
        form = SignInForm()
    return render(request, 'signin.html', {'form': form})
