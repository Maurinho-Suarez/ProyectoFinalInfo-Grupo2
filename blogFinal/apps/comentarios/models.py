from django.db import models

from apps.post.models import Post
from django.contrib.auth.models import User

class Comentario(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    texto = models.TextField(verbose_name='Comentario')
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.texto

    class Meta:
        ordering = ['-fecha']