from django.contrib import admin
from .models import Ciencia

# Register your models here.
class cienciaAdmin(admin.ModelAdmin):
    readonly_fields = ("created","updated")
admin.site.register(Ciencia, cienciaAdmin)
