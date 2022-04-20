from django.db import models

from blog.apps.authors.models import User
from blog.apps.posts.models import Post, Base


class Comment(Base):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(verbose_name='Comentário')
