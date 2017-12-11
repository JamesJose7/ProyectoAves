from __future__ import unicode_literals
from django.db import models


# Create your models here.

class Autores(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    bibliografia = models.CharField(max_length=200)
    fecha = models.CharField(max_length=200)
    year_of_collection = models.CharField(max_length=200)
    year_of_public = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre
    class Meta:
        default_related_name = 'Autor'
        verbose_name_plural = "Autores"
        verbose_name = "Autor"
        db_table = 'Autores'



class Familia(models.Model):
    id_familia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    orden = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre
    class Meta:
        default_related_name = 'Familia'
        verbose_name_plural = "Familias"
        verbose_name = "Familia"
        db_table = 'Familia'

class Localidad(models.Model):
    id_localidad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    toponim = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)
    provincia = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre
    class Meta:
        default_related_name = 'Localidad'
        verbose_name_plural = "Localidades"
        verbose_name = "Localidad"
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
    def __str__(self):
        return self.cordinate
    class Meta:
        default_related_name = 'Ubicacion'
        verbose_name_plural = "Ubicaciones"
        verbose_name = "Ubicacion"
        db_table = 'Ubicacion'




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
    id_familia = models.OneToOneField(Familia, unique=True)
    id_ubicacion = models.ForeignKey(Ubicacion)

    def __str__(self):
        return self.especie
    class Meta:
        default_related_name = 'Ave'
        verbose_name_plural = "Aves"
        verbose_name = "Ave"
        db_table = 'Ave'

