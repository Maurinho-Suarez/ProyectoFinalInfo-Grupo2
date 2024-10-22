# Register your models here.
from django.contrib import admin
from .models import Contacto

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre','email','mensaje','tipo_contacto','suscripcion')

#admin.site.register(Contacto)