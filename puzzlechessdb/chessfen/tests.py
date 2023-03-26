from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

class ChessFenIndexViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('chessfen:index')
        self.fen_file = SimpleUploadedFile("test_fen.txt", b"rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")

    def test_valid_file_upload(self):
        response = self.client.post(self.url, {'fen_file': self.fen_file})
        self.assertEqual(response.status_code, 200)
        self.assertIn('success_message', response.context)

    def test_invalid_file_upload(self):
        invalid_file = SimpleUploadedFile("test_fen.txt", b"invalid_fen_string")
        response = self.client.post(self.url, {'fen_file': invalid_file})
        self.assertEqual(response.status_code, 200)
        self.assertIn('error_message', response.context)
