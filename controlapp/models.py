# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    rut_cliente = models.CharField(max_length=15, blank=True, null=True)
    nombre_cliente = models.CharField(max_length=50, blank=True, null=True)
    apellido_cliente = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class LogsMaquina(models.Model):
    id_log = models.AutoField(primary_key=True)
    id_maquina = models.IntegerField(blank=True, null=True)
    log_temp_celda = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logs_maquina'


class Maquina(models.Model):
    id_maquina = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    key_maquina = models.CharField(max_length=15, blank=True, null=True)
    ip_maquina = models.CharField(max_length=15, blank=True, null=True)
    nserie_maquina = models.CharField(max_length=15, blank=True, null=True)
    modelo_maquina = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maquina'


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=50, blank=True, null=True)
    apellido_usuario = models.CharField(max_length=50, blank=True, null=True)
    tipo_usuario = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'
