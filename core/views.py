from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import ProductStrEnumPropForm, ProductTextChoicesForm
from .models import ProductStrEnumProp, ProductTextChoices


class ProductCreateView(TemplateView):
    template_name = "core/product_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form_type = self.request.GET.get("form_type", "str_enum")

        if form_type == "text_choices":
            context["form"] = ProductTextChoicesForm()
            context["products"] = ProductTextChoices.objects.all().order_by("-id")
        else:
            context["form"] = ProductStrEnumPropForm()
            context["products"] = ProductStrEnumProp.objects.all().order_by("-id")

        context["current_type"] = form_type
        return context

    def post(self, request, *args, **kwargs):
        form_type = request.POST.get("form_type", "str_enum")

        if form_type == "text_choices":
            form = ProductTextChoicesForm(request.POST)
        else:
            form = ProductStrEnumPropForm(request.POST)

        if form.is_valid():
            form.save()
            return self.get(request, *args, **kwargs)

        context = self.get_context_data()
        context["form"] = form
        return render(request, self.template_name, context)
