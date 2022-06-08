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
    url(r'^detalle/(?P<pk>\d+)/$', views.VolanteTiendaDetailView.as_view(), name='detalle')
]

urlpatterns += [
    url(r'^comprar/(?P<pk>\d+)/$', views.comprar, name='comprar')
]

urlpatterns += [
    url(r'^about/$',views.aboutUs, name="about_us")
]

