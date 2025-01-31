from django.db import models

# Create your models here.
class Sizes(models.Model):
    size = models.CharField(max_length=12)

    def __str__(self):
        return self.size
    
class Category(models.Model):
    name = models.CharField(max_length=50)  
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name
    


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    size = models.ManyToManyField(Sizes, blank=True)
    product_code = models.CharField(max_length=30, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image_url = models.CharField(max_length=500)

    def __str__(self):
        return f"Image for {self.product.name}"

