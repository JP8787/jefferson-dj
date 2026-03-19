from rest_framework.routers import DefaultRouter
from backlog.api.views import SprintHistoriaViewSet

router_backlog = DefaultRouter()
router_backlog.register(prefix="sprint-historias", viewset=SprintHistoriaViewSet, basename="sprint-historias")

urlpatterns = router_backlog.urls