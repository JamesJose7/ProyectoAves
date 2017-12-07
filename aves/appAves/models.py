from __future__ import unicode_literals
from django.db import models


# Create your models here.
#Familia
class familia(models.Model):
    id_familia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    orden = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'familia'

    def __unicode__(self):
        return "%s - %s - %s" % (self.id_familia, self.nombre, self.orden)

#Autor
class autor(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'autor'

    def __unicode__(self):
        return "%s - %s" % (self.id_autor, self.nombre)

#Bibliografia
class bibliografia(models.Model):
  id_bilbiografia = models.AutoField(primary_key=True)
  bibliografia = models.TextField()

  class Meta:
        managed = False
        db_table = 'bibliografia'

  def __unicode__(self):
        return "%s - %s" % (self.id_bilbiografia, self.bibliografia)

#Migracion
class migracion(models.Model):
    id_migracion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'migracion'

    def __unicode__(self):
        return "%s - %s" % (self.id_migracion, self.nombre)

#UICN
class uicn(models.Model):
    id_familia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'uicn'

    def __unicode__(self):
        return "%s - %s" % (self.id_familia, self.nombre)

#Endemismo
class endemismo(models.Model):
    id_endemismo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'endemismo'

    def __unicode__(self):
        return "%s - %s" % (self.id_endemismo, self.nombre)

#Ubicacion
class ubicacion(models.Model):
    id_ubicacion = models.AutoField(primary_key=True)
    pais = models.CharField(max_length=200)
    provincia = models.CharField(max_length=200)
    localidad = models.CharField(max_length=200)
    toponim = models.CharField(max_length=200)
    longitud = models.CharField(max_length=200)
    latitud = models.CharField(max_length=200)
    gps = models.CharField(max_length=200)
    latitudMax = models.CharField(max_length=200)
    latitudMin = models.CharField(max_length=200)
    id_ave = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'ubicacion'

    def __unicode__(self):
        return "%s - %s - %s - %s - %s - %s - %s - %s - %s - %s - %s" % (self.id_ubicacion, self.pais, self.provincia, self.localidad,
                           self.toponim, self.longitud, self.latitud, self.gps, self.latitudMax,
                           self.latitudMin, self.id_ave)

# Tabla aves
class ave(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=200)
    especie = models.CharField(max_length=200)
    synonim = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    morfometres = models.CharField(max_length=200)
    ecology = models.CharField(max_length=200)
    behaviour = models.CharField(max_length=200)
    yearPublished = models.CharField(max_length=200)
    yearCollection= models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    call = models.CharField(max_length=200)
    observacion = models.CharField(max_length=200)
    id_familia = models.OneToOneField(familia)
    id_endemismo = models.OneToOneField(endemismo)
    id_migracion = models.OneToOneField(migracion)
    id_autor = models.ForeignKey(autor)
    id_bibliografia = models.ForeignKey(bibliografia)
    id_ubicacion = models.ForeignKey(ubicacion)

    class Meta:
        managed = False
        db_table = 'ave'

    def __unicode__(self):
        return "%s - %s - %s - %s - %s - %s - %s - %s - %s - %s - %s - %s - %s - %s - %s - %s - %s - %s" % (self.id, self.codigo, self.especie, self.synonim, self.nombre, self.morfometres, self.ecology, self.ecology, self.behaviour, self.yearPublished, self.yearCollection, self.date, self.call, self.observacion, self.id_familia, self.id_endemismo, self.id_migracion, self.id_autor, self.id_bibliografia)
