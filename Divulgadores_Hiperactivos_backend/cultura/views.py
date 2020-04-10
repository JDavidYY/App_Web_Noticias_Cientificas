from django.shortcuts import render
from .models import Cultura
# Create your views here.

def cultura(request):
#    noticias_cultura=[]
#    for noticiaaaas in noticia.objects.all():
#        if noticiaaaas.seccion=='CT':
#            noticias_cultura.append(noticiaaaas)
    noticias_cultura = Cultura.objects.all()
    return render(request, "cultura/cultura.html", {"noticias_cultura": noticias_cultura})
