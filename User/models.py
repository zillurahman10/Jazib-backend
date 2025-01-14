from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=200)
    address = models.CharField(max_length=300, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    age = models.CharField(max_length=2, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.username
    