#trae objetos

from apps.post.models import Categoria

def categorias_context(request):
    categoria= Categoria.objects.all()
    return {
        "categorias": categoria
    }