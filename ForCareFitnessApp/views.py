from django.shortcuts import render

def cadastro(request):
    return render(request, 'usuarios/cadastro.html')

def login(request):
    return render(request, 'usuarios/login.html')

def admin(request):
    return render(request, 'dashboards/admin.html')
