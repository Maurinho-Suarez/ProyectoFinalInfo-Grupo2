from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .models import Categoria, Post

# CRUD para Categoría
class CrearCategoria(CreateView):
    model = Categoria
    fields = ['nombre']
    template_name = 'posts/agregar_categoria.html'
    success_url = reverse_lazy('index')

class ActualizarCategoria(UpdateView):
    model = Categoria
    fields = ['nombre']
    template_name = 'posts/agregar_categoria.html'
    success_url = reverse_lazy('index')

class EliminarCategoria(DeleteView):
    model = Categoria
    template_name = 'general/confirma_eliminar.html'
    success_url = reverse_lazy('index')

#-----------------------------------------------------

# CRUD para Post
class CrearPost(CreateView):
    model = Post
    fields = ['titulo','autor','descripcion_post','categoria','imagen']
    template_name = 'posts/agregar_post.html'
    success_url = reverse_lazy('index')

class ActualizarPost(UpdateView):
    model = Post
    fields = ['titulo','autor','descripcion_post','categoria','imagen']
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

