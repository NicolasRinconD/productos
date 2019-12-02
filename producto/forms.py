from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre',
            'precio',
            'talla',
            'peso',
            'color',
        ]

        labels = {
            'nombre': 'Nombre',
            'precio': 'Precio',
            'talla': 'Talla',
            'peso': 'Peso',
            'color': 'Color',
        }