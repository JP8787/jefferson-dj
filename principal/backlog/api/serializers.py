from rest_framework import serializers
from backlog.models import SprintHistoria

class SprintHistoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SprintHistoria
        fields = ["id", "sprint", "historia_usuario", "fecha_asignacion"]
        read_only_fields = ["id", "fecha_asignacion"]