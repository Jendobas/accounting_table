from django.db import models


class Product(models.Model):
    GUM = 'GUM'
    SLAVUTINY = 'SLAVUTINY'
    SALON = 'SALON'

    SELLERS = [
        (GUM, 'Гум'),
        (SLAVUTINY, 'Славутины'),
        (SALON, 'Салон'),
    ]

    date = models.DateField(auto_now_add=True)
    art = models.CharField(max_length=20)
    model = models.CharField(max_length=80)
    color = models.CharField(max_length=20)
    size = models.CharField(max_length=20, blank=True)
    structure = models.CharField(max_length=20, blank=True, default='-')
    shipment = models.IntegerField(default=1)  # поставили вещей
    count = models.IntegerField(default=0)  # всего вещей
    seller = models.CharField(max_length=10, choices=SELLERS, default=GUM)

    def remains(self):
        if self.count < self.shipment:
            return self.count
        return self.count - self.shipment  # кол-во вещей на складе

    def __str__(self):
        return f'{self.art}, {self.model}, {self.color}, {self.size}, {self.structure}, {self.shipment}, {self.count}, {self.seller}'
