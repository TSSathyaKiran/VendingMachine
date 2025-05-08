from django.core.exceptions import ValidationError
from django.db import models

class Vending_machine(models.Model):

    machine_name = models.CharField(max_length=30, null=False)
    machine_id = models.CharField(max_length=3, unique=True)

    def save(self, *args, **kwargs):
        self.machine_id = f'VM{(int(self.machine_id)):03}'
        super().save(*args, **kwargs)

    vending_machine_type_choices = [
        ('Snacks', 'SNACKS'),
        ('Drinks','DRINKS'),
        ('Toys','TOYS'),
        ('Books','BOOKS'),
        ('Fashion','FASHION'),
        ('Misc','MISCELLANEOUS'),

    ]
    vending_machine_type = models.CharField(choices=vending_machine_type_choices)
    no_of_items = models.PositiveIntegerField(db_default=0)
    items_to_be_added = no_of_items

    def items_availablity(self):
        if self.no_of_items == self.items_to_be_added:
            return False
        
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

    def purchase(self):
        if self.item_quantity > 0:
            self.item_quantity -= 1
            self.save()

            self.vending_machine.items_to_be_added += 1
            self.vending_machine.save()
            return True
        else:
            return False
    
