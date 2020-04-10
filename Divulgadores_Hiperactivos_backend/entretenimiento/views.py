from django.shortcuts import render
from .models import Entretenimiento
# Create your views here.

def entretenimiento(request):
 #   noticias_entretenimiento=[]
 #   for noticiaaaas in noticia.objects.all():
 #       if noticiaaaas.seccion=='ET':
 #           noticias_entretenimiento.append(noticiaaaas)
    noticias_entretenimiento = Entretenimiento.objects.all()
    return render(request, "entretenimiento/entretenimiento.html", {"noticias_entretenimiento":noticias_entretenimiento})