from django.views.generic import ListView

from blog.apps.posts.models import Post


class HomeView(ListView):
    template_name = 'pages/home.html'
    model = Post
    paginate_by = 6
    context_object_name = 'posts'
