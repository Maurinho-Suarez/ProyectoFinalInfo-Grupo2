# Register your models here.
from django.contrib import admin
from .models import Categoria, Post



@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('titulo','autor','categoria','descripcion_post',
                    'fecha_creado','fecha_editado','imagen')

admin.site.register(Categoria)
