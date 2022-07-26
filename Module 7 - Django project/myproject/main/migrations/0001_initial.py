# Generated by Django 4.0.6 on 2022-07-28 11:12
import datetime

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DjangoProject",
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
                ("title", models.CharField(max_length=50)),
                (
                    "modules_numbers",
                    models.DecimalField(decimal_places=2, max_digits=1000),
                ),
                (
                    "date",
                    models.DateTimeField(
                        default=datetime.datetime(2022, 7, 28, 11, 12, 54, 649915),
                        verbose_name="Published in ",
                    ),
                ),
            ],
        ),
    ]
