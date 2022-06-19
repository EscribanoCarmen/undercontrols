from django.contrib import admin
from django.urls import path
from django.urls import re_path as url
from . import views



urlpatterns = [
    url(r'^$', views.index, name='index'),
]

urlpatterns += [
    url(r'^create/$', views.createTemplate, name='create_template')
]

urlpatterns += [
    url(r'^create-f1/$', views.F1Create.as_view(), name='f1_create'),
    url(r'^create-camion/$', views.CamionCreate.as_view(), name='camion_create'),
    url(r'^create-turismo/$', views.TurismoCreate.as_view(), name='gt_create'),
]

urlpatterns += [
    url(r'^administrator/$', views.administrator, name='administrator'),
   
]

urlpatterns += [
     url(r'^administrator-pers/$', views.administrator_pers, name='administrator-pers'),
]

urlpatterns += [
    url(r'^administrator-pers/(?P<pk>\d+)/mod/$', views.VolanteUpdate.as_view(), name='administrator-mod')
]

urlpatterns += [
    url(r'^administrator-pers/(?P<pk>\d+)/cancel/$', views.VolanteCancel.as_view(), name='administrator-cancel')
]

urlpatterns += [
    url(r'^administrator-tienda/$', views.administrador_tienda, name='administrator-tienda')
]

urlpatterns += [
    url(r'^administrator-add/$', views.TiendaCreateVolante.as_view(), name='administrator-add')
]

urlpatterns += [
    url(r'^administrator/(?P<pk>\d+)/update/$', views.TiendaUpdateVolante.as_view(), name='administrator-update')
]

urlpatterns += [
    url(r'^administrator/(?P<pk>\d+)/delete/$', views.TiendaDeleteVolante.as_view(), name='administrator-delete')
]

urlpatterns += [
    path("register", views.register_request, name="register")
]

urlpatterns += [
    url(r'^my-products/$', views.mis_pedidos, name='mis_pedidos')
]

urlpatterns += [
     url(r'^product/(?P<pk>\d+)$', views.PedidoDetailView.as_view(), name='producto-detalle'),
]

urlpatterns += [
    url(r'^shop/$', views.Tienda, name='shop')
]

urlpatterns += [
    url(r'^detalle/(?P<pk>\d+)/$', views.VolanteTiendaDetailView, name='detalle')
]

urlpatterns += [
    url(r'^comprar/(?P<pk>\d+)/(?P<tipo>\d+)/(?P<card>\d+)/(?P<local>\d+)/$', views.comprar, name='comprar')
]

urlpatterns += [
    url(r'^about/$',views.aboutUs, name="about_us")
]

urlpatterns += [
    url(r'^compra-finalizada/$', views.gracias, name='gracias')
]

urlpatterns += [
    url(r'^elegir-pago/(?P<pk>\d+)/(?P<tipo>\d+)/crear-metodo-pago/$', views.TarjetaCreate.as_view(), name='metodo-pago-create')
]

urlpatterns += [
    url(r'^elegir-direccion/(?P<pk>\d+)/(?P<tipo>\d+)/(?P<card>\d+)/crear-direccion/$', views.DireccionCreate.as_view(), name='direccion-create')
]

urlpatterns += [
    url(r'^elegir-pago/(?P<pk>\d+)/(?P<tipo>\d+)/$', views.pagar1, name='pago')
]

urlpatterns += [
    url(r'^elegir-direccion/(?P<pk>\d+)/(?P<tipo>\d+)/(?P<card>\d+)/$', views.pagar2, name='direccion')
]