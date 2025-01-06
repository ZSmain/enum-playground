from django.utils.translation import gettext_lazy as _

from enum_properties import StrEnumProperties
from django_enum.choices import TextChoices


class CategoryStrEnumProp(StrEnumProperties):
    label: str
    symbol: str
    description: str

    ELECTRONICS = "E", _("Electronics"), "⚡", _("Electronic devices and accessories")
    CLOTHING = "C", _("Clothing"), "👕", _("Apparel and fashion items")
    BOOKS = "B", _("Books"), "📚", _("Books and publications")
    FOOD = "F", _("Food"), "🍔", _("Food and beverages")


class CategoryTextChoices(TextChoices):
    # label is added by the base class (TextChoices)
    symbol: str
    description: str

    ELECTRONICS = "E", _("Electronics"), "⚡", _("Electronic devices and accessories")
    CLOTHING = "C", _("Clothing"), "👕", _("Apparel and fashion items")
    BOOKS = "B", _("Books"), "📚", _("Books and publications")
    FOOD = "F", _("Food"), "🍔", _("Food and beverages")
