from django.shortcuts import render, redirect
from django.contrib import auth

def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        context = {}
        if request.method == "POST":
            erros = {}

            nome = request.POST.get('nome', None)
            password = request.POST.get('senha', None)

            usuario = auth.authenticate(
                request,
                username=nome,
                password=password
            )

            if usuario:
                auth.login(request, usuario)
                return redirect('index')
            else:
                erros['css'] = "d-block"
                erros['login'] = "Credenciais não encontradas"
            
            if erros:
                context['erros'] = erros

        return render(request, './login.html', context=context)

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        return render(request, './index.html')