from django.db import models


class Sprint(models.Model):
	id = models.BigAutoField(primary_key=True)

	class Meta:
		managed = False
		db_table = 'sprint'


class HistoriaUsuario(models.Model):
	id = models.BigAutoField(primary_key=True)

	class Meta:
		managed = False
		db_table = 'historia_usuario'


class SprintHistoria(models.Model):
	sprint = models.ForeignKey(Sprint, on_delete=models.DO_NOTHING)
	historia_usuario = models.ForeignKey(HistoriaUsuario, on_delete=models.DO_NOTHING)
	pk = models.CompositePrimaryKey('sprint', 'historia_usuario')

	class Meta:
		managed = False
		db_table = 'sprint_historia'
