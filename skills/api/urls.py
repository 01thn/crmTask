from django.urls import path

from .api_views import SkillsListAPIView


urlpatterns = [
    path('skills/', SkillsListAPIView.as_view(), name='skills')
]

