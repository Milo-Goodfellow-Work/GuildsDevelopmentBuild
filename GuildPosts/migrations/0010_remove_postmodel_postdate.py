# Generated by Django 2.0.7 on 2018-08-29 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GuildPosts', '0009_auto_20180829_1846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='PostDate',
        ),
    ]
