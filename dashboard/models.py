from django.db import models
from usuario.models import Paises

# Create your models here.

# oficinaRe = 'TABASCO'
# pais_nom = []
# pais_iso = []

# for paises_I in Paises.objects.all():
#     pais_nom.append(paises_I.nombre_pais)
#     pais_iso.append(paises_I.iso3)

# types_Puntos = [
#         ("aeropuerto", "aeropuerto"),
#         ("carretero", "carretero"),
#         ("casa de seguridad", "casa de seguridad"),
#         ("ferrocarril", "ferrocarril"),
#         ("hotel", "hotel"),
#         ("puestos a disposicion", "puestos a disposicion"),
#         ("voluntarios", "voluntarios"),
#     ]


# punto_estra = [

# ]

# types_paises = []

# for nom in pais_nom:
#     Snom = str(nom)
#     types_paises.append((Snom, Snom))



# class RPDashboar(models.Model):
#     idRescate = models.AutoField(primary_key=True)
#     fecha = models.CharField(max_length=10)
#     hora = models.CharField(max_length=5)
    
#     nombreAgente = models.CharField(max_length=300,blank=True)
#     tipo_rescate = models.CharField(max_length=22, choices=types_Puntos, default="carretero")
#     puntoEstra = models.CharField(max_length=250, blank=True)
#     nacionalidad = models.CharField(max_length=100, choices=types_paises, default=str(pais_nom[0]))
