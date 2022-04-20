from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.ProfileRegisterView.as_view(), name='register'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('edit/', views.ProfileEditView.as_view(), name='edit'),
]
