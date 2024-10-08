# Generated by Django 5.0.7 on 2024-08-27 04:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("perfil", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="project",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
