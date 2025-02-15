# Generated by Django 5.1.3 on 2024-11-30 04:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicomedico',
            old_name='paciente_id',
            new_name='paciente',
        ),
        migrations.AlterField(
            model_name='historicomedico',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 30, 4, 6, 53, 989075)),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='data_cadastro',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 30, 4, 6, 53, 988256)),
        ),
    ]
