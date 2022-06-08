from email.policy import default
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Volante_Tienda(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion_breve = models.TextField(max_length=300, null=False, default='En proceso')
	caracteristicas = models.TextField(max_length=300, null=False, default='En proceso')
	descripcion_larga = models.TextField(max_length=900, null=True)
	imagen = models.ImageField(blank=True, null=False, default="error404.png")
	precio = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=500)


class TipoFormula1(models.Model):
	BOTONES = (
		('8', '8'),
		('15', '15'),
	)

	LEVAS = (
		('Dos', '2'),
		('Tres', '3'),
		('Cuatro', '4'),
	)

	MATERIAL_LEVAS = (
		('Plastico', 'Plástico'),
		('Metal', 'Metal'),
	)

	ESTADO = (
		('P', 'En Produccion'),
		('E', 'Para Enviar')
	)

	botones = models.CharField(max_length=100, choices=BOTONES)
	numero_levas = models.CharField(max_length=20, choices=LEVAS, null=False)
	material_levas = models.CharField(max_length=100, choices=MATERIAL_LEVAS)
	display = models.BooleanField(default=False)
	tipo_volante = models.CharField(max_length=100, default='Formula 1 Actual')
	precio = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=400)
	estado = models.CharField(max_length=50, choices=ESTADO, default='P')

class TipoTurismo(models.Model):
	BOTONES = (
		('Ocho', '8'),
		('Catorce', '14'),
	)
	LEVAS = (
		('Cero', '0'),
		('Dos', '2'),
	)
	MATERIAL_LEVAS = (
		('Plastico', 'Plástico'),
		('Metal', 'Metal'),
	)

	ESTADO = (
		('P', 'En Produccion'),
		('E', 'Para Enviar')
	)

	TIPO_TURISMO = (
		('GT', 'Gran Turismo'),
		('Turismo', 'Turismo Redondo'),
	)

	botones = models.CharField(max_length=100, choices=BOTONES)
	numero_levas = models.CharField(max_length=20, choices=LEVAS)
	material_levas = models.CharField(max_length=100, choices=MATERIAL_LEVAS)
	display = models.BooleanField(default=False)
	precio = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=400)	
	estado = models.CharField(max_length=50, choices=ESTADO, default='P')

class TipoCamion(models.Model):
	BOTONES = (
		('Cero', '0'),
		('Cuatro', '4'),
	)
	PIEL = (
		('Cuero', 'Cuero'),
		('Alcántara', 'Alcántara'),
		('Goma', 'Goma'),
	)
	ESTADO = (
		('P', 'En Produccion'),
		('E', 'Para Enviar')
	)

	botones = models.CharField(max_length=100, choices=BOTONES)
	piel_aro = models.CharField(max_length=100, choices=PIEL)
	tipo_volante = models.CharField(max_length=100, default='Formula 1 Actual')
	intermitentes = models.BooleanField(default=False)
	luces = models.BooleanField(default=False)
	precio = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=300)	
	estado = models.CharField(max_length=50, choices=ESTADO, default='P')
	
#NECESARIO PARA UNA FK MÚLTIPLE
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Pedidos(models.Model):
	ESTADO = (
        ('P', 'En Produccion'),
        ('E', 'Para Enviar')
    )
	refF1 = models.ForeignKey(TipoFormula1, on_delete=models.CASCADE, null=True, unique=True)
	refCamion = models.ForeignKey(TipoCamion, on_delete=models.CASCADE, null=True, unique=True)
	refTurismo = models.ForeignKey(TipoTurismo, on_delete=models.CASCADE, null=True, unique=True)
	refTienda = models.ForeignKey(Volante_Tienda, on_delete=models.CASCADE, null=True)
	tipo = models.CharField(max_length=50, default='Error', null=False)
	comprador = models.CharField(max_length=100, null=False, default='usuario no encontrado')
	precio = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=500)
	estado = models.CharField(max_length=50, choices=ESTADO, null=False, default='P')
	dias_finalizar = models.CharField(max_length=3, null=True, default=30)
	
	class Meta:
		permissions = (('is_admin', 'is_admin'),)






