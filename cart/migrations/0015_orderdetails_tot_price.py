# Generated by Django 4.0 on 2022-01-18 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0014_alter_orderdetails_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetails',
            name='tot_price',
            field=models.IntegerField(),
        ),
    ]
