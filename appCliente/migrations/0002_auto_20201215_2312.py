# Generated by Django 3.1.4 on 2020-12-16 04:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appCliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='f_created',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Registrado el'),
        ),
    ]
