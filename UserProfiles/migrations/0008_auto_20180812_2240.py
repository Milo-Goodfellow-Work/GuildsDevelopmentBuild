# Generated by Django 2.0.7 on 2018-08-12 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfiles', '0007_auto_20180812_2238'),
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
            field=models.ImageField(blank=True, default='UserProfiles/Defaults/BlankWhite.png', null=True, upload_to='UserProfiles/'),
        ),
        migrations.AlterField(
            model_name='userprofilemodel',
            name='UserProfileImage',
            field=models.ImageField(blank=True, default='UserProfiles/Defaults/Blank.png', null=True, upload_to='UserProfiles/'),
        ),
        migrations.AlterField(
            model_name='userprofilemodel',
            name='UserProfileWebsite',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
