# Generated by Django 5.0.4 on 2024-04-23 13:32

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0002_alter_product_price"),
    ]

    operations = [
        migrations.CreateModel(
            name="Categoria",
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
                ("nombre", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Cliente",
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
                ("nombre", models.CharField(max_length=50)),
                ("apellido", models.CharField(max_length=50)),
                ("telefono", models.CharField(max_length=10)),
                ("email", models.EmailField(max_length=100)),
                ("contraseña", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Equipo",
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
                ("nombre", models.CharField(max_length=100)),
                (
                    "logo",
                    models.ImageField(
                        blank=True, null=True, upload_to="uploads/equipo/"
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="product",
            name="category",
        ),
        migrations.RemoveField(
            model_name="order",
            name="customer",
        ),
        migrations.RemoveField(
            model_name="order",
            name="product",
        ),
        migrations.CreateModel(
            name="Producto",
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
                ("nombre", models.CharField(max_length=100)),
                (
                    "precio",
                    models.DecimalField(decimal_places=2, default=0, max_digits=9),
                ),
                (
                    "descripcion",
                    models.CharField(blank=True, default="", max_length=250, null=True),
                ),
                ("imagen", models.ImageField(upload_to="uploads/product/")),
                (
                    "categoria",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="store.categoria",
                    ),
                ),
                (
                    "equipo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.equipo"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Orden",
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
                ("cantidad", models.IntegerField(default=1)),
                ("direccion", models.CharField(blank=True, default="", max_length=100)),
                ("telefono", models.CharField(blank=True, default="", max_length=20)),
                ("fecha", models.DateField(default=datetime.datetime.today)),
                ("estado", models.BooleanField(default=False)),
                (
                    "cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.cliente"
                    ),
                ),
                (
                    "producto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.producto"
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Category",
        ),
        migrations.DeleteModel(
            name="Customer",
        ),
        migrations.DeleteModel(
            name="Order",
        ),
        migrations.DeleteModel(
            name="Product",
        ),
    ]