from django.db import models

class Sprint(models.Model):
    id_sprint = models.IntegerField(primary_key=True)

    class Meta:
        managed = False         
        db_table = "sprint"

class HistoriaUsuario(models.Model):
    id_historia = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = "historia_usuario"

class SprintHistoria(models.Model):
    id_sprint = models.IntegerField(primary_key=True)
    id_historia = models.IntegerField()
    fecha_asignacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False         
        db_table = "sprint_historia"
        unique_together = ("id_sprint", "id_historia")