from django.shortcuts import render
from .models import Ciencia
# Create your views here.


def ciencia(request):
#    noticias_ciencia=[]
#    for noticiaaaas in noticia.objects.all():
#        if noticiaaaas.seccion=='CN':
#            noticias_ciencia.append(noticiaaaas)

    noticias_ciencia = Ciencia.objects.all()

    return render(request, "ciencia/ciencia.html", {"noticias_ciencia":noticias_ciencia})