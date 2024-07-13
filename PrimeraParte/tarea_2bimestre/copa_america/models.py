from django.db import models

class CopaAmerica(models.Model):
    
    anio = models.IntegerField()
    sede = models.CharField(max_length=50)
    campeon = models.CharField(max_length=50)
    subcampeon = models.CharField(max_length=50)
    goleador = models.CharField(max_length=50)
    partidos_jugados = models.IntegerField()
    goles_marcados = models.IntegerField()

    def __str__(self):
        return f"Copa América {self.anio}"
