from django.db import models

class ChessPosition(models.Model):
    fen = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fen
