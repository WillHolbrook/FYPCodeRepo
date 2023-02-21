# -*- coding: utf-8 -*-
# Generated by Django 4.1.3 on 2023-02-16 11:40

import datetime

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("api", "0004_alter_report_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="report",
            name="corpus_flag",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="report",
            name="in_idf_flag",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="report",
            name="last_modified",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="report",
            name="plaintext_datetime",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="report",
            name="sentence_datetime",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="report",
            name="tei_xml",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="report",
            name="upload_datetime",
            field=models.DateTimeField(
                auto_now_add=True,
                default=datetime.datetime(
                    2023, 2, 16, 11, 40, 45, 24146, tzinfo=datetime.timezone.utc
                ),
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="report",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reports",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]