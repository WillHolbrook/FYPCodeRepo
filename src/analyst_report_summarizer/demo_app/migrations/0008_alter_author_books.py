# Generated by Django 4.1.3 on 2022-11-17 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_app', '0007_alter_character_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='authors', to='demo_app.book'),
        ),
    ]
