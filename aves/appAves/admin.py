from django.contrib import admin
from appAves.models import *
# Register your models here.
class LocalidadInline(admin.TabularInline):
    model = Ubicacion
    extra = 3


class UbicacionAdmin(admin.ModelAdmin):
    inlines = [LocalidadInline]
    list_display = ('nombre', 'provincia','pais')
    list_filter = ['provincia']
    search_fields = ['nombre']

class FamiliasAdmin(admin.ModelAdmin):
    inlines = []
    list_display = ('nombre', 'orden')
    list_filter = ['nombre']
    search_fields = ['nombre']
class AvesAdmin(admin.ModelAdmin):
    inlines = []
    list_display = ('nombre', 'especie','ecologia')
    list_filter = ['especie']
    search_fields = ['nombre']
class AutoresAdmin(admin.ModelAdmin):
    inlines = []
    list_display = ('nombre', 'source')
    list_filter = ['source']
    search_fields = ['nombre']



admin.site.register(Localidad,UbicacionAdmin)
admin.site.register(Familia,FamiliasAdmin)
admin.site.register(Autores,AutoresAdmin)
admin.site.register(Ave,AvesAdmin)
# admin.site.register(Familia)
# admin.site.register(Ubicacion)
# admin.site.register(Localidad)