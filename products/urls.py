from django.urls import path

from .views import ProductListView, ProductDetailView, ProductUpdateView, ProductDeleteView

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('<int:pk>/edit', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
]
