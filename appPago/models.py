from django.db import models
# Importamos el modelo de otra APP
from appCliente.models import *
from datetime import datetime
# Create your models here.

class Pago(models.Model):
    f_ini_pago = models.DateField()
    f_exp_pago = models.DateField()
    comentario_pago = models.CharField(max_length=100,null=True, blank=True)
    # on_delete=models.SET_NULL pone null el campo
    # on_delete=models.CASCADE,null=true,blank=true borra el registro
    # on_delete=models.Protected No permite que el principal sea borrado
    # Relación 1 a muchos
    fk_cli_pago = models.ForeignKey(Cliente, verbose_name= 'pago del cliente', on_delete=models.CASCADE)
    # Relación muchos a muchos, si desea agregar mas campos a la tabla es mejor crear la tabla y relacionarla
    # fk_m_m = models.models.ManyToManyField(ModeloRelacionado, verbose_name=_(""))
    def __str__(self):
        return self.f_exp_pago
    class Meta:
        db_table = 'pago'
        ordering = ['id']
        verbose_name = 'pago'
        verbose_name_plural = 'pagos'
    