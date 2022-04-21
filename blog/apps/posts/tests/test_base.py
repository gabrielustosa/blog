from django.test import TestCase

from blog.apps.authors.models import User
from blog.apps.posts.models import Category, Post


class PostMixin:
    def make_category(self, name='Category'):
        return Category.objects.create(name=name)

    def make_author(
            self,
            name='user',
            password='123456',
            email='username@email.com',
    ):
        return User.objects.create_user(
            name=name,
            password=password,
            email=email,
        )

    def make_post(
            self,
            author_data=None,
            category_data=None,
            title='teste',
            content='Teste teste teste',
            description='Teste',
            is_published=False,
    ):
        if category_data is None:
            category_data = {}

        if author_data is None:
            author_data = {}

        return Post.published.create(
            category=self.make_category(**category_data),
            author=self.make_author(**author_data),
            title=title,
            content=content,
            description=description,
            is_published=is_published,
            image=''
        )


class PostTestBase(TestCase, PostMixin):
    def setUp(self):
        return super().setUp()
