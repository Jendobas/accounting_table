# Generated by Django 4.2.5 on 2023-09-25 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tab', '0005_remove_product_seller_delete_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]