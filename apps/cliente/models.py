from django.db import models
from apps.config.models import (
    Ciudad,
    Zona,
    )
from apps.venta.models import Vendedor


# Create your models here.


class Cliente(models.Model):
    nombre = models.CharField('Nombre', max_length=80, null=False, blank=False)
    razon_social = models.CharField('Razón Social', max_length=80, null=False, blank=False)
    rif = models.CharField('RIF', max_length=12, null=False, blank=False)
    direccion = models.CharField('Dirección', max_length=120, null=False, blank=False)
    ciudad = models.ForeignKey(Ciudad, related_name='clientes', on_delete=models.CASCADE)
    zona = models.ForeignKey(Zona, on_delete=models.SET_DEFAULT, default=0)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.SET_DEFAULT, default=0)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre + ' ' + self.rif