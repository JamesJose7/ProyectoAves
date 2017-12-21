from django.shortcuts import render
from django.template import RequestContext

from appAves.models import *


def index(request):
    """
    """
    diccionario = {'saludo': "Hola Mundo"}
    return render(request, 'index.html', diccionario,
        context_instance=RequestContext(request))


def listado_aves(request):
    """
        obtengo las aves
    """
    aves = Ave.objects.all()
    diccionario = {'list_aves': aves}
    return render(request, 'listado_aves.html', diccionario,
        context_instance=RequestContext(request))
#
# def materia(request, id):
#     """
#         obtengo las materias
#     """
#     materia = Ave.objects.get(pk=id)
#     numero_paralelos = Ave.objects.filter(la_materia=materia).count()
#     numero_estudiantes = Estudiante.objects.filter(
#             paraleloestudiante__la_paralelo__la_materia=materia).count()
#     diccionario = {'materia': materia, 'numero_paralelos': numero_paralelos,
#                    'mensaje': 'Mensaje de la pantalla',
#                    'numero_estudiantes': numero_estudiantes}
#     return render(request, 'materia.html', diccionario,
#                   context_instance=RequestContext(request))
#
