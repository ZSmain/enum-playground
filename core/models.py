from django.db import models
from django_enum import EnumField

from .enums import CategoryStrEnumProp, CategoryTextChoices


class ProductStrEnumProp(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = EnumField(CategoryStrEnumProp, default=CategoryStrEnumProp.ELECTRONICS)

    def __str__(self):
        return f"{self.name} ({self.category.symbol})"


class ProductTextChoices(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = EnumField(CategoryTextChoices, default=CategoryTextChoices.ELECTRONICS)

    def __str__(self):
        return f"{self.name} ({self.category.symbol})"
