import django.db.models.deletion

from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(

            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('descricao', models.CharField(max_length=100)),
            ]

            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('cpf', models.CharField(max_length=11)),
                ('telefone', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=45)),
                ('pai_aluno', models.CharField(max_length=45)),
                ('mae_aluno', models.CharField(max_length=45)),
            ]

            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=45)),
                ('formacao', models.CharField(max_length=45)),
            ]

            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('descricao', models.CharField(max_length=45)),
            ],

            name='Nota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestao_escolar.disciplina')),
            ],
        ),
        migrations.AddField(
            model_name='disciplina',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestao_escolar.professor'),
        ),
    ]