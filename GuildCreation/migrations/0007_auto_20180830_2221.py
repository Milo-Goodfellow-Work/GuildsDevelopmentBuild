# Generated by Django 2.0.7 on 2018-08-30 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GuildCreation', '0006_auto_20180813_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guildmodel',
            name='GuildInvite',
            field=models.BigIntegerField(),
        ),
    ]
