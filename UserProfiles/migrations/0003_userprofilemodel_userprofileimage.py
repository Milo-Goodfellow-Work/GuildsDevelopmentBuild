# Generated by Django 2.0.7 on 2018-08-08 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfiles', '0002_auto_20180808_0134'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofilemodel',
            name='UserProfileImage',
            field=models.ImageField(blank=True, null=True, upload_to='UserProfiles/'),
        ),
    ]
