from django.contrib import admin
from catalogo.models import Categoria
from catalogo.models import Producto
from catalogo.models import Venta
from catalogo.models import Detalle_venta
from catalogo.models import Cliente 
from catalogo.models import Empleado

# Register your models here.



admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Venta)
admin.site.register(Detalle_venta)
admin.site.register(Cliente)
admin.site.register(Empleado)







