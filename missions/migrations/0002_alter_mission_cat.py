# Generated by Django 5.2.1 on 2025-05-24 15:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cats", "0001_initial"),
        ("missions", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mission",
            name="cat",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="missions",
                to="cats.cat",
            ),
        ),
    ]
