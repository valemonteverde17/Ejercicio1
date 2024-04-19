from django.db import models

# Create your models here.
class Transporte(models.Model):
    tipo = models.CharField(max_length=30)
    placa = models.CharField(max_length=30)
    marca =  models.CharField(max_length=30)
    capacidad = models.IntegerField()
    fecha_creado = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.tipo}-{self.placa}-{self.fecha_creado}"
        