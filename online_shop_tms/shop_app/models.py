from __future__ import unicode_literals
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Discount(models.Model):
    name = models.CharField(max_length=50)
    percent = models.IntegerField()
    allow_to_sum_with_promo = models.BooleanField()


class ProductItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    count_on_stock = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='media/products', null=True, blank=True, default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Promocode(models.Model):
    name = models.CharField(max_length=100)
    percent = models.IntegerField()
    expire = models.DateTimeField()

    def __str__(self):
        return self.name
