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
    aves = Ave.objects.all().order_by('nombre')[0:50]
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


def top_autores(request):
    """
    obtengo el top 10 de autores con mas publicaciones
    """
    titulo = "Top 10 Autores con mas publicaciones"
    autores = Autores.objects.all().values('nombre')[:10]
    conteo = Ave.objects.all().values('id_autor')[:10].annotate(Count("id_autor_id"))
    # autores_aux = json.dumps([{'autor': o.nombre} for o in autores])


    # autor_count = {}
    # for autor in autores:
    #     autor_count[autor.nombre] = 0
    #
    # for cont in conteo:
    #     for autor in autores:
    #         if cont.nombre == autor.nombre:
    #             autor_count[autor.nombre] = autor_count[autor.nombre] + 1
    #             print()


    diccionario = {'lst_autores': autores,"conteo":conteo,"titulo":titulo}
    return render(request, 'top_autores.html', diccionario,
              context_instance=RequestContext(request))

@csrf_exempt
def top_autores_view(request):
    """
    """
    if request.is_ajax() == True:
        req = {}
        letra = request.POST.getlist('valor')[0]
        autores = Autores.objects.all().values('nombre')[:10]
        conteo = Ave.objects.all().values('id_autor')[:10].annotate(Count("id_autor_id"))

        req['mensaje'] = 'Correcto .... cargando datos '
        req['autores'] = {'results':list(autores)}
        req['values'] = {'values':list(conteo)}

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
    data = {
        "personas":20,
        "alumnos":120,
    }

    data_lugares = lugares.objects.all()
    data_lugares = serializers.serialize('json',data_lugares)
    return HttpResponse(data_lugares,content_type="application/json")
