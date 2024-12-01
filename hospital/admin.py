from django.contrib import admin
from hospital.models import *

class ConsultaAdmin(admin.ModelAdmin):
    list_display = ("id", "motivo_consulta")

class CirurgiaAdmin(admin.ModelAdmin):
    list_display = ("id", "procedimento")

class ExameAdmin(admin.ModelAdmin):
    list_display = ("id", "tipo_exame")

class TratamentoAdmin(admin.ModelAdmin):
    list_display = ("id", "tipo_tratamento")

class PlanosAdmin(admin.ModelAdmin):
    list_display = ("id",)

class PacienteAdmin(admin.ModelAdmin):
    list_display = ("id", "nome")

class HistoricoMedicoAdmin(admin.ModelAdmin):
    list_display = ("id", "paciente")

admin.site.register(Consulta, ConsultaAdmin)
admin.site.register(Cirurgia, CirurgiaAdmin)
admin.site.register(Exame, ExameAdmin)
admin.site.register(Tratamento, TratamentoAdmin)
admin.site.register(Plano, PlanosAdmin)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(HistoricoMedico, HistoricoMedicoAdmin)
