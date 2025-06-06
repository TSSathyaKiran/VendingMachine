# Generated by Django 5.2 on 2025-05-08 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendingmachine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vending_machine',
            name='machine_name',
            field=models.CharField(default='Unnamed', max_length=30),
        ),
        migrations.AlterField(
            model_name='vending_machine',
            name='machine_id',
            field=models.CharField(max_length=3, unique=True),
        ),
        migrations.AlterField(
            model_name='vending_machine',
            name='vending_machine_type',
            field=models.CharField(choices=[('Snacks', 'SNACKS'), ('Drinks', 'DRINKS'), ('Toys', 'TOYS'), ('Books', 'BOOKS'), ('Fashion', 'FASHION'), ('Misc', 'MISCELLANEOUS')]),
        ),
    ]
