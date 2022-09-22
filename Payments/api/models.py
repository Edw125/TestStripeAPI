from django.db import models


class Item(models.Model):
    CURRENCY = [
        ('RUB', 'Rouble'),
        ('USD', 'US dollar'),
        ('EUR', 'Euro'),
        ('GBP', 'British pound sterling'),
    ]

    stripe_price_id = models.CharField(max_length=100)
    name = models.CharField('Name', max_length=200)
    description = models.TextField('Description')
    price = models.PositiveIntegerField()
    currency = models.CharField(
        max_length=3,
        choices=CURRENCY,
        default=CURRENCY[0][0],
    )

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Name'
        verbose_name_plural = 'Names'

    def __str__(self):
        return self.name


class Order(models.Model):
    pass


class Discount(models.Model):
    pass


class Tax(models.Model):
    pass
