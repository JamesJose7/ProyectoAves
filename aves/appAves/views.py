from django.shortcuts import render
from django.template import RequestContext
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from appAves.models import *
from django.core import serializers
import json


def index(request):
    """
    """
    diccionario = {'saludo': "Hola Mundo"}
    return render(request, 'index.html', diccionario,
                  context_instance=RequestContext(request))


def mapa_view(request):
    lugaresOBJ = lugares.objects.all()
    diccionario = {'lugares': lugaresOBJ}
    return render(request, 'mapa.html', diccionario,
                  context_instance=RequestContext(request))


def listado_aves(request):
    """
        obtengo las aves
    """
    aves = Ave.objects.all().order_by('nombre')[:50]
    titulo = "Galeria Aves"
    diccionario = {'list_aves': aves, 'titulo': titulo}
    return render(request, 'listado_aves.html', diccionario,
                  context_instance=RequestContext(request))


def ave(request, id):
    """
        obtengo las aves
    """
    ave = Ave.objects.get(pk=id)

    diccionario = {'ave': ave}
    return render(request, 'ave.html', diccionario,
                  context_instance=RequestContext(request))


def autor(request, id):
    """
        obtengo un autor en especifico
    """
    autor = Autores.objects.get(pk=id)

    diccionario = {'autor': autor}
    return render(request, 'autor.html', diccionario,
                  context_instance=RequestContext(request))


def estadisticas(request):
    """
    obtengo el top 10 de autores con mas publicaciones
    """
    titulo = "Estadisticas"
    autores = Autores.objects.all().values('nombre')[:10]
    conteo = Ave.objects.all().values('id_autor')[:10].annotate(Count("id_autor_id"))
    diccionario = {'lst_autores': autores, "conteo": conteo, "titulo": titulo}
    return render(request, 'estadisticas.html', diccionario,
                  context_instance=RequestContext(request))


def trabajos_relacionados(request, id):
    """
    obtengo los trabajos relacionados del autor
    """
    aves = Ave.objects.filter(id_autor_id=id)
    titulo = "Trabajos relacionados"
    diccionario = {'list_aves': aves, 'titulo': titulo}
    return render(request, 'listado_aves.html', diccionario,
                  context_instance=RequestContext(request))


@csrf_exempt
def top_autores_view(request):
    """
    """
    if request.is_ajax() == True:
        req = {}
        autores = Autores.objects.all().values('nombre')[:10]
        conteo = Ave.objects.all().values('id_autor')[:10].annotate(Count("id_autor_id"))

        req['mensaje'] = 'Correcto .... cargando datos '
        req['autores'] = {'results': list(autores)}
        req['values'] = {'values': list(conteo)}

    return JsonResponse(req, safe=False)


@csrf_exempt
def uicn_view(request):
    """
    """
    if request.is_ajax() == True:
        req = {}
        conteo = Ave.objects.all().values('uicn').annotate(Count('uicn'))
        req['mensaje'] = 'Correcto .... cargando datos '
        req['values'] = {'values': list(conteo)}

    return JsonResponse(req, safe=False)


def about_view(request):
    """
    render about
    """
    return render(request, 'about.html', context_instance=RequestContext(request))


def sacar_data(request):
    """
    sacar data
    """

    data = Ave.objects.all()[:10]
    data = serializers.serialize('json',data)
    return HttpResponse(data,content_type="application/json")

