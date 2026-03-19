from rest_framework import serializers
from backlog.models import SprintHistoria

class SprintHistoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SprintHistoria
        fields = ["id_sprint", "id_historia", "fecha_asignacion"]
        read_only_fields = ["fecha_asignacion"]