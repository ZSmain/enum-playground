from core.enums import CategoryStrEnumProp, CategoryTextChoices
from core.models import ProductStrEnumProp, ProductTextChoices
from core.utils.print_context import _print_context, print_context_decorator
from django.test import TestCase

@print_context_decorator
class TestProduct(TestCase):
    def test_str_enum_prop(self):
        product = ProductStrEnumProp.objects.create(
            name="Laptop",
            price=999.99,
            category=CategoryStrEnumProp.ELECTRONICS,
        )
        _print_context(product, "category")
        _print_context(product, "category", "category.label", "category.symbol")
        _print_context(product.category.label)
        _print_context(product.category.symbol)
        _print_context(dict(CategoryStrEnumProp.__dict__))
        # _print_context(dir(CategoryStrEnumProp))
        # for attr in dir(CategoryStrEnumProp):
        #     # if its a function, slot wrapper or method, skip it
        #     if callable(getattr(CategoryStrEnumProp, attr)):
        #         continue
        #     print(attr, ": ", getattr(CategoryStrEnumProp, attr))
        self.assertEqual(str(product), "Laptop (⚡)")

    def test_text_choices(self):
        product = ProductTextChoices.objects.create(
            name="T-shirt",
            price=19.99,
            category=CategoryTextChoices.CLOTHING,
        )
        _print_context(product, "category")
        _print_context(product, "category", "category.label", "category.symbol")
        _print_context(product.category.label)
        _print_context(product.category.symbol)
        _print_context(dict(CategoryStrEnumProp.__dict__))
        # _print_context(dir(CategoryStrEnumProp))
        # for attr in dir(CategoryStrEnumProp):
        #     # if its a function, slot wrapper or method, skip it
        #     if callable(getattr(CategoryStrEnumProp, attr)):
        #         continue
        #     print(attr, ": ", getattr(CategoryStrEnumProp, attr))
        self.assertEqual(str(product), "T-shirt (👕)")








