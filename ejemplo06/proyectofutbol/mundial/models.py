from django.db import models

# Create your models here.
class Estadios(models.Model):
    nombre = models.CharField(max_length=60)
    capacidad = models.IntegerField()


    def __str__(self):
        return "%s - capacidad: %d" % (self.nombre, 
                self.capacidad)

class Equipos(models.Model):
    siglas = models.CharField(max_length=15)
    nombre = models.CharField(max_length=60)
    sobrenombre = models.CharField(max_length=60)


    def __str__(self):
        return "%s - %s - %s " % (self.siglas, 
                self.nombre,
                self.sobrenombre)
