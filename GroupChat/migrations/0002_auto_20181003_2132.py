# Generated by Django 2.0.7 on 2018-10-03 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GroupChat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='PostBody',
            new_name='MessageBody',
        ),
    ]
