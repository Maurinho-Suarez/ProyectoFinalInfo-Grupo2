from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy


from .models import Post

# CRUD para Post
class CrearPost(CreateView):
    model = Post
    fields = ['titulo','autor','descripción_post','fecha_creado','fecha_editado','imagen']
    template_name = 'posts/agregar_post.html'
    success_url = reverse_lazy('index')

class ActualizarPost(UpdateView):
    model = Post
    fields = ['titulo','autor','descripcion','fecha_creado','fecha_editado','imagen']
    template_name = 'posts/agregar_post.html'
    success_url = reverse_lazy('index')

class EliminarPost(DeleteView):
    model = Post
    template_name = 'general/confirma_eliminar.html'
    success_url = reverse_lazy('index')

class ListarPost(ListView):
    model = Post
    template_name = 'posts/listar_posts.html'
    context_object_name = 'posts'

