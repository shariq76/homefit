# Generated by Django 4.0 on 2022-01-18 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0021_ordertable_orderdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetails',
            name='total_price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]