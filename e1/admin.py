from django.contrib import admin
from e1.models import juguetes,electro,ropa

# Register your models here.
class juguetesAdmin(admin.ModelAdmin):
    list_display = ['id','Producto', 'marca', 'stock', 'precio']

class electroAdmin(admin.ModelAdmin):
    list_display = ['id','Producto', 'marca', 'stock', 'precio']

class ropaAdmin(admin.ModelAdmin):
    list_display = ['id','Producto', 'marca', 'stock', 'precio']

admin.site.register(juguetes, juguetesAdmin)
admin.site.register(electro, electroAdmin )
admin.site.register(ropa, ropaAdmin )