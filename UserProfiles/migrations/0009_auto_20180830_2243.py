# Generated by Django 2.0.7 on 2018-08-30 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfiles', '0008_auto_20180812_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilemodel',
            name='Id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
