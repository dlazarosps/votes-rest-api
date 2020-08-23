# Generated by Django 2.2 on 2020-08-23 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_vote_user'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='vote',
            constraint=models.UniqueConstraint(fields=('session', 'user'), name='unique vote for session user'),
        ),
    ]
