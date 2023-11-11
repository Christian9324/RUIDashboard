from django.db import models

# Create your models here.

class Paises(models.Model):
    idPais = models.AutoField(primary_key=True)
    nombre_pais = models.CharField(max_length=250)
    iso3 = models.CharField(max_length=3, null=True)

    def __str__(self):
        return " {id}, {pais}, {iso3}".format(id = self.idPais, pais = self.nombre_pais, iso3 = self.iso3)

class Municipios(models.Model):
    idMunicipio = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=250)
    estadoAbr = models.CharField(max_length=50)
    nomMunicipio = models.CharField(max_length=250)

    def __str__(self):
        return " {estadoAbr}, {nomMunicipio}".format(
            estadoAbr = self.estadoAbr, 
            nomMunicipio = self.nomMunicipio)

class EstadoFuerza(models.Model):
    idEdoFuerza = models.AutoField(primary_key=True)
    oficinaR = models.CharField(max_length=50)
    numPunto = models.IntegerField()
    nomPuntoRevision = models.CharField(max_length=100)
    tipoP = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=300)
    coordenadasTexto = models.CharField(max_length=300)
    latitud = models.FloatField(default=0.0)
    longitud = models.FloatField(default=0.0)
    personalINM = models.IntegerField()
    personalSEDENA = models.IntegerField()
    personalMarina = models.IntegerField()
    personalGuardiaN = models.IntegerField()
    personalOTROS = models.IntegerField()
    vehiculos = models.IntegerField()
    seccion = models.IntegerField()

    def __str__(self):
        return "{id}, {oficina}, {nomPuntoRevision} --> {tipoP}".format(id = self.idEdoFuerza, 
                                                                      oficina = self.oficinaR, 
                                                                      nomPuntoRevision = self.nomPuntoRevision[0:25], 
                                                                      tipoP = self.tipoP)


class RescatePunto(models.Model):
    idRescate = models.AutoField(primary_key=True)
    oficinaRepre = models.CharField(max_length=50)
    fecha = models.CharField(max_length=10)
    hora = models.CharField(max_length=5)
    
    nombreAgente = models.CharField(max_length=300,blank=True)

    aeropuerto = models.BooleanField(default=False)
    carretero = models.BooleanField(default=False)
    tipoVehic = models.CharField(max_length=30, blank=True)
    lineaAutobus = models.CharField(max_length=50, blank=True)
    numeroEcono = models.CharField(max_length=50, blank=True)
    placas = models.CharField(max_length=20, blank=True)
    vehiculoAseg = models.BooleanField(default=False)
    
    casaSeguridad = models.BooleanField(default=False)
    centralAutobus = models.BooleanField(default=False)
    ferrocarril = models.BooleanField(default=False)
    empresa = models.CharField(max_length=150, blank=True)
    hotel = models.BooleanField(default=False)
    nombreHotel = models.CharField(max_length=100, blank=True)
    
    puestosADispo = models.BooleanField(default=False)
    juezCalif = models.BooleanField(default=False)
    reclusorio = models.BooleanField(default=False)
    policiaFede = models.BooleanField(default=False)
    dif = models.BooleanField(default=False)
    policiaEsta = models.BooleanField(default=False)
    policiaMuni = models.BooleanField(default=False)
    guardiaNaci = models.BooleanField(default=False)
    fiscalia = models.BooleanField(default=False)
    otrasAuto = models.BooleanField(default=False)

    voluntarios = models.BooleanField(default=False)
    otro = models.BooleanField(default=False)
    presuntosDelincuentes = models.BooleanField(default=False)
    numPresuntosDelincuentes = models.IntegerField()
    municipio = models.CharField(max_length=200, blank=True)
    puntoEstra = models.CharField(max_length=250, blank=True)
    
    nacionalidad = models.CharField(max_length=100)
    iso3 = models.CharField(max_length=3)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=150)
    noIdentidad = models.CharField(max_length=50)
    parentesco = models.CharField(max_length=50, blank=True)
    fechaNacimiento = models.CharField(max_length=10)
    sexo = models.BooleanField(default=False)
    embarazo = models.BooleanField(default=False)
    numFamilia = models.IntegerField(blank=True)
    edad = models.IntegerField()

    def __str__(self):
        tipoE = ""
        tipo= ""
        if(self.edad > 18):
            tipoE = "A"
        else:
            tipoE = "NNA"

        if(self.aeropuerto):
            tipo = "aeropuerto"
        elif(self.carretero):
            tipo= "carretero"
        elif(self.casaSeguridad):
            tipo= "Casa de Seguridad"
        elif(self.centralAutobus):
            tipo= "Central de Autobús"
        elif(self.ferrocarril):
            tipo= "Ferrocarril"
        elif(self.hotel):
            tipo= "Hotel"
        elif(self.puestosADispo):
            tipo= "Puestos a Disposición"
        elif(self.voluntarios):
            tipo= "Voluntarios"
        elif(self.otro):
            tipo= "Otro"
        else:
            tipo = ""
        return "{id}.- OR: {oficinaRepre}, Fecha: {fecha} {hora}, Tipo: {tipo} --> {iso3}, {tipoE}".format(id = self.idRescate, 
                                                                      oficinaRepre = self.oficinaRepre, 
                                                                      fecha = self.fecha, 
                                                                      hora = self.hora, 
                                                                      tipo = tipo, 
                                                                      iso3 = self.iso3, 
                                                                      tipoE = tipoE)