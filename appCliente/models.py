from django.db import models
from datetime import datetime
# Create your models here.
# Elegibles
sexo_opciones = (
    ('hombre','hombre'),
    ('mujer','mujer'),
)
# Elegibles 2
tipo_opciones = (
    ('diario','Diario'),
    ('mensual','Mensual'),
    ('especial','Especial'),
)

class Cliente(models.Model):
    ci_cli = models.CharField(max_length=10, unique=True, verbose_name='CI')
    apellido_cli = models.CharField(max_length=30, verbose_name='Apellido')
    nombre_cli = models.CharField(max_length=30, verbose_name='Nombre')
    num_cell_cli = models.CharField(max_length=9, null=True, blank=True, verbose_name='Celular')
    sexo_cli = models.CharField(max_length=7,choices=sexo_opciones,default='hombre', verbose_name='Sexo')
    tipo_cli = models.CharField(max_length=9,choices=tipo_opciones, default='diario', verbose_name='Tipo cliente')
    f_created = models.DateField(default=datetime.now, verbose_name='Registrado el')
    # DateField->Fecha DateTimeField->Fecha y Hora
    # auto_now=True -> Solo se crea la primera vez
    # auto_now_add=True -> Cada que se modifique
    # Enteros models.integerField(default=0)
    # Enteros positivos models.PositiveIntegerField(default=0)
    # Decimales models.DecimalField(default=0.00,max_digits=9,decimal_places=2)
    # Bool models.BooleanField(default=False)
    # imagenes = models.ImageField(upload_to='nombre_carpeta', height_field=None, width_field=None, max_length=None)
    # doc = models.FileField(upload_to='nombre_carpeta', max_length=100)

    # Crear el metodo STR
    def __str__(self):
        nombres =self.apellido_cli+' '+self.nombre_cli 
        return nombres
    # Definimos el meta
    class Meta:
        db_table = 'cliente'
        # Como nos va a ordenar la tabla al momento de llamar
        ordering = ['f_created']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Cliente'
    