from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Post(models.Model):
    image = models.ImageField(verbose_name="Imagen")
    title = models.CharField(max_length=200, verbose_name="Titulo")
    desc = models.TextField(verbose_name="Descricion")
    content = RichTextField(verbose_name="Contenido")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificacion")

    class Meta:
        verbose_name = "Publicacion"
        verbose_name_plural = "Publicaciones"
        ordering = ["-created"]

    def __str__(self):
        return self.title
