# Generated by Django 5.1.3 on 2024-11-30 04:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_rename_paciente_id_historicomedico_paciente_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Planos',
            new_name='Plano',
        ),
        migrations.AlterField(
            model_name='historicomedico',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 30, 4, 7, 50, 380269)),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='data_cadastro',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 30, 4, 7, 50, 379431)),
        ),
    ]
