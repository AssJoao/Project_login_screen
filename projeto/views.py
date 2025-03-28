from django.shortcuts import render
from django.http import HttpResponse

def teste_view(request):

    return HttpResponse("Essa é a rota de teste")

def login_screen(request):
    return render(request,'login_screen/login_screen.html')