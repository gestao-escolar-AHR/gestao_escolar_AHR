# Generated by Django 5.2.4 on 2025-07-04 19:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_escolar', '0002_aula'),
    ]

    operations = [
        migrations.CreateModel(
            name='Frequencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(null=True)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestao_escolar.aluno')),
                ('turma', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='gestao_escolar.turma')),
            ],
        ),
    ]
