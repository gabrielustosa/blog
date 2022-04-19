from django.views.generic import TemplateView

from blog.apps.posts.models import Post


class HomeView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(is_published=True)
        return context
