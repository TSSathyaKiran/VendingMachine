from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('<int:id>', views.Machine, name='Machine'),
    path('login/', views.user_login, name='login'),
    path('register', views.register, name='register'),
    
]