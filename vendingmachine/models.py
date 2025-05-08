from django.db import models

class Vending_machine(models.Model):
    machine_id = models.IntegerField(max_length=3, unique=True)

    vending_machine_type_choices = [
        ('Snacks', 'SNACKS'),
        ('Drinks','DRINKS'),
        ('Toys','TOYS'),
        ('Books','BOOKS'),
        ('Fashion','FASHION'),
        ('Misc','MISCELLANEOUS'),

    ]
    vending_machine_type = models.CharField(choices=vending_machine_type_choices)
    no_of_items = models.IntegerField(db_default=0)

    def items_availablity(self):
        if self.no_of_items < 1:
            return False

class machine_item(models.Model):
    vending_machine = models.ForeignKey(Vending_machine, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    item_cost = models.FloatField()
    item_quantity = models.IntegerField()

    def purchase(self):
        if self.item_quantity > 0:
            self.item_quantity -= 1
            return True
        else:
            return False
    
