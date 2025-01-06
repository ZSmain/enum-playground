from django import forms

from .models import ProductStrEnumProp, ProductTextChoices


class ProductStrEnumPropForm(forms.ModelForm):
    class Meta:
        model = ProductStrEnumProp
        fields = ["name", "price", "category"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-select"}),
        }


class ProductTextChoicesForm(forms.ModelForm):
    class Meta:
        model = ProductTextChoices
        fields = ["name", "price", "category"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-select"}),
        }
