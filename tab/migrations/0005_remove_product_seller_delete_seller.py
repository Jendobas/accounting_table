# Generated by Django 4.2.5 on 2023-09-25 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tab', '0004_remove_seller_products_product_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='seller',
        ),
        migrations.DeleteModel(
            name='Seller',
        ),
    ]