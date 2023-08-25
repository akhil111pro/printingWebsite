# Generated by Django 4.1.4 on 2023-01-09 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bannaoapp", "0009_alter_orders_orderedby"),
    ]

    operations = [
        migrations.CreateModel(
            name="order_update",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("orderedBy", models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name="orders",
            name="orderedBy",
            field=models.TextField(max_length=50),
        ),
    ]
