from django.core.exceptions import ValidationError
from django.db import models

class Vending_machine(models.Model):

    machine_id = models.IntegerField(unique=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.items_to_be_added = self.no_of_items
        super().save(*args, **kwargs)

    @property
    def machine_name(self):
        return f'VM{self.machine_id:03}'

    vending_machine_type_choices = [
        ('Snacks', 'SNACKS'),
        ('Drinks','DRINKS'),
        ('Toys','TOYS'),
        ('Books','BOOKS'),
        ('Fashion','FASHION'),
        ('Misc','MISCELLANEOUS'),

    ]
    vending_machine_type = models.CharField(choices=vending_machine_type_choices)
    no_of_items = models.PositiveIntegerField(default=0)
    items_to_be_added = models.PositiveBigIntegerField(default=0)

    def items_availablity(self):
        if self.no_of_items == self.items_to_be_added:
            return False
        else: return True
        
    def __str__(self):
        return self.machine_name

class machine_item(models.Model):
    vending_machine = models.ForeignKey(Vending_machine, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    item_cost = models.FloatField()
    item_quantity = models.PositiveBigIntegerField()

    def save(self, *args, **kwargs):
        if self.vending_machine.items_to_be_added < self.item_quantity:
            raise ValidationError({'item_quantity' : 'Item quantity exceeds machine limit!'})
        else:
            self.vending_machine.items_to_be_added -= self.item_quantity
            self.vending_machine.save()
        super().save(*args, **kwargs)

    def purchase(self):
        if self.item_quantity > 0:
            self.item_quantity -= 1
            self.save()

            self.vending_machine.items_to_be_added += 1
            self.vending_machine.save()
            return True
        else:
            return False
    
