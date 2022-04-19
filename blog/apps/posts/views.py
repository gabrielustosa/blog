from django.views.generic import TemplateView

from blog.apps.posts.models import Post


class PostDetailView(TemplateView):
    template_name = 'post/detail_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_id = self.kwargs.get('post_id')
        context['post'] = Post.objects.get(id=post_id)
        return context
