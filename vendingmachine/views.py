from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Vending_machine, machine_item

def Home(request):
    list_of_machines = Vending_machine.objects.order_by("machine_id")
    context = {"list_of_machines" : list_of_machines}
    return render(request, "vendingmachine/home.html", context)

def Machine(request, id):
    machine = get_object_or_404(Vending_machine, machine_id = id)
    return render(request, 'vendingmachine/vm.html', {'machine' : machine})