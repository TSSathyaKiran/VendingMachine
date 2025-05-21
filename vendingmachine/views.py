from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Vending_machine, machine_item
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            context = {'error': "Invalid Credentials!"}
            return render(request, 'vendingmachine/login.html', context)
    return render(request, "vendingmachine/login.html")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = User.objects.create_user(username=username, password=password)
        return redirect('login')
    return render(request, "vendingmachine/login.html")

def Home(request):
    list_of_machines = Vending_machine.objects.order_by("machine_id")
    context = {"list_of_machines" : list_of_machines}
    return render(request, "vendingmachine/home.html", context)

def Machine(request, id):
    machine = get_object_or_404(Vending_machine, machine_id = id)
    return render(request, 'vendingmachine/vm.html', {'machine' : machine})
