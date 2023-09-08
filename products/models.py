from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.PositiveBigIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.PositiveBigIntegerField(null=True, blank=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.product.name
