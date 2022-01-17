from django.db import models


    
class Paciente(models.Model):
    nombre= models.CharField(max_length=30)
    Apellido = models.CharField(max_length=30)  
    documento_pac = models.IntegerField()

class Medico(models.Model):
    nombre= models.CharField(max_length=30)
    Apellido = models.CharField(max_length=30)  
    Profesion = models.CharField(max_length=30)

class Practica(models.Model):
    documento_pac = models.IntegerField()
    fecha_practica= models.DateField()