from django.db import models

# Create your models here.


class Vendedor(models.Model):
    nombre = models.CharField('Nombre', max_length=80, null=False, blank=False)
    apellidos = models.CharField('Apellidos', max_length=80, null=False,
                                 blank=False)
    cedula = models.CharField('Cédula de Identidad', max_length=12, null=False,
                              blank=False)
    direccion = models.CharField('Dirección', max_length=120, null=False,
                                 blank=False)
    telefonos = models.CharField('Teléfonos', max_length=12, null=False,
                                 blank=False)

    class Meta:
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'
        ordering = ['apellidos', 'nombre']

    def __str__(self):
        return '{0}, {1}'.format({self.apellidos}, {self.nombre})