from django import forms

from .models import Comentario

class ComentarioForm(forms.ModelForm):
    
    class Meta:
        model = Comentario
        fields = ['texto']
        error_messages = {
            'texto': {
                'required': 'Por favor, añade tu comentario antes de enviarlo.',
            },
        }