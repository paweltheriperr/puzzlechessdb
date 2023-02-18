from django.db import models

# Klasa FEN dziedziczy po klasie Model z modułu models.
class FEN(models.Model):
    # Pole name typu CharField o maksymalnej długości 100 znaków.
    name = models.CharField(max_length=100)
    # Pole fen typu CharField o maksymalnej długości 100 znaków.
    fen = models.CharField(max_length=100)
