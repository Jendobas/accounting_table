from django.contrib import admin

from .models import Product, Deliveries


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # отображение
    list_display = ['art', 'model', 'color', 'size', 'structure', 'shipment', 'count', 'remains', 'seller']
    # указываем редактируемые иконки
    list_editable = ['model', 'color', 'size', 'structure', 'shipment', 'count', 'seller']
    list_filter = ['seller', 'model']


@admin.register(Deliveries)
class DeliveriesAdmin(admin.ModelAdmin):
    list_display = ['comment', 'date']

