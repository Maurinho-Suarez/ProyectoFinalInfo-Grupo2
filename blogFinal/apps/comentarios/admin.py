# Register your models here.
from django.contrib import admin
from .models import Comentario

@admin.register(Comentario)
class ComentariosAdmin(admin.ModelAdmin):
    list_display = ('user','post','texto','fecha')

#admin.site.register(Comentario)
