from django.urls import path

from .api_views import UserListAPIView


urlpatterns = [
    path('user/', UserListAPIView.as_view(), name='user')
]

