from django.test.client import Client
from django.test.testcases import TestCase
from django.urls import reverse


class CoreURLSTestCase(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_access_page_index(self):
        """_Teste de acesso direto a pagina home sem login gera erro """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
    
    def test_access_page_login_adim(self):
        """_Teste de acesso direto a pagina home sem login gera erro """
        response = self.client.get(reverse('admin:login'))
        self.assertEqual(response.status_code, 200)