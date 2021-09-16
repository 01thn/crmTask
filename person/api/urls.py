from rest_framework.routers import DefaultRouter
from .api_views import PersonViewSet


router = DefaultRouter()
router.register(r'person', PersonViewSet, basename='person')
urlpatterns = router.urls