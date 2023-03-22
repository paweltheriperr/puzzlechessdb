from django.test import TestCase
from django.test import TestCase, Client
from django.urls import reverse
from chess import Board
from .models import Fen

class ChessFenTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('chessfen:index')


    def test_get_index_page(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chessfen/index.html')
        self.assertContains(response, 'FEN')
#Testowanie wyświetlania strony głównej (GET request)
    def test_post_invalid_fen(self):
        data = {'chess_fen': 'invalid fen'}
        response = self.client.post(self.url, data=data)
        self.assertTemplateUsed(response, 'chessfen/index.html')
        self.assertContains(response, 'Niepoprawny FEN.')
        self.assertEqual(Fen.objects.count(), 0)
        #Testowanie wprowadzenia niepoprawnego FEN (POST request)

    def test_post_valid_fen(self):
        board = Board()
        fen_str = board.fen()
        data = {'chess_fen': fen_str}
        response = self.client.post(self.url, data=data)
        self.assertTemplateUsed(response, 'chessfen/index.html')
        self.assertContains(response, fen_str)
        self.assertEqual(Fen.objects.count(), 1)
        self.assertEqual(Fen.objects.last().fen, fen_str)
        #Testowanie wprowadzenia poprawnego FEN (POST request)
