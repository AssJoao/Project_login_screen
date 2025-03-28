from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('teste/', views.teste_view, name="teste"), 
    path('login/', views.login_screen,name="login"),
]
