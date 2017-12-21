from __future__ import unicode_literals
from django.db import models


# Create your models here.

class Autores(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=300,null=True)
    bibliografia = models.CharField(max_length=300,null=True)
    fecha = models.CharField(max_length=300,null=True)
    year_of_collection = models.CharField(max_length=300,null=True)
    year_of_public = models.CharField(max_length=300,null=True)
    source = models.CharField(max_length=300,null=True)
    def __unicode__(self):
        return "%s" % self.nombre
    class Meta:
        default_related_name = 'Autor'
        verbose_name_plural = "Autores"
        verbose_name = "Autor"
        db_table = 'Autores'



class Familia(models.Model):
    id_familia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=300,null=True)
    orden = models.CharField(max_length=300,null=True)
    def __unicode__(self):
        return "%s" % self.nombre
    class Meta:
        default_related_name = 'Familia'
        verbose_name_plural = "Familias"
        verbose_name = "Familia"
        db_table = 'Familia'

class Localidad(models.Model):
    id_localidad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=300,null=True)
    toponim = models.CharField(max_length=300,null=True)
    pais = models.CharField(max_length=300,null=True)
    provincia = models.CharField(max_length=300,null=True)
    def __unicode__(self):
        return "%s" % self.nombre
    class Meta:
        default_related_name = 'Localidad'
        verbose_name_plural = "Localidades"
        verbose_name = "Localidad"
        db_table = 'Localidad'

class Ubicacion(models.Model):
    id_ubicacion = models.AutoField(primary_key=True)
    cordinate = models.CharField(max_length=300,null=True)
    altitudmax = models.CharField(db_column='altitudMax', max_length=300,null=True)  # Field name made lowercase.
    altitudmin = models.CharField(db_column='altitudMin', max_length=300,null=True)  # Field name made lowercase.
    utmwgs = models.CharField(max_length=300,null=True)
    longitudy = models.CharField(db_column='longitudY', max_length=300,null=True)  # Field name made lowercase.
    latitudx = models.CharField(db_column='latitudX', max_length=300,null=True)  # Field name made lowercase.
    id_localidad = models.ForeignKey(Localidad)
    def __unicode__(self):
        return "%s" % self.cordinate
    class Meta:
        default_related_name = 'Ubicacion'
        verbose_name_plural = "Ubicaciones"
        verbose_name = "Ubicacion"
        db_table = 'Ubicacion'




class Ave(models.Model):
    id_ave = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=300,null=True)
    especie = models.CharField(max_length=300,null=True)
    synonim = models.CharField(max_length=300,null=True)
    nombre = models.CharField(max_length=300,null=True)
    morfometria = models.CharField(max_length=300,null=True)
    ecologia = models.CharField(max_length=300,null=True)
    comportamiento = models.CharField(max_length=300,null=True)
    clase = models.CharField(max_length=300,null=True)
    llamar = models.CharField(max_length=300,null=True)
    uicn = models.CharField(max_length=300,null=True)
    endemismo = models.CharField(max_length=300,null=True)
    observacion = models.CharField(max_length=300,null=True)
    migracion = models.CharField(max_length=300,null=True)
    ecosistema = models.CharField(max_length=300,null=True)
    id_autor = models.ForeignKey(Autores)
    id_familia = models.ForeignKey(Familia)
    id_ubicacion = models.ForeignKey(Ubicacion)

    def __unicode__(self):
        return "%s" % self.id_ave

    class Meta:
        default_related_name = 'Ave'
        verbose_name_plural = "Aves"
        verbose_name = "Ave"
        db_table = 'Ave'

