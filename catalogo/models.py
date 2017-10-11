from django.db import models
from core.models import User, Person

# Create your models here.


class Categoria(models.Model):

    nombre = models.CharField(max_length=60)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return '%s' % (self.nombre)


class Producto(models.Model):

    nombre = models.CharField(max_length=60)
    codigo = models.CharField(max_length=10, null=True, blank=True)
    detalle = models.TextField(null=True, blank=True)
    precio_venta = models.FloatField(default=0.0)
    categoria = models.ManyToManyField(
        "Categoria",
        verbose_name="list of Categorias",
        null=True,  blank=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return '%s (%s)' % (self.nombre, self.codigo)

class Cliente(models.Model):

    ruc = models.CharField(max_length=11)
    person = models.OneToOneField(Person)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return '%s' % (self.ruc)


class Venta(models.Model):

    nro_doc = models.CharField(max_length=15)
    fecha = models.DateTimeField(auto_now_add=True)
    prec_total = models.FloatField(default=0)
    vendedor = models.ForeignKey(User)
    cliente = models.ForeignKey(Cliente, blank=True, null=True)

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"

    def __str__(self):
        return '%s' % (self.nro_doc)


class Detalle_venta(models.Model):
    cantidad = models.IntegerField()
    precio_uni = models.FloatField(default=0)
    producto = models.ForeignKey(Producto)
    venta = models.ForeignKey(Venta)

    class Meta:
        verbose_name = "Detalle_venta"
        verbose_name_plural = "Detalle_ventas"

    def __str__(self):
        return 'VENTA%s-PROD: %s' % (self.venta.nro_doc, self.producto.nombre,)



class Empleado(models.Model):

    nombre = models.CharField(max_length=60)
    codigo = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"

    def __str__(self):
        return '%s' % (self.codigo)

        
