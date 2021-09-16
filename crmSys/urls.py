from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("companies.api.urls")),
    path('api/', include("person.api.urls")),
    path('api/', include("skills.api.urls")),
    path('api/', include("user.api.urls")),
    path('api-auth', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
