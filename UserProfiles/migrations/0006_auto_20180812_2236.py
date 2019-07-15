# Generated by Django 2.0.7 on 2018-08-12 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfiles', '0005_auto_20180808_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilemodel',
            name='UserProfileBio',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='userprofilemodel',
            name='UserProfileHeader',
            field=models.ImageField(default='UserProfiles/Defaults/BlankWhite.png', upload_to='UserProfiles/'),
        ),
        migrations.AlterField(
            model_name='userprofilemodel',
            name='UserProfileImage',
            field=models.ImageField(default='UserProfiles/Defaults/Blank.png', upload_to='UserProfiles/'),
        ),
    ]