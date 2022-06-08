# from dataclasses import field
from pyexpat import model
from re import template
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic
from .models import Pedidos, TipoCamion, TipoFormula1, Volante_Tienda, TipoTurismo
# Create your views here.
from django.core.cache import cache

def index(request):
	cache.delete('mi_cache')
	return render(
	request,
	'index.html',
	context= {},
	)

def createTemplate(request):
	return render(
		request,
		'create_template.html',
		context={},
	)

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#CREAR VOLANTE PTIPO F1
class F1Create(CreateView):
	model = TipoFormula1
	fields = ['botones', 'numero_levas', 'material_levas', 'display','precio']
	template_name = 'f1_form.html'
	#variable global
	global pedido
	pedido = Pedidos()

	def get_success_url(self):
		pedido.refF1 = self.object

		pedido.tipo = 'F1 Moderno'
		pedido.dias_finalizar = 30
		pedido.precio = pedido.refF1.precio
		pedido.id = Pedidos.objects.all().count() + 1
		pedido.save()	
		return reverse_lazy('f1_create')
		

	def post(self, request, *args, **kwargs):
		pedido.comprador = request.user.username
		self.object = None
		return super().post(request, *args, **kwargs)

#CREAR VOLANTE GRAN TURISMO
class TurismoCreate(CreateView):
	model =	TipoTurismo
	fields = ['botones', 'numero_levas', 'material_levas', 'display', 'precio']
	template_name = 'turismo_form.html'
	#variable global
	global pedido2
	pedido2 = Pedidos()

	def get_success_url(self):
		pedido2.refTurismo = self.object
		pedido2.tipo = 'GT'
		pedido2.dias_finalizar = 30
		pedido2.precio = pedido2.refTurismo.precio
		pedido2.id = Pedidos.objects.all().count() + 1
		print('---------- ', Pedidos.objects.all().count())
		pedido2.save()
		return reverse_lazy('gt_create')
		

	def post(self, request, *args, **kwargs):
		pedido2.comprador = request.user.username
		self.object = None
		return super().post(request, *args, **kwargs)

class CamionCreate(CreateView):
	model =	TipoCamion
	fields = ['piel_aro', 'botones', 'intermitentes', 'luces', 'precio']
	template_name = 'camion_form.html'
	#variable global
	global pedido3
	pedido3 = Pedidos()

	def get_success_url(self):
		pedido3.refCamion = self.object
		pedido3.tipo = 'Camión'
		pedido3.dias_finalizar = 30
		pedido3.precio = pedido3.refCamion.precio
		pedido3.id = Pedidos.objects.all().count() + 1
		pedido3.save()
		return reverse_lazy('index')
		

	def post(self, request, *args, **kwargs):
		pedido3.comprador = request.user.username
		self.object = None
		return super().post(request, *args, **kwargs)



#FORMULARIOS PARA LA TIENDA (EN ADMINISTRACIÓN)
class TiendaCreateVolante(CreateView):
	model = Volante_Tienda
	fields = '__all__'
	template_name = 'tienda_crear.html'

	def get_success_url(self):
		return reverse_lazy('administrator-tienda')

class TiendaUpdateVolante(UpdateView):
	model = Volante_Tienda
	fields = '__all__'
	template_name = 'tienda_modificar.html'
	def get_success_url(self):
		return reverse_lazy('administrator-tienda')

class TiendaDeleteVolante(DeleteView):
	model = Volante_Tienda
	template_name = 'tienda_quitar.html'

	def get_success_url(self):
		return reverse_lazy('administrator-tienda')


from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect("index")

	form = NewUserForm()
	return render (request, "register.html", context={"register_form":form})


class VolanteUpdate(UpdateView):
	model = Pedidos
	fields = ['estado', 'dias_finalizar']
	template_name = 'modificar_pers.html'
	success_url ="../../"

class VolanteCancel(DeleteView):
	model = Pedidos
	template_name = 'cancel_pers.html'

	def get_success_url(self):
		if self.request.user.has_perm('is_admin'):
			return reverse_lazy('administrator-pers')
		else:
			return reverse_lazy('mis_pedidos')
	

#VISTAS DE ADMINISTRADOR
def administrator(request):
	num_wheelsPed = Pedidos.objects.all().count()
	num_wheelsShop = Volante_Tienda.objects.all().count()

	return render(
		request,
		'administrator.html',
		context={'num_wheelsShop':num_wheelsShop, 'num_wheelsPed': num_wheelsPed}
	)

def administrator_pers(request):
	lista = Pedidos.objects.all()

	return render(
		request,
		'administrator_pers.html',
		context={'lista': lista}
	)

def administrador_tienda(request):
	lista_tienda = Volante_Tienda.objects.all()
	# print(lista_tienda)

	return render(
		request,
		'administrator_tienda.html',
		context={'lista_tienda': lista_tienda}
	)

def mis_pedidos(request):
	lista_pedidos = Pedidos.objects.all()

	return render(
		request, 
		'mis_pedidos.html',
		context={'lista_pedidos': lista_pedidos}
	
	)

class PedidoDetailView(generic.DetailView):
	model = Pedidos
	template_name = 'detalle-pedido.html'
	
#TIENDA
def Tienda(request):
	lista = Volante_Tienda.objects.all()

	return render(
		request,
		'tienda.html',
		context={'lista':lista}
	)

class VolanteTiendaDetailView(generic.DetailView):
	model = Volante_Tienda
	template_name= 'detalle_tienda.html' 

import smtplib
from django.conf import settings
from django.core.mail import send_mail
def comprar(request, pk):
	todos = Volante_Tienda.objects.all()
	#hay que pasarlo a int para comparar la pk que recibo con los ides del queryset
	ide = int(pk)		

	#variable global
	global pedido4
	pedido4 = Pedidos()

	pedido4.comprador = request.user.username
	for i in todos:
		if i.id == ide:
			pedido4.refTienda = i
	pedido4.tipo = 'De Tienda'
	pedido4.dias_finalizar = 0
	pedido4.save()

	# email function
	email_from = settings.EMAIL_HOST_USER
	recipient_list = ["cargares2013@gmail.com"]
	subject = "Asunstos"
	message = "Gracias por su compra"

	send_mail(subject, message, email_from, recipient_list)

	return render(
		request,
		'comprado.html',
		context={}
	)

def aboutUs(request):
	return render(
		request,
		"about_us.html",
		context={},
	)
		
		


	

