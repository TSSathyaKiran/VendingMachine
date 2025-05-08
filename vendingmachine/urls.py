from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home),
    path('<id>', views.Machine)
]