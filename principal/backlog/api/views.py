from rest_framework import viewsets

from backlog.api.serializers import SprintHistoriaSerializer
from backlog.models import SprintHistoria


class SprintHistoriaViewSet(viewsets.ModelViewSet):
    queryset = SprintHistoria.objects.all()
    serializer_class = SprintHistoriaSerializer
