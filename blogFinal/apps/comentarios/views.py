from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.comentarios.forms import ComentarioForm
from .models import Comentario

def agregar_comentario(request):
    form = ComentarioForm(request.POST)
    if form.is_valid():
        form.save()
        form = ComentarioForm()

    template_name= 'comentarios/agregar_comentario.html'
    context = {
        'form' : form,
    }

    return render(request, template_name, context)

def comentarios(request):
    comentarios = Comentario.object.all()
    template_name = 'comentarios/listar_comentarios.html'
    context = {
    'comentarios' : comentarios,
    }
    return render(request, template_name, context)

class ModificarComentario(LoginRequiredMixin, UpdateView):
    model = Comentario
    fields = ['texto',]
    template_name = 'comentarios/agregar_comentario.html'
    success_url = reverse_lazy('apps.comentarios:listar_comentarios')

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        return queryset.filter(user = self.request.user)
    
class EliminarComentario(LoginRequiredMixin, DeleteView):
    model = Comentario
    template_name = 'general/confirma_eliminar.html'
    success_url = reverse_lazy('apps.comentarios:listar_comentarios')