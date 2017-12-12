# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Autores(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    bibliografia = models.CharField(max_length=200)
    fecha = models.DateField()
    year_of_collection = models.CharField(max_length=200)
    year_of_public = models.CharField(max_length=200)
    source = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'Autores'


class Ave(models.Model):
    id_ave = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=200)
    especie = models.CharField(max_length=200)
    synonim = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    morfometria = models.CharField(max_length=200)
    ecologia = models.CharField(max_length=200)
    comportamiento = models.CharField(max_length=200)
    clase = models.CharField(max_length=200)
    llamar = models.CharField(max_length=200)
    uicn = models.CharField(max_length=200)
    endemismo = models.CharField(max_length=200)
    observacion = models.CharField(max_length=200)
    migracion = models.CharField(max_length=200)
    ecosistema = models.CharField(max_length=200)
    id_autor = models.ForeignKey(Autores)
    id_bibliografia_id = models.IntegerField()
    id_familia = models.ForeignKey('Familia', unique=True)
    id_ubicacion = models.ForeignKey('Ubicacion')

    def __unicode__(self):
        # return "%s" % self.id_ave
        return "s"

    class Meta:
        managed = False
        db_table = 'Ave'


class Familia(models.Model):
    id_familia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    orden = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'Familia'


class Localidad(models.Model):
    id_localidad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    toponim = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)
    provincia = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'Localidad'


class Ubicacion(models.Model):
    id_ubicacion = models.AutoField(primary_key=True)
    cordinate = models.CharField(max_length=200)
    altitudmax = models.CharField(db_column='altitudMax', max_length=200)  # Field name made lowercase.
    altitudmin = models.CharField(db_column='altitudMin', max_length=200)  # Field name made lowercase.
    utmwgs = models.CharField(max_length=200)
    longitudy = models.CharField(db_column='longitudY', max_length=200)  # Field name made lowercase.
    latitudx = models.CharField(db_column='latitudX', max_length=200)  # Field name made lowercase.
    id_localidad = models.ForeignKey(Localidad)

    class Meta:
        managed = False
        db_table = 'Ubicacion'
