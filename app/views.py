# from dataclasses import field

from cmath import isnan
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth import login
from .forms import NewUserForm
from django.shortcuts import render, redirect
from pyexpat import model
from re import template
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic
from .models import Direccion, Pedidos, TipoCamion, TipoFormula1, UsuarioDatos, Volante_Tienda, TipoTurismo, User, TarjetaCredito
# Create your views here.
from django.core.cache import cache
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


def index(request):
    ide = 404
    if request.user.is_authenticated:
        for i in UsuarioDatos.objects.all():
            if i.user == request.user:
                ide = i.id

    return render(
        request,
        'index.html',
        context={'ide': ide},
    )


def createTemplate(request):
    return render(
        request,
        'create_template.html',
        context={},
    )


# CREAR VOLANTE PTIPO F1


class F1Create(CreateView):
    model = TipoFormula1
    fields = ['botones', 'numero_levas', 'material_levas', 'display', 'precio']
    template_name = 'f1_form.html'

    def get_success_url(self, **kwargs):         
        if  kwargs != None:
            return reverse_lazy('pago', kwargs = {'pk': self.object.id, 'tipo': 1})


# CREAR VOLANTE GRAN TURISMO


class TurismoCreate(CreateView):
    model = TipoTurismo
    fields = ['botones', 'numero_levas', 'material_levas', 'display', 'precio']
    template_name = 'turismo_form.html'
    
    def get_success_url(self, **kwargs):         
        if  kwargs != None:
            return reverse_lazy('pago', kwargs = {'pk': self.object.id, 'tipo': 2})



class CamionCreate(CreateView):
    model = TipoCamion
    fields = ['piel_aro', 'botones', 'intermitentes', 'luces', 'precio']
    template_name = 'camion_form.html'
    
    def get_success_url(self, **kwargs):         
        if  kwargs != None:
            return reverse_lazy('pago', kwargs = {'pk': self.object.id, 'tipo': 3})


# FORMULARIOS PARA LA TIENDA (EN ADMINISTRACIÓN)
class TiendaCreateVolante(CreateView):
    model = Volante_Tienda
    fields = '__all__'
    template_name = 'tienda_crear.html'

    def get_success_url(self):
        return reverse_lazy('administrator-tienda')


class TarjetaCreate(CreateView):
    model = TarjetaCredito
    fields = ['tarjeta_credito', 'num_tarjeta', 'fecha_caducidad', 'codigo_seguridad']
    template_name = 'metodo_pago.html'
    success_url = "../"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
         



class DireccionCreate(CreateView):
    model = Direccion
    fields = ['direccion', 'puerta', 'piso', 'ciudad', 'provincia']
    template_name = 'direccion_crear.html'
    success_url = "../"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

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

from django.forms import ValidationError
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        global datos
        datos = UsuarioDatos()
        if form.is_valid():
            username = form['username'].value()
            print(User.objects.filter(username=username).exists(), '///////////////////')
            user = form.save()
            datos.user = user
            
            datos.save()
            login(request, user)
            return redirect("index")

    form = NewUserForm()
    return render(request, "register.html", context={"register_form": form})



class VolanteUpdate(UpdateView):
    model = Pedidos
    fields = ['estado', 'dias_finalizar']
    template_name = 'modificar_pers.html'
    success_url = "../../"


class VolanteCancel(DeleteView):
    model = Pedidos
    template_name = 'cancel_pers.html'

    def get_success_url(self):
        if self.request.user.has_perm('is_admin'):
            return reverse_lazy('administrator-pers')
        else:
            return reverse_lazy('mis_pedidos')


# VISTAS DE ADMINISTRADOR
def administrator(request):
    num_wheelsPed = Pedidos.objects.all().count()
    num_wheelsShop = Volante_Tienda.objects.all().count()

    return render(
        request,
        'administrator.html',
        context={'num_wheelsShop': num_wheelsShop,
                 'num_wheelsPed': num_wheelsPed}
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
    lista_pedidos = []
    lista_pedidos1 = Pedidos.objects.all()
    for i in lista_pedidos1:
        if i.comprador == request.user.username:
            lista_pedidos.append(i)

    return render(
        request,
        'mis_pedidos.html',
        context={'lista_pedidos': lista_pedidos}

    )


class PedidoDetailView(generic.DetailView):
    model = Pedidos
    template_name = 'detalle-pedido.html'

# TIENDA


def Tienda(request):
    lista = Volante_Tienda.objects.all()

    return render(
        request,
        'tienda.html',
        context={'lista': lista}
    )

def VolanteTiendaDetailView(request, pk):
    todos = Volante_Tienda.objects.all()
    volante = ''
    usuario = UsuarioDatos()
    for i in todos:
        if i.id == int(pk):
            volante = i
    ide = 0
    if request.user.is_authenticated:
        for i in UsuarioDatos.objects.all():
            if i.user == request.user:
                ide = i.id
    try:
        usuario = UsuarioDatos.objects.get(pk=ide)
        
    except:
        todos = UsuarioDatos.objects.all()
        for i in todos:
            if i.user == 23: 
                usuario = i
           
    
    return render(
        request,
        "detalle_tienda.html",
        context={'volante_tienda': volante,
        'ide': ide,
        'tipo': 4,
        'usuario':usuario}
    )


def aboutUs(request):
    return render(
        request,
        "about_us.html",
        context={},
    )

def gracias(request):
    return render(
        request,
        "comprado2.html",
        context={}
    )
    


class updateUser(UpdateView):
    model = User
    fields= '__all__'
    template_name = 'editar-perfil1.html'

    def get_success_url(self):
        return reverse_lazy('administrator-tienda')

def enviarEmail(receptor, mensaje):
    #EMAIL
    subject = 'Compra en Under Controls'
    receptorF = receptor
    # print(receptor)

    template = render_to_string('email.html', {
        'name': 'Compra en Under Controls SL.',
        'email': mensaje,
        'messsage': mensaje,
    })

    email = EmailMessage(
        subject,
        template,
        settings.EMAIL_HOST_USER,
        [receptorF]
    )

    email.fail_silently = False
    email.send()

######################################
def pagar1(request, pk, tipo):
    todos = TarjetaCredito.objects.all()
    
    disponibles = []
    for i in todos:
        if i.user == request.user:
            disponibles.append(i)

    return render(
        request,
        'elegir_pago.html',
        context={
            'disponibles': disponibles,
            'pk':pk,
            'tipo': tipo,
            },
    )

def pagar2(request, pk, tipo, card):
    direcciones = Direccion.objects.all()
    localizaciones = []
    for x in direcciones:
        if x.user == request.user:
            localizaciones.append(x)
    return render(
        request,
        'elegir_direccion.html',
        context={
            'card':card,
            'pk':pk,
            'tipo': tipo,
            'localizaciones': localizaciones,
            },
    )

#COMPRAR **************
def comprar(request, pk, tipo, card, local):
    tarjetas = TarjetaCredito.objects.all()
    direcciones = Direccion.objects.all()
    #hay que pasarlo a int para comparar la pk que recibo con los ides del queryset
    ide = int(pk)
    card = int(card)
    local = int(local)
    tipo = int(tipo)
    #COMPROBAR EL TIPO DE VOLANTE
    #F1
    if tipo == 1:
        pedido = Pedidos()
        todos = TipoFormula1.objects.all()
        for i in todos:
            if i.id == ide:
                pedido.refF1 = i
        for c in tarjetas:
            if c.id == card:
                pedido.tarjeta_credito = c
        for l in direcciones:
            if l.id == local:
                pedido.direccion = l
        pedido.tipo = 'F1 Moderno'
        pedido.dias_finalizar = 30
        pedido.precio = pedido.refF1.precio
        pedido.id = Pedidos.objects.all().count() + 1
        pedido.comprador = request.user.username
        pedido.save()

        mensaje = '[Este mensaje fue enviado automáticamente, no responda por favor]\n Usted ha comprado un producto personalizado en Under Controls. Puede ver el proceso de construcción de su volante en Mis Pedidos en nuesta web.'
        enviarEmail(request.user.email, mensaje)
    elif tipo == 2:
        pedido2 = Pedidos()
        todos = TipoTurismo.objects.all()
        for i in todos:
            if i.id == ide:
                pedido2.refTurismo = i
        for c in tarjetas:
            if c.id == card:
                pedido2.tarjeta_credito = c
        for l in direcciones:
            if l.id == local:
                pedido2.direccion = l
        pedido2.tipo = 'Turismo/GT'
        pedido2.dias_finalizar = 30
        pedido2.precio = pedido2.refTurismo.precio
        pedido2.id = Pedidos.objects.all().count() + 1
        pedido2.comprador = request.user.username
        pedido2.save()

        mensaje = '[Este mensaje fue enviado automáticamente, no responda por favor]\n Usted ha comprado un producto personalizado en Under Controls. Puede ver el proceso de construcción de su volante en Mis Pedidos en nuesta web.'
        enviarEmail(request.user.email, mensaje)

    elif tipo == 3:
        pedido3 = Pedidos()
        todos = TipoFormula1.objects.all()
        for i in todos:
            if i.id == ide:
                pedido3.refCamion = i
        for c in tarjetas:
            if c.id == card:
                pedido3.tarjeta_credito = c
        for l in direcciones:
            if l.id == local:
                pedido3.direccion = l
        pedido3.tipo = 'F1 Moderno'
        pedido3.dias_finalizar = 30
        pedido3.precio = pedido3.refCamion.precio
        pedido3.id = Pedidos.objects.all().count() + 1
        pedido3.comprador = request.user.username
        pedido3.save()

        mensaje = '[Este mensaje fue enviado automáticamente, no responda por favor]\n Usted ha comprado un producto personalizado en Under Controls. Puede ver el proceso de construcción de su volante en Mis Pedidos en nuesta web.'
        enviarEmail(request.user.email, mensaje)
    
    elif tipo == 4:
        pedido4 = Pedidos()
        pedido4.comprador = request.user.username
        todos_volante_tienda = Volante_Tienda.objects.all()
        for i in todos_volante_tienda:
            if i.id == ide:
                pedido4.refTienda = i
                pedido4.precio = i.precio
        pedido4.tipo = 'De Tienda'
        for c in tarjetas:
            if c.id == card:
                pedido4.tarjeta_credito = c
        for l in direcciones:
            if l.id == local:
                pedido4.direccion = l

        pedido4.dias_finalizar = 0
        pedido4.save()


        mensaje = '[Este mensaje fue enviado automáticamente, no responda por favor]\n Usted ha comprado un producto de la tienda de Under Controls. Su producto llegará en un periodo de entre 3-7 días al domicilio asignado a su cuenta.'
        enviarEmail(request.user.email, mensaje)

    return render(
        request,
        'comprado2.html',
        context={},
    )

