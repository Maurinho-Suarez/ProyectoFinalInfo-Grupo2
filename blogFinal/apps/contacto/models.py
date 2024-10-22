from django.db import models

from django.contrib.auth.models import User
# Create your models here.

opc_contacto = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "felicitaciones"],
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Apellido y Nombre")
    email = models.EmailField(verbose_name="Correo eléctronico")
    mensaje = models.TextField(verbose_name="Mensaje")
    tipo_contacto = models.IntegerField(choices=opc_contacto,verbose_name="Tipo de contacto")
    suscripcion = models.BooleanField(default=False, verbose_name="Suscribirme a correos informativos")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de envio")

    def __str__(self):
        return self.nombre