from rest_framework import serializers

from backlog.models import HistoriaUsuario, Sprint, SprintHistoria


class SprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprint
        fields = '__all__'


class HistoriaUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoriaUsuario
        fields = '__all__'


class SprintHistoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SprintHistoria
        fields = '__all__'
