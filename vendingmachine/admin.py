from django.contrib import admin

# Register your models here.
from .models import Vending_machine, machine_item

class items_admin(admin.TabularInline):
    model = machine_item
    extra = 4

class Vending_machine_Admin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields" : ['machine_id', 'vending_machine_type', 'no_of_items']})
    ]

    inlines = [items_admin]

    list_display = ['machine_name', 'machine_id', 'vending_machine_type', 'no_of_items', 'items_to_be_added']

admin.site.register(Vending_machine, Vending_machine_Admin)