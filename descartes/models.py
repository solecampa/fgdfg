from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Guia(models.Model):
    guia = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.guia}"
    
class Filtro(models.Model):
    filtro = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.filtro}"

class Tecnico(models.Model):
    nombre = models.CharField(max_length=64)
    iniciales = models.CharField(max_length=3, unique=True)
    def __str__(self):
        return f"{self.nombre}-{self.iniciales}"

class Motivo(models.Model):
    motivo = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.motivo}"


class Descartes(models.Model):
    PRODUCTO = [
    ('MIV', 'Mezcla intra Venosa'),
    ('MNPE', 'Mezcla de Nutricion Parenteral Extemporanea'),
    ]
    LINEA = [
    ('B', 'Blanca'),
    ('V', 'Verde'),
    ('A', 'Amarilla'),
    ('C', 'Celeste'),
    ('R', 'Rosa'),
    ('N/A', 'No aplica'),
    ]
    fecha = models.DateField()
    producto = models.CharField(max_length=64, choices=PRODUCTO, default='MNPE')
    lote = models.CharField(max_length=64)
    motivo = models.ForeignKey(Motivo, on_delete=models.PROTECT)
    tecnico = models.ForeignKey(Tecnico, on_delete=models.PROTECT)
    volumen = models.IntegerField()
    guia = models.ForeignKey(Guia, on_delete=models.PROTECT, blank=True)
    filtro = models.ForeignKey(Filtro, on_delete=models.PROTECT, blank=True)
    observaciones = models.CharField(max_length=64, blank=True, null=True)
    borrado = models.BooleanField(default=False) 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    linea = models.CharField(max_length=64, choices=LINEA, default='N/A')
    
    def __str__(self):
        return f"{self.fecha}-{self.producto}-{self.lote}-{self.motivo}"