from rest_framework import viewsets
from .models import Habilidade, Perfil, Servico, Avaliacao, Pedido, Mensagem
from .serializers import (
    HabilidadeSerializer, 
    PedidoSerializer, 
    PerfilSerializer, 
    ServicoSerializer, 
    AvaliacaoSerializer, 
    MensagemSerializer,
)


# /habilidades > route url > viewset > get data in model > return with serializer
class HabilidadeViewSet(viewsets.ModelViewSet):
    queryset = Habilidade.objects.all()
    serializer_class = HabilidadeSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer


class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer


class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer


class MensagemViewSet(viewsets.ModelViewSet):
    queryset = Mensagem.objects.all()
    serializer_class = MensagemSerializer
