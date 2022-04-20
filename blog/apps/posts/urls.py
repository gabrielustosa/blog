from django.urls import path

from . import views

app_name = 'post'

urlpatterns = [
    path('visualizar/<int:post_id>/', views.PostDetailView.as_view(), name='detail_view'),
    path('categoria/<int:category_id>/', views.CategoryListView.as_view(), name='category_list'),
    path('criar/', views.PostCreateView.as_view(), name='create'),
    path('buscar/', views.PostSearchView.as_view(), name='search')
]
