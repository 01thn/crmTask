from rest_framework.routers import DefaultRouter
from .api_views import SkillsViewSet


router = DefaultRouter()
router.register(r'skills', SkillsViewSet, basename='skills')
urlpatterns = router.urls
