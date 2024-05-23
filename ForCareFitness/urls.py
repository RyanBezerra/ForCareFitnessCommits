from django.urls import path
from ForCareFitnessApp import views

urlpatterns = [
    path('', views.cadastro, name="cadastro"),
    path('login/', views.login, name="login"),
    path('admin/', views.admin, name="admin"),
]
