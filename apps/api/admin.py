from django.contrib import admin
from .models import Habilidade, Perfil, Servico, Avaliacao, Pedido, Mensagem

@admin.register(Habilidade)
class HabilidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'experiencia')

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'perfil', 'preco', 'localizacao')

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('perfil', 'servico', 'comentario', 'nota')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('perfil', 'servico', 'data', 'hora', 'status', 'pagamento')

@admin.register(Mensagem)
class MensagemAdmin(admin.ModelAdmin):
    list_display = ('remetente', 'destinatario', 'data_hora', 'assunto', 'texto')
