from typing import Any
from django.shortcuts import render
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from mixins.custom_test_mixin import CustomTestMixin

from apps.contacto.forms import ContactoForm
from .models import Contacto

class CrearContacto(CreateView):
    model = Contacto
    fields = ['nombre','email','mensaje','tipo_contacto','suscripcion']
    template_name = 'contacto/agregar_contacto.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        return super().form_valid(form)

class ModificarContacto(UpdateView, CustomTestMixin):
    model = Contacto
    fields = ['nombre','email','mensaje','tipo_contacto','suscripcion']
    template_name = 'contacto/agregar_contacto.html'
    success_url = reverse_lazy('index')

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        return queryset.filter(user = self.request.user)
    
class EliminarContacto(DeleteView, CustomTestMixin):
    model = Contacto
    template_name = 'general/confirma_eliminar.html'
    success_url = reverse_lazy('index')

class ListarContacto(LoginRequiredMixin,ListView):
    model = Contacto
    template_name = 'contacto/listar_contactos.html'
    context_object_name = 'contacto'

    def get_context_data(self):
        context= super().get_context_data()
        contactos= Contacto.objects.all()
        context ["contacto"] = contactos
        return context