from django.db import models

class Sprint(models.Model):
    id_sprint = models.IntegerField(primary_key=True)

    class Meta:
        managed = False          # la tabla ya existe
        db_table = "sprint"

class HistoriaUsuario(models.Model):
    id_historia = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = "historia_usuario"

class SprintHistoria(models.Model):
    id = models.AutoField(primary_key=True)  # surrogate PK sencilla
    sprint = models.ForeignKey(Sprint, on_delete=models.DO_NOTHING, db_column="id_sprint")
    historia_usuario = models.ForeignKey(HistoriaUsuario, on_delete=models.DO_NOTHING, db_column="id_historia")
    fecha_asignacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False          # usamos la tabla existente
        db_table = "sprint_historia"
        unique_together = ("sprint", "historia_usuario")