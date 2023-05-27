from rest_framework.test import APIClient
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.test import TestCase
from django.contrib.auth.models import User

from apps.api.models import Habilidade, Perfil, Servico, Avaliacao, Pedido, Mensagem


class TestHabilidadesViewSet(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="user_teste", email="test@test.com", password="teste123")
        self.refresh_token = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.refresh_token.access_token}")
        Habilidade.objects.create(nome="Habilidade de testes", descricao="Habilidade em realizar testes")


    def test_list_view(self):
        # Faz a requisição e verifica se a resposta foi bem-sucedida (status 200)
        response = self.client.get("/api/habilidades/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verificar se a resposta é a esperada (list)
        content = response.json()
        self.assertIsInstance(content, list)

        # Verificar se os dados retornados estão de acordo com o esperado
        expected_name = "Habilidade de testes"
        expected_description = "Habilidade em realizar testes"
        content_data = content[0]
        self.assertEqual(expected_name, content_data.get("nome"))
        self.assertEqual(expected_description, content_data.get("descricao"))

    def test_create_view(self):
        # Cria o payload a ser testado
        data = {"nome": "Habilidade em Jardinagem", "descricao": "Habilidade em cuidar de jardins"}

        # Faz a requisição e verifica se a resposta foi bem-sucedida (status 201)
        response = self.client.post("/api/habilidades/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_view(self):
        habilidade_id = 1

        # Faz a requisição e verifica se a resposta foi bem-sucedida (status 200)
        response = self.client.get(f"/api/habilidades/{habilidade_id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verifica se a resposta contém os dados esperados
        expected_name = "Habilidade de testes"
        expected_description = "Habilidade em realizar testes"
        content = response.json()
        self.assertEqual(expected_name, content.get("nome"))
        self.assertEqual(expected_description, content.get("descricao"))


class TestPerfisViewSet(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="user_teste", email="test@test.com", password="teste123")
        self.refresh_token = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.refresh_token.access_token}")
        Habilidade.objects.create(nome="Habilidade de engenharia", descricao="Habilidade em realizar engenharia")
        Perfil.objects.create(user=self.user, experiencia="Experiência de testes", portifolio="https://www.teste.com")


    def test_list_view(self):
        # Faz a requisição e verifica se a resposta foi bem-sucedida (status 200)
        response = self.client.get("/api/perfis/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verificar se a resposta é a esperada (list)
        content = response.json()
        self.assertIsInstance(content, list)

        # Verificar se os dados retornados estão de acordo com o esperado
        expected_experience = "Experiência de testes"
        expected_portifolio = "https://www.teste.com"
        content_data = content[0]
        self.assertEqual(expected_experience, content_data.get("experiencia"))
        self.assertEqual(expected_portifolio, content_data.get("portifolio"))

    def test_create_view(self):
        # Cria um novo usuário para o teste
        user_2 = User.objects.create_user(username="user_teste2", email="test2@test2.com", password="teste1234")

        # Cria o payload a ser testado
        data = {
            "user": user_2.pk, 
            "experiencia": "Experiência em jardinagem", 
            "portifolio": "https://www.jardinagem.com",
            "habilidades": [1]
        }

        # Faz a requisição e verifica se a resposta foi bem-sucedida (status 201)
        response = self.client.post("/api/perfis/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_view(self):
        perfil_id = 1

        # Faz a requisição e verifica se a resposta foi bem-sucedida (status 200)
        response = self.client.get(f"/api/perfis/{perfil_id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verifica se a resposta contém os dados esperados
        expected_experience = "Experiência de testes"
        expected_portifolio = "https://www.teste.com"
        content = response.json()
        self.assertEqual(expected_experience, content.get("experiencia"))
        self.assertEqual(expected_portifolio, content.get("portifolio"))


class TestServicosViewSet(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="user_teste", email="test@test.com", password="teste123")
        self.refresh_token = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.refresh_token.access_token}")
        self.perfil = Perfil.objects.create(user=self.user, experiencia="Experiência de testes", portifolio="https://www.teste.com")
        Servico.objects.create(perfil=self.perfil, descricao="Descrição de testes", preco=100.00, localizacao="Leme - SP")


    def test_list_view(self):
        # Faz a requisição e verifica se a resposta foi bem-sucedida (status 200)
        response = self.client.get("/api/servicos/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verificar se a resposta é a esperada (list)
        content = response.json()
        self.assertIsInstance(content, list)

        # Verificar se os dados retornados estão de acordo com o esperado
        expected_description = "Descrição de testes"
        expected_price = "100.00"
        expected_location = "Leme - SP"
        content_data = content[0]
        self.assertEqual(expected_description, content_data.get("descricao"))
        self.assertEqual(expected_price, content_data.get("preco"))
        self.assertEqual(expected_location, content_data.get("localizacao"))

    def test_create_view(self):
        # Cria o payload a ser testado
        data = {
            "perfil": self.perfil.pk,
            "descricao": "Descrição de jardinagem",
            "preco": 100.00,
            "localizacao": "Leme - SP"
        }

        # Faz a requisição e verifica se a resposta foi bem-sucedida (status 201)
        response = self.client.post("/api/servicos/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_view(self):
        servico_id = 1

        # Faz a requisição e verifica se a resposta foi bem-sucedida (status 200)
        response = self.client.get(f"/api/servicos/{servico_id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verifica se a resposta contém os dados esperados
        expected_description = "Descrição de testes"
        expected_price = "100.00"
        expected_location = "Leme - SP"
        content = response.json()
        self.assertEqual(expected_description, content.get("descricao"))
        self.assertEqual(expected_price, content.get("preco"))
        self.assertEqual(expected_location, content.get("localizacao"))


class TestAvaliacoesViewSet(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="user_teste", email="test@test.com", password="teste123")
        self.refresh_token = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.refresh_token.access_token}")
        self.perfil = Perfil.objects.create(user=self.user, experiencia="Experiência de testes", portifolio="https://www.teste.com")
        self.servico = Servico.objects.create(perfil=self.perfil, descricao="Descrição de testes", preco=100.00, localizacao="Leme - SP")
        Avaliacao.objects.create(perfil=self.perfil, servico=self.servico, comentario="Comentário de testes", nota=5)


    def test_list_view(self):
        # Faz a requisição e verifica se a resposta foi bem-sucedida (status 200)
        response = self.client.get("/api/avaliacoes/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verificar se a resposta é a esperada (list)
        content = response.json()
        self.assertIsInstance(content, list)

        # Verificar se os dados retornados estão de acordo com o esperado
        expected_comment = "Comentário de testes"
        expected_note = 5
        content_data = content[0]
        self.assertEqual(expected_comment, content_data.get("comentario"))
        self.assertEqual(expected_note, content_data.get("nota"))

    def test_create_view(self):
        # Cria o payload a ser testado
        data = {
            "perfil": self.perfil.pk,
            "servico": self.servico.pk,
            "comentario": "Comentário de jardinagem",
            "nota": 5
        }

        # Faz a requisição e verifica se a resposta foi bem-sucedida (status 201)
        response = self.client.post("/api/avaliacoes/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_view(self):
        avaliacao_id = 1

        # Faz a requisição e verifica se a resposta foi bem-sucedida (status 200)
        response = self.client.get(f"/api/avaliacoes/{avaliacao_id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verifica se a resposta contém os dados esperados
        expected_comment = "Comentário de testes"
        expected_note = 5
        content = response.json()
        self.assertEqual(expected_comment, content.get("comentario"))
        self.assertEqual(expected_note, content.get("nota"))


class TestPedidosViewSet(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="user_teste", email="test@test.com", password="teste123")
        self.refresh_token = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.refresh_token.access_token}")
        self.perfil = Perfil.objects.create(user=self.user, experiencia="Experiência de testes", portifolio="https://www.teste.com")
        self.servico = Servico.objects.create(perfil=self.perfil, descricao="Descrição de testes", preco=100.00, localizacao="Leme - SP")
        Pedido.objects.create(perfil=self.perfil, servico=self.servico, data="2021-10-10", hora="10:00:00", status="pendente")


    def test_list_view(self):
        # Faz a requisição e verifica se a resposta foi bem-sucedida (status 200)
        response = self.client.get("/api/pedidos/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verificar se a resposta é a esperada (list)
        content = response.json()
        self.assertIsInstance(content, list)

        # Verificar se os dados retornados estão de acordo com o esperado
        expected_date = "2021-10-10"
        expected_hour = "10:00:00"
        expected_status = "pendente"
        content_data = content[0]
        self.assertEqual(expected_date, content_data.get("data"))
        self.assertEqual(expected_hour, content_data.get("hora"))
        self.assertEqual(expected_status, content_data.get("status"))

    def test_create_view(self):
        # Cria o payload a ser testado
        data = {
            "perfil": self.perfil.pk,
            "servico": self.servico.pk,
            "data": "2021-10-10",
            "hora": "10:00:00",
            "status": "pendente"
        }

        # Faz a requisição e verifica se a resposta foi bem-sucedida (status 201)
        response = self.client.post("/api/pedidos/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_view(self):
        pedido_id = 1

        # Faz a requisição e verifica se a resposta foi bem-sucedida (status 200)
        response = self.client.get(f"/api/pedidos/{pedido_id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verifica se a resposta contém os dados esperados
        expected_date = "2021-10-10"
        expected_hour = "10:00:00"
        expected_status = "pendente"
        content = response.json()
        self.assertEqual(expected_date, content.get("data"))
        self.assertEqual(expected_hour, content.get("hora"))
        self.assertEqual(expected_status, content.get("status"))


class TestMensagemViewSet(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user_rmt = User.objects.create_user(username="user_remetente", email="test@test.com", password="teste123")
        self.user_dst = User.objects.create_user(username="user_destinatario", email="test@test.com", password="teste123")
        self.refresh_token = RefreshToken.for_user(self.user_rmt)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.refresh_token.access_token}")
        self.remetente = Perfil.objects.create(user=self.user_rmt, experiencia="Remetente de testes", portifolio="https://www.teste.com")
        self.destinatario = Perfil.objects.create(user=self.user_dst, experiencia="Destinatario de testes", portifolio="https://www.teste.com")
        Mensagem.objects.create(remetente=self.remetente, destinatario=self.destinatario, texto="Texto de testes")

    def test_list_view(self):
        # Faz a requisição e verifica se a resposta foi bem-sucedida (status 200)
        response = self.client.get("/api/mensagens/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verificar se a resposta é a esperada (list)
        content = response.json()
        self.assertIsInstance(content, list)

        # Verificar se os dados retornados estão de acordo com o esperado
        expected_text = "Texto de testes"
        content_data = content[0]
        self.assertEqual(expected_text, content_data.get("texto"))

    def test_create_view(self):
        # Cria o payload a ser testado
        data = {
            "remetente": self.remetente.pk,
            "destinatario": self.destinatario.pk,
            "data_hora": "2021-10-10T10:00:00Z",
            "assunto": "Assunto de testes",
            "texto": "Texto de testes"
        }

        # Faz a requisição e verifica se a resposta foi bem-sucedida (status 201)
        response = self.client.post("/api/mensagens/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
