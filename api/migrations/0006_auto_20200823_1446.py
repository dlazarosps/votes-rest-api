# Generated by Django 2.2 on 2020-08-23 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_vote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='begin',
            field=models.DateTimeField(),
        ),
    ]
