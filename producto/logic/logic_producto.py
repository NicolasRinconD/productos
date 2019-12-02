from ..models import Producto

def get_productos():
    queryset = Producto.objects.all().order_by('nombre')
    return (queryset)

def create_producto(form):
    producto = form.save()
    producto.save()
    return ()