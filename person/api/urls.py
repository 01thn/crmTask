from django.urls import path

from .api_views import PersonListAPIView


urlpatterns = [
    path('person/', PersonListAPIView.as_view(), name='person')
]

