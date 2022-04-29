from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView

from blog.apps.comments.form import CommentForm
from blog.apps.pages.views import HomeView
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
        post = Post.published.get(id=post_id)
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


class PostCreateView(CreateView):
    template_name = 'post/create.html'
    model = Post
    fields = ('title', 'content', 'description', 'category', 'image', 'is_published')
    success_url = reverse_lazy('page:home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)


class PostSearchView(HomeView):
    def get_queryset(self, **kwargs):
        query = super().get_queryset()
        term = self.request.GET.get('term') or self.request.session['term']

        if not term:
            return query

        self.request.session['term'] = term

        self.request.session.save()
        query = Post.published.filter(
            title__icontains=term
        )
        return query


class CategoryListView(HomeView):
    def get_queryset(self, **kwargs):
        category_id = self.kwargs.get('category_id')
        query = Post.published.filter(
            category__id=category_id
        )
        return query


class PostManageView(ListView):
    template_name = 'post/manage.html'
    model = Post
    paginate_by = 6
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


class EditPostView(UpdateView):
    template_name = 'post/edit.html'
    model = Post
    fields = ('title', 'content', 'description', 'category', 'image', 'is_published')
    success_url = reverse_lazy('post:manage')

    def dispatch(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author != self.request.user:
            raise Http404()
        return super().dispatch(request, *args, **kwargs)


class DeletePostView(DeleteView):
    template_name = 'post/delete.html'
    model = Post
    success_url = reverse_lazy('post:manage')

    def dispatch(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author != self.request.user:
            raise Http404()
        return super().dispatch(request, *args, **kwargs)
