# Generated by Django 5.0.4 on 2024-05-06 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0010_remove_jugadores_equipo"),
    ]

    operations = [
        migrations.AddField(
            model_name="jugadores",
            name="imagen",
            field=models.ImageField(
                blank=True, null=True, upload_to="uploads/jugadores/"
            ),
        ),
    ]
