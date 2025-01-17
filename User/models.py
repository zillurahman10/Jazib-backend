from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Add on_delete
    address = models.CharField(max_length=300, null=True, blank=True)  # Allow blank
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    age = models.CharField(max_length=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username  # Fix the reference to the username
