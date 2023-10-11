from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # отображение
    list_display = ['art', 'model', 'color', 'size', 'structure', 'shipment', 'count', 'remains', 'seller']
    # указываем редактируемые иконки
    list_editable = ['model', 'color', 'size', 'structure', 'shipment', 'count', 'seller']
    list_filter = ['seller', 'model']

    # def count_prod(self, prod: Product):  # создаём вычисляемые поля в админке
    #     count_prod = prod.count - prod.quantity
    #     return count_prod
