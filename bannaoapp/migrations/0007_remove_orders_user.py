# Generated by Django 4.1.4 on 2023-01-08 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bannaoapp", "0006_remove_orders_orderedby_orders_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="orders",
            name="user",
        ),
    ]
