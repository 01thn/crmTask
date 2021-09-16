from rest_framework.routers import DefaultRouter
from .api_views import UserModelViewSet


router = DefaultRouter()
router.register(r'user', UserModelViewSet, basename='user')
urlpatterns = router.urls

