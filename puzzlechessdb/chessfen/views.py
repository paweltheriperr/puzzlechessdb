# Importuj potrzebne moduły
from django.shortcuts import render
import chess
import svgwrite

# Definiuj widok dla żądania HTTP
def index(request):
    # Twórz planszę szachową
    board = chess.Board()
    # Twórz obiekt svg dla planszy
    dwg = svgwrite.Drawing(size=('100%', '100%'))
    # Ustaw rozmiar kwadratu
    square_size = 50
    # Dla każdego wiersza i kolumny na planszy szachowej
    for y in range(8):
        for x in range(8):
            # Ustaw kolor kwadratu
            fill = '#D18B47' if (x + y) % 2 else '#FFCE9E'
            # Dodaj kwadrat do planszy svg
            dwg.add(dwg.rect(insert=(x * square_size, y * square_size), size=(square_size, square_size), fill=fill))
    # Utwórz kod SVG planszy jako tekst
    svg_code = dwg.tostring()
    # Renderuj szablon HTML i przekaż kod SVG planszy jako zmienną kontekstu
    return render(request, 'chessfen/index.html', {'board_svg': svg_code})
