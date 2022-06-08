from django.contrib import admin
from .models import Volante_Tienda, TipoFormula1, Pedidos, TipoCamion, TipoTurismo
# Register your models here.


admin.site.register(Volante_Tienda)
admin.site.register(TipoFormula1)
admin.site.register(TipoTurismo)
admin.site.register(TipoCamion)
admin.site.register(Pedidos)
