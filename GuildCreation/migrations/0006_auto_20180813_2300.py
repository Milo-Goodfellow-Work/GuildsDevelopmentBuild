# Generated by Django 2.0.7 on 2018-08-13 23:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GuildCreation', '0005_memberlistmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guildmodel',
            name='GuildSize',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(2)]),
        ),
    ]
