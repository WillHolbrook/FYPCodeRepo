# -*- coding: utf-8 -*-
# Generated by Django 4.1.7 on 2023-02-26 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0008_termidf"),
    ]

    operations = [
        migrations.AlterField(
            model_name="report",
            name="corpus_flag",
            field=models.BooleanField(default=False),
        ),
    ]
