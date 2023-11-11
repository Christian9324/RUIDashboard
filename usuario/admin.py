from django.contrib import admin
from .models import RescatePunto, Paises, EstadoFuerza, Municipios
# Register your models here.

admin.site.register(RescatePunto)
admin.site.register(Paises)
admin.site.register(EstadoFuerza)
admin.site.register(Municipios)
