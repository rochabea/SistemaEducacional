from django.shortcuts import render
from .models import Users

def home(request):
    return render(request,'user/home.html')

def user(request):
    #salvar os dados da tela para o banco de dados
    novo_user = Users()
    novo_user.nome = request.POST.get('nome')
    novo_user.idade = request.POST.get('idade')
    novo_user.save()
    # exibir todos os usários já cadastrados em uma nova página
    user = {
        'user': Users.objects.all()
    }
    # retornar os dados para a página de listagem de usuários
    return render(request, 'user/user.html', user)
