# Generated by Django 5.2.1 on 2025-05-24 12:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
        ("cats", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="agent",
            field=models.OneToOneField(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="cats.cat"
            ),
        ),
    ]
