from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from .models import Product
from .forms import NewProductForm


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/product_list.html'


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'products/product_detail.html'


class ProductUpdateView(UpdateView):
    model = Product
    context_object_name = 'product'
    form_class = NewProductForm
    template_name = 'products/product_create.html'
