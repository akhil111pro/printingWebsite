# Generated by Django 4.1.4 on 2023-01-15 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bannaoapp", "0011_delete_order_update_remove_orders_filename"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orders",
            name="orderedBy",
            field=models.CharField(editable=False, max_length=50),
        ),
    ]
