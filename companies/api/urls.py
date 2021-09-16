from django.urls import path

from .api_views import CompaniesListAPIView


urlpatterns = [
    path('companies/', CompaniesListAPIView.as_view(), name='companies')
]

