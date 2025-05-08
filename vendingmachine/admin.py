from django.contrib import admin

# Register your models here.
from .models import Vending_machine, machine_item

class items_admin(admin.TabularInline):
    model = machine_item
    extra = 2

class Vending_machine_Admin(admin.ModelAdmin):
    pass

admin.site.register(Vending_machine)