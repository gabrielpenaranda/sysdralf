from django.db import models
from apps.cliente.models import Cliente
# Create your models here.



class TipoActividad(models.Model):
    nombre = models.CharField('Nombre', max_length=80, null=False, blank=False)
    descripcion = models.TextField('Descripción')
    
    class Meta:
        verbose_name = 'Tipo de Actividad'
        verbose_name_plural = 'Tipos de Actividad'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
    

class Actividad(models.Model):
    descripcion = models.TextField('Descripción')
    accion = models.TextField('Acciones')
    fecha = models.DateField('Fecha', null = False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoActividad, default=0, on_delete=models.SET_DEFAULT)
    
    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'
        ordering = ['fecha', 'cliente', 'tipo']

    def __str__(self):
        return '{0}, {1}, {2}'.format({self.fecha}, {self.cliente}, {self.tipo})


class Persona(models.Model):
    nombre = models.CharField('Nombre', max_length=80, null=False, blank=False)
    apellidos = models.CharField('Nombre', max_length=80, null=False, blank=False)
    cargo = models.CharField('Nombre', max_length=80, null=False, blank=False)
    telefono = models.CharField('Nombre', max_length=80, null=False, blank=False)
    celular = models.CharField('Nombre', max_length=80, null=False, blank=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
        ordering = ['apellidos', 'nombre'] 

    def __str__(self):
        return self.apellidos + ', ' + self.nombre
    
        

