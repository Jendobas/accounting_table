from django.db import models


class Deliveries(models.Model):
    date = models.DateField(auto_now_add=True)
    comment = models.CharField(max_length=20, default='-')

    def __str__(self):
        return f'{self.date}'


class Product(models.Model):
    GUM = 'GUM'
    SLAVUTINY = 'SLAVUTINY'
    SALON = 'SALON'

    SELLERS = [
        (GUM, 'Гум'),
        (SLAVUTINY, 'Славутины'),
        (SALON, 'Салон'),
    ]

    art = models.CharField(max_length=20)
    model = models.CharField(max_length=80)
    color = models.CharField(max_length=20)
    size = models.CharField(max_length=20, blank=True)
    structure = models.CharField(max_length=20, blank=True, default='-')
    shipment = models.IntegerField(default=1)  # поставили вещей
    count = models.IntegerField(default=0)  # всего вещей
    seller = models.CharField(max_length=10, choices=SELLERS, default=GUM)
    date_name = models.ForeignKey(Deliveries, on_delete=models.PROTECT, null=True)

    def remains(self):
        if self.count < self.shipment:
            return self.count
        return self.count - self.shipment  # кол-во вещей на складе

    def __str__(self):
        return f'{self.art}, {self.model}, {self.color}, {self.size}, {self.structure}, {self.shipment}, {self.count}, {self.seller}'
