# Generated by Django 4.1.3 on 2023-02-14 12:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("api", "0003_report"),
    ]

    operations = [
        migrations.AlterField(
            model_name="report",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_files",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
