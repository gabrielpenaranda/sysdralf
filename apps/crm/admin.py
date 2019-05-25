from django.contrib import admin
from .models import (
    Persona,
    TipoActividad,
    Actividad
)
# Register your models here.

admin.site.register(TipoActividad)
admin.site.register(Actividad)
admin.site.register(Persona)

