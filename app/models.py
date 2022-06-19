from email.policy import default
from urllib import request
from django.db import models
from django.contrib.auth.models import User

#TARJETA
class TarjetaCredito(models.Model):
	TIPOS_TARJETA = (
		('MasterCard', 'Mastercard'),
		('VISA', 'VISA'),
	)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	tarjeta_credito = models.CharField(max_length=100, null=False, choices=TIPOS_TARJETA)
	num_tarjeta = models.CharField(max_length=16, null=False)
	fecha_caducidad = models.CharField(max_length=100, null=False)
	codigo_seguridad = models.CharField(null=False, max_length=3)

class Direccion(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	direccion = models.CharField(max_length=100, null=False, default="C/")
	puerta = models.CharField(max_length=100, null=False, default='Puerta no introducida')
	piso = models.CharField(max_length=10, null=True, blank=True)
	ciudad = models.CharField(max_length=100, null=False, default='Ciudad no introducida')
	provincia = models.CharField(max_length=100, null=False, default='Provincia no introducida')
	

# USUARIO DATOS
class UsuarioDatos(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	metodo_pago = models.ManyToManyField(TarjetaCredito, max_length=100, null=True, blank=True)
	direccion = models.ManyToManyField(Direccion, max_length=100, null=True, blank=True)
 

class Volante_Tienda(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion_breve = models.TextField(max_length=300, null=False, default='En proceso')
	año = models.CharField(max_length=4, null=True)
	info_coche = models.TextField(max_length=900, null=True)
	imagen = models.ImageField(blank=True, null=False, default="error404.png")
	stock = models.IntegerField(null=False, default=0)
	precio = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=500)


class TipoFormula1(models.Model):
	BOTONES = (
		('8', '8 [+50€]'),
		('15', '15 [+100€]'),
	)

	LEVAS = (
		('Dos', '2 [+50€]'),
		('Tres', '3[+150€]'),
		('Cuatro', '4 [+200€]'),
	)

	MATERIAL_LEVAS = (
		('Plastico', 'Plástico [+0€]'),
		('Metal', 'Metal [+50€]'),
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
		('Ocho', '8 [+100€]'),
		('Catorce', '14 [+170€]'),
	)
	LEVAS = (
		('Cero', '0 [+0€]'),
		('Dos', '2 [+100€]'),
	)
	MATERIAL_LEVAS = (
		('Plastico', 'Plástico [+0€]'),
		('Metal', 'Metal [+50€]'),
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
	material_levas = models.CharField(max_length=100, choices=MATERIAL_LEVAS, null=True, blank=True)
	display = models.BooleanField(default=False)
	precio = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=400)	
	estado = models.CharField(max_length=50, choices=ESTADO, default='P')

class TipoCamion(models.Model):
	BOTONES = (
		('Cero', '0 [+0€]'),
		('Cuatro', '4 [+100€]'),
	)
	PIEL = (
		('Cuero', 'Cuero [+200€]'),
		('Alcántara', 'Alcántara [+150€]'),
		('Goma', 'Goma [+100€]'),
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
	tarjeta_credito = models.ForeignKey(TarjetaCredito, on_delete=models.CASCADE, unique=False, null=True)
	direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, unique=False, null=True)
	estado = models.CharField(max_length=50, choices=ESTADO, null=False, default='P')
	dias_finalizar = models.CharField(max_length=3, null=True, default=30)
	
	class Meta:
		permissions = (('is_admin', 'is_admin'),)







