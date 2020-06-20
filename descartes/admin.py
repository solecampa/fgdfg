from django.contrib import admin
from .models import Tecnico, Motivo, Descartes, Guia, Filtro


# Register your models here.




class DescartesAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'producto', 'lote', 'motivo', 'tecnico','volumen','guia', 'filtro', 'linea')
class GuiaAdmin(admin.ModelAdmin):
    list_display = ('guia', )
class FiltroAdmin(admin.ModelAdmin):
    list_display = ('filtro', )
class TecnicoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'iniciales' )
class MotivoAdmin(admin.ModelAdmin):
    list_display = ('motivo', )



admin.site.register(Descartes, DescartesAdmin)
admin.site.register(Tecnico, TecnicoAdmin)
admin.site.register(Motivo, MotivoAdmin)
admin.site.register(Guia, GuiaAdmin)
admin.site.register(Filtro, FiltroAdmin)
