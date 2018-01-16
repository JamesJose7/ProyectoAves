from django.shortcuts import render
from django.template import RequestContext

from appAves.models import *


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
    aves = Ave.objects.all()
    diccionario = {'list_aves': aves}
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

