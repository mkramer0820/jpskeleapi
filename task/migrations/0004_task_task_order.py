# Generated by Django 2.1 on 2018-09-18 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
        ('task', '0003_auto_20180918_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_order',
            field=models.ForeignKey(default='1', on_delete='CASCADE', to='orders.Orders'),
            preserve_default=False,
        ),
    ]