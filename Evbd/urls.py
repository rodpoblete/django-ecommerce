from e1.views import login, index, elecData, jugarData, ropaData, agregar, editarElectro, eliminar,editar
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login),
    path('index/', index),
    path('index/electronica/', elecData),
    path('addelectro/', agregar),
    path('eliminar/<int:id>',eliminar),
    path('modificar/<int:id>', editar),
    path('editarElectro/', editarElectro),
    path('juguetes/', jugarData),
    path('ropa/', ropaData)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
