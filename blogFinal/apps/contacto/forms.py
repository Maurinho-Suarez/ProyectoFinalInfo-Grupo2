from django import forms

from .models import Contacto

class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        fields = ['nombre','email','mensaje','tipo_contacto','suscripcion']
        error_messages = {
            'nombre': {
                'required': 'Por favor, ingresa el nombre y apellido del contacto a registrarse.',
            },
            'email': {
                'required': 'Por favor, añade tu dirección de correo eléctronico para validar contacto.',
            },
            'tipo_contacto': {
                'required': 'Por favor, añade un tipo de contacto para validar el registro del nuevo contacto.',
            }
        }