from django.db import models
from Product.models import Product
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


class Order(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.full_name}"

    def calculate_total_price(self):
        total = sum(item.price * item.quantity for item in self.order_items.all())
        self.total_price = total
        self.save()

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price at the time of order

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"