from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Usuario  # Agora está dentro do app correto!

@login_required
def criar_usuario(request):
    if not request.user.tem_permissao(5):  # Apenas administradores
        return JsonResponse({"erro": "Acesso negado. Você não tem permissão para criar usuários."}, status=403)

    if request.method == "POST":
        email = request.POST.get("email")
        nome = request.POST.get("nome")
        idade = request.POST.get("idade")
        senha = request.POST.get("senha")
        permissao = request.POST.get("permissao")

        if Usuario.objects.filter(email=email).exists():
            return JsonResponse({"erro": "Este e-mail já está cadastrado!"}, status=400)

        novo_usuario = Usuario.objects.create_user(
            email=email, senha=senha, permissao=permissao,
            nome=nome, idade=idade
        )
        return JsonResponse({"mensagem": "Usuário criado com sucesso!"}, status=201)

    return render(request, "criar_usuario.html")

def home(request):
    return render(request, 'login_screen/login_screen.html')  # Ajuste para seu template real
