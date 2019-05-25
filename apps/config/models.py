from django.db import models

# Create your models here.


class Estado(models.Model):
    nombre = models.CharField('Estado', max_length=40, null=False, blank=False,
                              unique=True)       


    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
        ordering = ['nombre']

    def __str__(self):
        return  '{0}'.format({self.nombre})


class Ciudad(models.Model):
    nombre = models.CharField('Ciudad', max_length=40, null=False, blank=False)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
        ordering = ['nombre', 'estado']

    def __str__(self):
        return  '{0}'.format({self.nombre})


class Region(models.Model):
    nombre = models.CharField('Región', max_length=60, null=False, blank=False,
                              unique=True)
    descripcion = models.CharField('Descripción', max_length=240, null=False,
                                   blank=True)                            


    class Meta:
        verbose_name = 'Región'
        verbose_name_plural = 'Regiones'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Zona(models.Model):
    nombre = models.CharField('Zona', max_length=60, null=False, blank=False,
                              unique=True)
    descripcion = models.TextField('Descripción', null=False,
                                   blank=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)                                 

    class Meta:
        verbose_name = 'Zona'
        verbose_name_plural = 'Zonas'
        ordering = ['nombre', 'region']

    def __str__(self):
        return self.nombre