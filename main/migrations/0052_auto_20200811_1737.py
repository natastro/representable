# Generated by Django 2.2.13 on 2020-08-11 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0051_auto_20200811_1632"),
    ]

    operations = [
        migrations.RemoveField(model_name="blockgroup", name="geometry",),
        migrations.AlterField(
            model_name="blockgroup",
            name="census_id",
            field=models.CharField(max_length=12),
        ),
    ]
