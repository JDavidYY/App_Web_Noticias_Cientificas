from django.contrib import admin
from .models import Entretenimiento
# Register your models here.
class entretenimientoAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(Entretenimiento, entretenimientoAdmin)