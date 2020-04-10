from django.contrib import admin
from .models import Cultura

# Register your models here.

class culturaAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
admin.site.register(Cultura, culturaAdmin)