from django.db import models

from blog.apps.authors.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(is_published=True)


class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(Base):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(Base):
    title = models.CharField(max_length=255, verbose_name='Título')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Autor')
    content = models.TextField(verbose_name='Conteúdo')
    description = models.TextField(verbose_name='Descrição')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoria')
    image = models.ImageField(upload_to='posts/%Y/%m/%d/', verbose_name='Imagem')
    is_published = models.BooleanField(default=False, verbose_name='Publicar')
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title
