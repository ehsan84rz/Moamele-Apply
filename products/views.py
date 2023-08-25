from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from .models import Product


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/product_list.html'
