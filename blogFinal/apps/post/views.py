from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from mixins.custom_test_mixin import CustomTestMixin

from .models import Categoria, Post
from apps.comentarios.forms import ComentarioForm
from apps.comentarios.models import Comentario

# CRUD para Categoría
class CrearCategoria(LoginRequiredMixin,CustomTestMixin, CreateView):
    model = Categoria
    fields = ['nombre']
    template_name = 'posts/agregar_categoria.html'
    success_url = reverse_lazy('index')

class ActualizarCategoria(UpdateView, CustomTestMixin):
    model = Categoria
    fields = ['nombre']
    template_name = 'posts/agregar_categoria.html'
    success_url = reverse_lazy('index')

class EliminarCategoria(DeleteView, CustomTestMixin):
    model = Categoria
    template_name = 'general/confirma_eliminar.html'
    success_url = reverse_lazy('index')

#-----------------------------------------------------

# CRUD para Post
class CrearPost(CreateView, CustomTestMixin):
    model = Post
    fields = ['titulo','autor','descripcion_post','categoria','imagen']
    template_name = 'posts/agregar_post.html'
    success_url = reverse_lazy('index')

class ActualizarPost(UpdateView, CustomTestMixin):
    model = Post
    fields = ['titulo','autor','descripcion_post','categoria','imagen']
    template_name = 'posts/agregar_post.html'
    success_url = reverse_lazy('index')

class EliminarPost(DeleteView, CustomTestMixin):
    model = Post
    template_name = 'general/confirma_eliminar.html'
    success_url = reverse_lazy('index')

class ListarPost(ListView):
    model = Post
    template_name = 'posts/listar_posts.html'
    context_object_name = 'posts'

    def get_context_data(self):
        context= super().get_context_data()
        categorias= Categoria.objects.all()
        context ["categorias"] = categorias
        return context

def listar_post_categoria(request,categoria):
    categoria_db=Categoria.objects.filter(nombre = categoria)
    posts= Post.objects.filter(categoria = categoria_db[0].id)
    template_name='posts/listar_posts.html'
    context= {
        'posts': posts 
    }
    return render(request, template_name= template_name, context= context)

def detalle_post(request,id):
    post = Post.objects.get(id = id)
    comentarios= Comentario.objects.filter(post=id)
    form= ComentarioForm(request.POST)

    if form.is_valid():
        if request.user.is_authenticated: 
            aux= form.save(commit=False)
            aux.post= post
            aux.user= request.user
            aux.save()
            form= ComentarioForm()

        else: 
            return redirect('apps.blog_auth:iniciar_sesion')
        
    context= {
        "post": post,
        "form" : form, 
        "comentarios" : comentarios
    }
    template_name = "posts/detalle_post.html"

    return render(request, template_name=template_name,context=context)

