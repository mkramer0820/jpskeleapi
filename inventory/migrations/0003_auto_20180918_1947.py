# Generated by Django 2.1 on 2018-09-18 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20180918_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spec',
            name='spec',
            field=models.CharField(max_length=30),
        ),
    ]
