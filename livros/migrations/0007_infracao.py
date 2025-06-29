# Generated by Django 4.2.23 on 2025-06-22 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0006_remove_reserva_data_devolucao_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Infracao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ocorrencia', models.CharField(choices=[('PERDIDO', 'Perdido'), ('DANIFICADO', 'Danificado')], max_length=20)),
                ('emprestimo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livros.emprestimo')),
            ],
        ),
    ]
