from django.urls import path, include
from rest_framework import routers
from .views import (
    HabilidadeViewSet,
    PedidoViewSet,
    PerfilViewSet,
    ServicoViewSet,
    AvaliacaoViewSet,
    MensagemViewSet,
)

router = routers.DefaultRouter()
router.register('habilidades', HabilidadeViewSet)
router.register('pedidos', PedidoViewSet)
router.register('perfis', PerfilViewSet)
router.register('servicos', ServicoViewSet)
router.register('avaliacoes', AvaliacaoViewSet)
router.register('mensagens', MensagemViewSet)

api_router = [
    # outras urls do seu projeto
    path('', include(router.urls)),
]
