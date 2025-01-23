from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['username', 'email', 'password']

    def save(self):
        username = self.validated_data['username']
        email = self.validated_data['email']
        password = self.validated_data['password']

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email already exists.')
        account = User(username=username, email=email, password=password)
        account.is_active = False
        account.save()
        return account