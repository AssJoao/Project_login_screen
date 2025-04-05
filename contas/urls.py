from django.urls import path
from . import views  # Importa as funções do views.py

urlpatterns = [
    path('', views.home, name='home'),  # Define a rota principal do app
]
