from django.db import models

class FEN(models.Model):
    fen = models.CharField(max_length=100)
