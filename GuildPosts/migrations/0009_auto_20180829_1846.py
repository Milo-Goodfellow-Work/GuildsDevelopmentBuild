# Generated by Django 2.0.7 on 2018-08-29 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GuildPosts', '0008_remove_postmodel_postlink'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='PostLikes',
        ),
        migrations.RemoveField(
            model_name='postmodel',
            name='PostReply',
        ),
    ]
