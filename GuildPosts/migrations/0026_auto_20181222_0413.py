# Generated by Django 2.0.7 on 2018-12-22 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GuildProfiles', '0002_auto_20180830_2241'),
        ('GuildPosts', '0025_auto_20181007_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='PostGuildProfile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GuildProfiles.GuildProfileModel'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='PostLink',
            field=models.BigIntegerField(default=5161187319),
        ),
    ]
