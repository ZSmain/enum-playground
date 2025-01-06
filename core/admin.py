from django.contrib import admin

from .models import ProductStrEnumProp, ProductTextChoices


@admin.register(ProductStrEnumProp)
class ProductStrEnumPropAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "price",
        "category",
        # "category_symbol",
        # "category_description",
    ]
    list_filter = ["category"]


@admin.register(ProductTextChoices)
class ProductTextChoicesAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "price",
        "category",
        # "category_symbol",
        # "category_description",
    ]
    list_filter = ["category"]
