# Generated by Django 2.0.7 on 2018-08-08 01:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilemodel',
            name='UserProfileRelation',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
