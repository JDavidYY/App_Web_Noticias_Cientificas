from django.shortcuts import render, HttpResponse
#from .models import noticia




# Create your views here.

#noticias = noticia.objects.all()

#Request del home
#noticias_novedades = noticias
def home(request):
    return render(request, "core/home.html")

#Request de ciencia



