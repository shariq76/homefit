from django.db import models
from django.contrib.auth.models import User

from fitapp.models import Products


# Create your models here.

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    s_product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.s_product)

    def total(self):
        return self.s_product.price * self.quantity


class OrderTable(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    total_amount = models.IntegerField()

    def __str__(self):
        if self is not None:
            return "#" + str(self.id)


class OrderDetails(models.Model):
    order = models.ForeignKey(OrderTable, on_delete=models.CASCADE)
    product = models.TextField()
    product_quantity = models.IntegerField()
    total_price = models.IntegerField()

    def __str__(self):
        return "#" + str(self.order.id) + " " + self.product
