from django.db import models

# Create your models here.

class Post(models.Model):
    """Post model."""
    #user = models.ForeignKey(User, on_delete=models.PROTECT)
    #profile = models.ForeignKey('users.Profile', on_delete=models.PROTECT)

    titulo = models.CharField(max_length=80, null=False)
    autor = models.CharField(max_length=80, null=False)
    descripcion_post = models.TextField()
    fecha_creado= models.DateTimeField(auto_now_add=True)
    fecha_editado = models.DateTimeField(auto_now=True)
    imagen = models.ImageField(blank=True,null=True,upload_to="post", default="posts/post_default.png")

    def __str__(self):
        """Retorna titulo del post"""
        return self.titulo

class Categoria(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        """Retorna titulo de la categoria del post"""
        return self.nombre