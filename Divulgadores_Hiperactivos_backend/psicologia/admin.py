from django.contrib import admin
from .models import Psicologia

# Register your models here.
class psicologiaAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(Psicologia, psicologiaAdmin)