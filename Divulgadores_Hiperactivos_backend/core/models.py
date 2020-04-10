from django.db import models

# Create your models here.

#class noticia(models.Model):
#    titulo = models.CharField(max_length=200)
#    imagen = models.ImageField(upload_to="imagenes_noticias")
#    Noticia = models.TextField(verbose_name="Redacción")
#    link = models.URLField(verbose_name="URL")
#    created = models.DateTimeField(auto_now_add=True, verbose_name="Creación")
#    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")


#Haciendo choices
#    CIENCIA = 'CN'
#    CULTURA = 'CT'
#    ENTRETENIMIENTO = 'ET'
#    PSICOLOGIA = 'PS'
#    SECCION = (
#        (CIENCIA, 'Ciencia'),
#        (CULTURA, 'Cultura'),
#        (ENTRETENIMIENTO, 'Entretenimiento'),
#        (PSICOLOGIA, 'Psicología'),
#    )
#    seccion = models.CharField(
#        max_length=2,
#        choices=SECCION,
#        default=CIENCIA,
#    )
    
#    class Meta:
#        verbose_name="Noticia"
#        verbose_name_plural="Noticias"
#        ordering = ["-created"]
#    def __str__(self):
#        return self.titulo

