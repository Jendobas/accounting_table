# Generated by Django 4.2.5 on 2023-10-10 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tab', '0010_rename_quantity_product_shipment'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date',
            field=models.DateField(auto_now_add=True, default='1985-05-14'),
            preserve_default=False,
        ),
    ]
