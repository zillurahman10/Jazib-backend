# Generated by Django 5.0.6 on 2025-01-31 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0008_alter_order_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='Pending', max_length=20),
        ),
    ]
