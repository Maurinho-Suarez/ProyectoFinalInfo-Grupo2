from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import CrearContacto, ModificarContacto, EliminarContacto, ListarContacto

app_name = 'apps.contacto'

urlpatterns = [
    path("agregar_contacto/", CrearContacto.as_view(), name='agregar_contacto'),
    path("agregar_contacto/", ModificarContacto.as_view(), name='agregar_contacto'),
    path('eliminar_contacto/', EliminarContacto.as_view(), name='eliminar_contacto'),
    path("listar_contactos/", ListarContacto.as_view(), name='listar_contactos')
]