from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

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


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    context_object_name = 'product'
    form_class = NewProductForm
    template_name = 'products/product_update.html'


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('products:product_list')
    template_name = 'products/product_delete.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    form_class = NewProductForm
    template_name = 'products/product_create.html'

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)
