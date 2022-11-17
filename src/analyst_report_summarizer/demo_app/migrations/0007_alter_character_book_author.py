# Generated by Django 4.1.3 on 2022-11-17 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo_app', '0006_rename_charachter_character'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characters', to='demo_app.book'),
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('books', models.ManyToManyField(to='demo_app.book')),
            ],
        ),
    ]
