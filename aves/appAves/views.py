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
    aves = Ave.objects.all().order_by('nombre')[0:50]
    titulo= "Galeria Aves"
    diccionario = {'list_aves': aves,'titulo':titulo}
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
    autores = Autores.objects.all()


    conteo = Ave.objects.all()

    diccionario = {'lst_autores': autores, 'conteo': conteo}
    return render(request, 'top_autores.html', diccionario,
                  context_instance=RequestContext(request))


def about_view(request):
    """
    render about
    """

    return render(request, 'about.html', context_instance=RequestContext(request))
