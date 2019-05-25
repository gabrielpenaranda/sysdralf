from django.contrib import admin
from .models import (
    Estado,
    Ciudad,
    Region,
    Zona
)
# Register your models here.


admin.site.register(Ciudad)
admin.site.register(Estado)
admin.site.register(Region)
admin.site.register(Zona)
