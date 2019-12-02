from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from setuptools.command.rotate import rotate

from .forms import ProductoForm
from .models import Producto
from django.contrib import messages
from django.urls import reverse
from .logic.logic_producto import create_producto, get_productos
from django.contrib.auth.decorators import login_required


def product_list(request):
    productos = get_productos()
    context = {
        'producto_list': productos,
    }
    return render(request, 'producto/productos.html', context)


def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            create_producto(form)
            messages.add_message(request, messages.SUCCESS, 'Producto creado')
            return HttpResponseRedirect('/producto')
        else:
            print(form.errors)
    else:
        form = ProductoForm()

    context = {
        'form': form,
    }

    return render(request, 'Producto/productoCreate.html', context)


def producto_update(request):
    producto_id = request.POST.get('producto_id')

    if producto_id:
        session = get_object_or_404(Producto, pk=producto_id)
    else:
        session = None

    """
    A subclass of ModelForm can accept an existing model instance 
    as the keyword argument instance; 
    if this is supplied, save() will update that instance. 
    If it's not supplied, save() will create a new instance of the specified model.
    """
    form = ProductoForm(instance=session)

    if request.method == 'PUT':
        form = ProductoForm(request.PUT, instance=session)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
        else:
            print(form.errors)
    context = {
        'form': form,
    }

    return render(request, 'Producto/productoCreate.html', context)



def producto_delete(request, pk):
    query = Producto.objects.get(pk=pk)
    query.delete()
    productos = get_productos()
    context = {
        'producto_list': productos,

    }
    return render(request, 'producto/productos.html', context)