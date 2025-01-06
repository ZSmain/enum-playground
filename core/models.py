from django.db import models
from django_enum import EnumField

from .enums import CategoryStrEnumProp, CategoryTextChoices


class ProductStrEnumProp(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = EnumField(CategoryStrEnumProp, default=CategoryStrEnumProp.ELECTRONICS)

    def get_category(self):
        return CategoryStrEnumProp(self.category)

    @property
    def category_symbol(self):
        return self.get_category().symbol

    @property
    def category_description(self):
        return self.get_category().description

    def __str__(self):
        return f"{self.name} ({self.get_category().symbol})"


class ProductTextChoices(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = EnumField(CategoryTextChoices, default=CategoryTextChoices.ELECTRONICS)

    def get_category(self):
        return CategoryStrEnumProp(self.category)

    @property
    def category_symbol(self):
        return self.get_category().symbol

    @property
    def category_description(self):
        return self.get_category().description

    def __str__(self):
        return f"{self.name} ({self.get_category().symbol})"
