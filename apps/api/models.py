from django.db import models
from django.contrib.auth.models import User

class Habilidade(models.Model):
    nome = models.CharField(unique=True, max_length=50)
    descricao = models.TextField()

    class Meta:
        verbose_name_plural = 'Habilidades'

    def __str__(self):
        return self.nome
    

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField('Habilidade')
    experiencia = models.CharField(max_length=255)
    portifolio = models.URLField()

    class Meta:
        verbose_name_plural = 'Perfis'

    def __str__(self):
        return self.user.username


class Servico(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name="servicos")
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    localizacao = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.descricao


class Avaliacao(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name="avaliacoes")
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, related_name="avaliacoes")
    comentario = models.TextField()
    nota = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Avaliações'

    def __str__(self):
        return self.perfil.user.username + self.servico.descricao


class Pedido(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='pedidos')
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, related_name='pedidos')
    data = models.DateField()
    hora = models.TimeField()
    status = models.CharField(max_length=20, default='pendente')
    pagamento = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Pedidos'

    def __str__(self) -> str:
        return self.servico.descricao


class Mensagem(models.Model):
    remetente = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='mensagens_enviadas')
    destinatario = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='mensagens_recebidas')
    data_hora = models.DateTimeField(auto_now_add=True)
    assunto = models.CharField(max_length=100)
    texto = models.TextField()

    class Meta:
        verbose_name_plural = 'Mensagens'

    def __str__(self):
        return self.assunto
