from django.shortcuts import render
from .models import Psicologia
# Create your views here.

def psicologia(request):
#    noticias_psicologia=[]
#    for noticiaaaas in noticia.objects.all():
#        if noticiaaaas.seccion=='ET':
#            noticias_psicologia.append(noticiaaaas)
    noticias_psicologia = Psicologia.objects.all()
    return render(request, "psicologia/psicologia.html", {"noticias_psicologia":noticias_psicologia})
