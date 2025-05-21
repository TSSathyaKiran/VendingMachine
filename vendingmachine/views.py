from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Vending_machine, machine_item
from django.contrib.auth import authenticate, login, logout

def user_login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username = username, password = password)
    if user is not None:
        login(request, user)
        render()

        
def Home(request):
    list_of_machines = Vending_machine.objects.order_by("machine_id")
    context = {"list_of_machines" : list_of_machines}
    return render(request, "vendingmachine/home.html", context)

def Machine(request, id):
    machine = get_object_or_404(Vending_machine, machine_id = id)
    return render(request, 'vendingmachine/vm.html', {'machine' : machine})
