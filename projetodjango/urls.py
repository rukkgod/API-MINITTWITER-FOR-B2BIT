from django.urls import path
from api.views import UserRegistrationAPIView, PostCreateAPIView, PostListAPIView

urlpatterns = [
    path('users/register/', UserRegistrationAPIView.as_view(), name='user-registration'),
    path('posts/create/', PostCreateAPIView.as_view(), name='post-create'),
    path('posts/', PostListAPIView.as_view(), name='post-list'),
]
