from django.db import models

# Create your models here.
class vending_machine(models.Model):
    vending_machine_type = models.CharField(max_length=100)
    no_of_items = models.IntegerField(db_default=0)

class machine_item(models.Model):
    item_name = models.ForeignKey(vending_machine, on_delete=models.CASCADE)
    item_cost = models.FloatField()


