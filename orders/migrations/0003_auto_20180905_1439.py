# Generated by Django 2.1 on 2018-09-05 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20180904_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_type',
            field=models.CharField(choices=[('Delivary Duty Paid', 'DDP'), ('Freight On Board', 'FOB'), ('NA', 'NA')], max_length=40, null=True, verbose_name='Shipment Type'),
        ),
    ]