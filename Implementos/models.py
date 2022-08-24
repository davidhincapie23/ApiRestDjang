from django.db import models

class Balones(models.Model):
    nombre = models.CharField (max_length=50)
    marca = models.CharField(max_length=50)
    numero = models.IntegerField()
    precio = models.IntegerField()
    creado = models.DateTimeField(auto_now_add=True)
    editado = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.nombre
    

