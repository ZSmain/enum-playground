from enum_properties import StrEnumProperties
from django_enum.choices import TextChoices


class CategoryStrEnumProp(StrEnumProperties):
    label: str
    symbol: str
    description: str

    ELECTRONICS = "E", "Electronics", "⚡", "Electronic devices and accessories"
    CLOTHING = "C", "Clothing", "👕", "Apparel and fashion items"
    BOOKS = "B", "Books", "📚", "Books and publications"
    FOOD = "F", "Food", "🍔", "Food and beverages"


class CategoryTextChoices(TextChoices):
    # label is added by the base class (TextChoices)
    symbol: str
    description: str

    ELECTRONICS = "E", "Electronics", "⚡", "Electronic devices and accessories"
    CLOTHING = "C", "Clothing", "👕", "Apparel and fashion items"
    BOOKS = "B", "Books", "📚", "Books and publications"
    FOOD = "F", "Food", "🍔", "Food and beverages"
