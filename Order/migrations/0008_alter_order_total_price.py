# Generated by Django 5.0.6 on 2025-01-31 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0007_alter_order_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
