# Generated by Django 2.2.6 on 2020-05-20 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_address_city'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'ordering': ('entry',)},
        ),
        migrations.RenameField(
            model_name='address',
            old_name='entry_ID',
            new_name='entry',
        ),
    ]
