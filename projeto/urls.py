from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Painel de administração do Django
    path('contas/', include('contas.urls')),  # Rota para o app 'contas'
]
