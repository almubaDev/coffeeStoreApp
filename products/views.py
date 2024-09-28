from django.shortcuts import (render, get_object_or_404,
                              redirect)
from django.urls import reverse_lazy, reverse
from django.views.generic import (ListView, CreateView, 
                                  DetailView, UpdateView,
                                  DeleteView)
from .models import Product
from .forms import ProductCreateForm, ProductUpdateForm


class ListProductsAvailableView(ListView):
    model = Product
    template_name = 'products/products_list.html'
    context_object_name = 'products'
    
    def get_queryset(self):
        return self.model.objects.filter(available=True)


class CreateProductView(CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'products/create_products.html'
    # success_url = reverse_lazy('products_list')
    
    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})
    
class DetailProductsView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

class UpdateProductView(UpdateView):
    model = Product
    form_class = ProductUpdateForm
    template_name = 'products/update_product.html'
    # success_url = reverse_lazy('products_list')
    
    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})
    


def delete_product(request, id=None):
    delete_product = get_object_or_404(Product, id=id)
    delete_product.delete()
    return redirect('products_list')