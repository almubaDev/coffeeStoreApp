from django import forms
from django.forms.widgets import ClearableFileInput
from .models import Product


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = ''  # Personaliza la etiqueta
    initial_text = 'Imagen actual'
    input_text = 'Cambiar imagen'
    
   

class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'product_image']
        labels = {
            'name' : 'Nombre del producto',
            'description' : 'Descripción del producto',
            'price' : 'Precio',
            'product_image' : ''
        }
        
        widgets = {
            'product_image': CustomClearableFileInput,
        }

class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'product_image', 'available']
        labels = {
            'name' : 'Nombre del producto',
            'description' : 'Descripción del producto',
            'price' : 'Precio',
            'product_image' : '',
            'available' : 'Disponible'
        }
        
        widgets = {
            'product_image': CustomClearableFileInput,
        }