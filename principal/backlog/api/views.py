from rest_framework.viewsets import ModelViewSet
from backlog.models import SprintHistoria
from backlog.api.serializers import SprintHistoriaSerializer

class SprintHistoriaViewSet(ModelViewSet):
    queryset = SprintHistoria.objects.all()
    serializer_class = SprintHistoriaSerializer