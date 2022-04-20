from typing import Dict

from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import TemplateView

from blog.apps.comments.form import CommentForm
from blog.apps.posts.models import Post
from blog.apps.comments.models import Comment


class PostDetailView(TemplateView):
    template_name = 'post/detail_view.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.form = CommentForm(request.POST or None)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_id = self.kwargs.get('post_id')
        post = Post.objects.get(id=post_id)
        context['post'] = post
        context['comments'] = Comment.objects.filter(post=post)
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        form = self.form

        comment = form.save(commit=False)

        if request.user.is_authenticated:
            comment.author = request.user
            comment.post = self.get_context_data()['post']
            comment.save()

            messages.success(request, 'Seu comentário foi enviado com sucesso.')
        else:
            messages.error(request, 'Você precisa estar autenticado para enviar comentários.')

        return redirect('post:detail_view', post_id=self.kwargs.get('post_id'))
