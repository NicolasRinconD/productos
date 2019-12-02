from djongo import models


class Producto(models.Model):
    descripcion = models.CharField(max_length=40)
    nombre = models.CharField(max_length=50)
    alturaTacon = models.FloatField(null=True, blank=True, default=None)
    tipo = models.CharField(max_length=50)
    forro = models.CharField(max_length=50)
    tacon = models.CharField(max_length=50)
    capellada = models.CharField(max_length=50)
    alturaSuela = models.FloatField(null=True, blank=True, default=None)
    color = models.CharField(max_length=50)
    peso = models.FloatField(null=True, blank=True, default=None)
    marca = models.CharField(max_length=50)
    plantilla = models.CharField(max_length=50)
    suela = models.CharField(max_length=50)
    ocasion = models.CharField(max_length=50)
    talla = models.IntegerField(null=True, blank=True, default=None)
    precio = models.FloatField(null=True, blank=True, default=0.0)

    def __str__(self):
        return '%s  %s %s %s %s %s' % (self.color, self.nombre, self.peso, self.alturaSuela, self.suela, self.precio)
