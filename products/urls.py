from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListProductsAvailableView.as_view(), name='products_list'),
    path('create/', views.CreateProductView.as_view(), name='products_create'),
    path('detail/<int:pk>', views.DetailProductsView.as_view(), name='product_detail'),
    path('edit/<int:pk>', views.UpdateProductView.as_view(), name='product_edit'),
    path('delete/<int:id>', views.delete_product, name='delete_product')
]  

