# Generated by Django 4.2.5 on 2023-10-03 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tab', '0009_alter_product_structure'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='quantity',
            new_name='shipment',
        ),
    ]
