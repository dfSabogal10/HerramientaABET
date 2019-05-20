# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-05-20 03:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('herramienta', '0005_auto_20190512_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='medidaOutcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.CharField(max_length=100)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
        migrations.RemoveField(
            model_name='curso',
            name='periodo',
        ),
        migrations.RemoveField(
            model_name='instrumentomedicion',
            name='curso',
        ),
        migrations.RemoveField(
            model_name='instrumentomedicion',
            name='outcome',
        ),
        migrations.RemoveField(
            model_name='outcomeabet',
            name='calificacion',
        ),
        migrations.RemoveField(
            model_name='outcomeabet',
            name='periodo',
        ),
        migrations.AddField(
            model_name='instrumentomedicion',
            name='periodo',
            field=models.CharField(default=2018, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medidaoutcome',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='herramienta.Curso'),
        ),
        migrations.AddField(
            model_name='medidaoutcome',
            name='outcome',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='herramienta.OutcomeAbet'),
        ),
        migrations.AddField(
            model_name='instrumentomedicion',
            name='medidaOutcome',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='herramienta.medidaOutcome'),
            preserve_default=False,
        ),
    ]
