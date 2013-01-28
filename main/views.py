from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from main.models import pelicula

def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))


def peliView(request, nombrepeli = None):
    #raise Exception(nombrepeli)

    if nombrepeli:
        #TODO get movie or none
        #peli = get_pelicula()pelicula.objects.get(titulo=nombrepeli)
        peli = pelicula.objects.get(titulo=nombrepeli)
        if peli:
            return render_to_response('pelicula.html', { 'Pelicula' : peli, }, context_instance=RequestContext(request))
        else:
            resp = "<html><head></head><body><h1>No se encontro la pelicula buscada %s.</h1></body></html>" % nombrepeli
            return HttpResponse(resp)
    else:
        return render_to_response('pelicula.html', context_instance=RequestContext(request))

def peliculasView(request):
    return render_to_response('peliculas.html', context_instance=RequestContext(request))

def user(request, NombrePelicula):
    Nombreusuario = str(NombrePelicula)
    if NombrePelicula:
        resp = "<html><head></head><body><p>Pelicula: %s</p></body></html>" % (Nombreusuario)
        return HttpResponse(resp)
    else:
        resp = "<html><head></head><body><p>Peliculas index%s</p></body></html>" % (Nombreusuario)
        return HttpResponse(resp)
		
#TODO get the movie or return none
"""
def get_pelicula(arg)
"""