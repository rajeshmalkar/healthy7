# Generated by Django 5.0.6 on 2024-06-01 07:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("healthapp", "0008_myorders_qty_order"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="pid",
        ),
        migrations.RemoveField(
            model_name="myorders",
            name="pid",
        ),
        migrations.RemoveField(
            model_name="myorders",
            name="uid",
        ),
        migrations.RemoveField(
            model_name="order",
            name="uid",
        ),
        migrations.DeleteModel(
            name="Meds",
        ),
        migrations.DeleteModel(
            name="MyOrders",
        ),
        migrations.DeleteModel(
            name="Order",
        ),
    ]
