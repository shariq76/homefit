# Generated by Django 4.0 on 2022-01-11 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0012_ordertable_orderdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetails',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cartitem'),
        ),
    ]
