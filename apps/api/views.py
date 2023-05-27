from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
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
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
class HabilidadeViewSet(viewsets.ModelViewSet):
    queryset = Habilidade.objects.all()
    serializer_class = HabilidadeSerializer


@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer


@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer


@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer


@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
class MensagemViewSet(viewsets.ModelViewSet):
    queryset = Mensagem.objects.all()
    serializer_class = MensagemSerializer
