# Generated by Django 5.1.3 on 2024-11-30 04:52

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0004_remove_historicomedico_descricao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cirurgia',
            name='paciente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.paciente'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='paciente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.paciente'),
        ),
        migrations.AddField(
            model_name='exame',
            name='paciente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.paciente'),
        ),
        migrations.AddField(
            model_name='tratamento',
            name='paciente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.paciente'),
        ),
        migrations.AlterField(
            model_name='historicomedico',
            name='cirurgia',
            field=models.ManyToManyField(to='hospital.cirurgia'),
        ),
        migrations.AlterField(
            model_name='historicomedico',
            name='consulta',
            field=models.ManyToManyField(to='hospital.consulta'),
        ),
        migrations.AlterField(
            model_name='historicomedico',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 30, 4, 52, 30, 706127, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='historicomedico',
            name='exame',
            field=models.ManyToManyField(to='hospital.exame'),
        ),
        migrations.AlterField(
            model_name='historicomedico',
            name='paciente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.paciente'),
        ),
        migrations.AlterField(
            model_name='historicomedico',
            name='tratamento',
            field=models.ManyToManyField(to='hospital.tratamento'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='data_cadastro',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 30, 4, 52, 30, 703517, tzinfo=datetime.timezone.utc)),
        ),
    ]
