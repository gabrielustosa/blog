from django.urls import path

from . import views

app_name = 'post'

urlpatterns = [
    path('view/<int:post_id>/', views.PostDetailView.as_view(), name='detail_view'),
]
