from django.db import models
from Product.models import Product
from django.contrib.postgres.fields import ArrayField  # For PostgreSQL specific array field
from django.contrib.postgres.fields import JSONField  # For storing complex data
# Create your models here.



# class Order(models.Model):
#     full_name = models.CharField(max_length=200)
#     email = models.EmailField(max_length=254)
#     phone_number = models.CharField(max_length=20)
#     address = models.CharField(max_length=300)
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)
#     order_date = models.DateTimeField(auto_now_add=True)
#     order_status = models.CharField(max_length=20, default='Pending')
#     created_at = models.DateTimeField(auto_now_add=True)

# You may want to define the order status choices as a tuple
ORDER_STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Confirmed', 'Confirmed'),
    ('Shipped', 'Shipped'),
    ('Delivered', 'Delivered'),
    ('Cancelled', 'Cancelled'),
]

class Order(models.Model):
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    payment_method = models.CharField(max_length=100)
    transaction_id = models.CharField(max_length=200)
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=20, default='Pending', choices=ORDER_STATUS_CHOICES, null=True, blank=True)

    def __str__(self):
        return f"Order {self.id} by {self.first_name} {self.last_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"