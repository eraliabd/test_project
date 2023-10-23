from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.PositiveBigIntegerField()
    image = RichTextUploadingField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    last_accessed = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(price__gte=0),
                name="valid_price"
            ),
            models.CheckConstraint(
                check=models.Q(price__gt=0) | models.Q(is_published=False),
                name="published_products_have_positive_price"
            ),
        ]


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.PositiveBigIntegerField(null=True, blank=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.product.name


class Contact(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
