# Generated by Django 2.2 on 2019-05-08 12:38

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190508_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communityentry',
            name='census_blocks_polygon',
            field=django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4326),
        ),
    ]
