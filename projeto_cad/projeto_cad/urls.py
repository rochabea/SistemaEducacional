from django.urls import path
from app_cad import views

#estrutura: rota, view responsável, nome de referência
urlpatterns = [
    path('',views.home,name='home'),
    path('user/', views.user,name='listagem')
]
