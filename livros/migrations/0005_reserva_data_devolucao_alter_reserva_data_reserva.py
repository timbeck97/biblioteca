# Generated by Django 4.2.23 on 2025-06-19 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0004_livro_genero_livro_isbn_livro_quantidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='data_devolucao',
            field=models.DateField(default='2025-06-30'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reserva',
            name='data_reserva',
            field=models.DateField(),
        ),
    ]
