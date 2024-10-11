from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import CrearPost, ActualizarPost, EliminarPost, ListarPost, CrearCategoria, ActualizarCategoria, EliminarCategoria

app_name = 'apps.post'

urlpatterns = [
    path("agregar_post/", CrearPost.as_view(), name='agregar_post'),
    path("actualizar_post/<int:pk>", ActualizarPost.as_view(), name='actualizar_post'),
    path("eliminar_post/<int:pk>", EliminarPost.as_view(), name='eliminar_post'),
    path("listar_post/", ListarPost.as_view(), name='listar_post'),
        
    path("agregar_categoria/", CrearCategoria.as_view(), name= 'agregar_categoria'),
    path("actualizar_categoria/<int:pk>", ActualizarCategoria.as_view(), name = 'actualizar_categoria'),
    path("eliminar_categoria/<int:pk>", EliminarCategoria.as_view(), name= 'eliminar_categoria'),
    
]