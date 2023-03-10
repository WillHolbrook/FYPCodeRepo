# -*- coding: utf-8 -*-
# Generated by Django 4.1.7 on 2023-03-10 16:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="report",
            name="buy_sell_hold",
            field=models.CharField(
                choices=[("Buy", "Buy"), ("Sell", "Sell"), ("Hold", "Hold")],
                default=None,
                max_length=4,
                null=True,
            ),
        ),
    ]
