# Generated by Django 2.2 on 2020-08-23 18:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20200823_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 23, 18, 52, 0, 379571)),
        ),
        migrations.AddConstraint(
            model_name='user',
            constraint=models.UniqueConstraint(fields=('cpf',), name='unique CPF in database'),
        ),
    ]
