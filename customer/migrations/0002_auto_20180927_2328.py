# Generated by Django 2.1 on 2018-09-28 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='state-prov',
            new_name='state',
        ),
    ]