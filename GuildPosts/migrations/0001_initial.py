# Generated by Django 2.0.7 on 2018-08-19 01:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('GuildCreation', '0006_auto_20180813_2300'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('PostBody', models.TextField(max_length=500)),
                ('PostDate', models.DateField(default=datetime.date.today)),
                ('PostGuild', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GuildCreation.GuildModel')),
            ],
        ),
    ]