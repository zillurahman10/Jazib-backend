from django.db import models

# Create your models here.
class Sizes(models.Model):
    size = models.CharField(max_length=12)

    def __str__(self):
        return self.size


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    image = models.CharField(max_length=200, null=True)
    size = models.ManyToManyField(Sizes, blank=True)
    product_code = models.CharField(max_length=30, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

