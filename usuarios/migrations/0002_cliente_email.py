# Generated by Django 4.2.23 on 2025-06-19 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.EmailField(default='teste@teste.com', max_length=254),
            preserve_default=False,
        ),
    ]
