from rest_framework import serializers
from .models import Order, OrderItem
from Product.models import Product

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, source='order_items')  # Use related_name 'order_items'

    class Meta:
        model = Order
        fields = ['email', 'first_name', 'last_name', 'phone_number', 'address', 'transaction_id', 'payment_method', 'order_status', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('order_items')  # Extract items data
        order = Order.objects.create(**validated_data)  # Create the order

        # Create order items
        for item_data in items_data:
            product = Product.objects.get(id=item_data['product'].id)  # Fetch the product
            OrderItem.objects.create(order=order, product=product, quantity=item_data['quantity'])

        return order
