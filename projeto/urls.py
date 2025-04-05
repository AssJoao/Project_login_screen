from django.contrib import admin
from django.urls import path, include
from contas.views import home  # importa a view home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # ← isso faz a raiz do site carregar a home
    path('contas/', include('contas.urls')),
]
