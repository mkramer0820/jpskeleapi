# Generated by Django 2.1 on 2018-09-18 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, null=True, verbose_name='Company Name')),
                ('slug', models.SlugField(blank=True, max_length=40, unique=True)),
                ('address1', models.CharField(blank=True, max_length=64, null=True, verbose_name='Address1')),
                ('address2', models.CharField(blank=True, max_length=64, null=True, verbose_name='Address2')),
                ('address3', models.CharField(blank=True, max_length=64, null=True, verbose_name='Address3')),
                ('country', models.CharField(blank=True, max_length=64, null=True, verbose_name='country')),
                ('state-prov', models.CharField(blank=True, max_length=64, null=True, verbose_name='State-Province')),
                ('zip', models.CharField(blank=True, max_length=10, null=True, verbose_name='Zip or Postal Code')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('website', models.URLField(blank=True, null=True, verbose_name='Website')),
                ('description', models.TextField(blank=True, null=True)),
                ('createdOn', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
    ]
