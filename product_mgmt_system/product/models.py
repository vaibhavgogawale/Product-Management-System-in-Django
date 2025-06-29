from datetime import datetime

from django.db import models
from django.db.models import IntegerField


# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = IntegerField()
    category = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (f"Product ID: {self.product_id}, Name: {self.name}, Desc: {self.description}, "
                f"Price: {self.price}, Stocks: {self.stock_quantity}, Category: {self.category}")