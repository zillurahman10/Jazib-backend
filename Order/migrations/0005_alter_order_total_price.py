# Generated by Django 5.0.6 on 2025-01-31 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0004_alter_order_transaction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
