# Generated by Django 2.1 on 2018-09-18 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factorycontact',
            name='contact_phone_number',
            field=models.CharField(blank=True, max_length=30, verbose_name='Phone Number'),
        ),
    ]
