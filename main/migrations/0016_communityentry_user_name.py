# Generated by Django 2.2.6 on 2020-05-17 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_merge_20200501_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='communityentry',
            name='user_name',
            field=models.CharField(default='', max_length=500),
        ),
    ]
