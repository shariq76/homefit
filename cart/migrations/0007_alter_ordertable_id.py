# Generated by Django 4.0 on 2022-01-09 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_orderdetails_ordertable_delete_orders_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordertable',
            name='id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]