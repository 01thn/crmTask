from rest_framework.routers import DefaultRouter
from .api_views import CompaniesViewSet


router = DefaultRouter()
router.register(r'companies', CompaniesViewSet, basename='companies')
urlpatterns = router.urls

