from rest_framework.routers import DefaultRouter

from backlog.api.views import SprintHistoriaViewSet


router = DefaultRouter()
router.register(r'sprint-historias', SprintHistoriaViewSet, basename='sprint-historias')

urlpatterns = router.urls
