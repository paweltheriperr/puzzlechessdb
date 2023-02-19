from django.http import HttpResponse
from django.shortcuts import render
import chess
import svgwrite
def add_pieces_to_board(dwg, board, square_size):
    # Twórz słownik z nazwami plików obrazków figur szachowych
    piece_images = {
        'P': 'wp.svg', 'N': 'wn.svg', 'B': 'wb.svg', 'R': 'wr.svg',
        'Q': 'wq.svg', 'K': 'wk.svg', 'p': 'bp.svg', 'n': 'bn.svg',
        'b': 'bb.svg', 'r': 'br.svg', 'q': 'bq.svg', 'k': 'bk.svg'
    }
    # Dla każdego pola na planszy
    for y in range(8):
        for x in range(8):
            # Ustaw pozycję figury na planszy
            square = chess.square(x, 7-y)
            # Jeśli na polu stoi figura
            if board.piece_at(square) is not None:
                # Pobierz nazwę pliku obrazka dla figury
                piece = piece_images[board.piece_at(square).symbol()]
                # Dodaj obrazek figury do planszy SVG
                dwg.add(dwg.image(piece, insert=(x * square_size, y * square_size), size=(square_size, square_size)))

def index(request):
    # Twórz planszę szachową
    board = chess.Board("1K3r2/8/P1B4b/1N6/2N5/PP1Np3/kBppN3/5qR1 w - - 0 1")
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
    # Dodaj figurki na planszę SVG
    add_pieces_to_board(dwg, board, square_size)
    # Utwórz kod SVG planszy jako tekst
    svg_code = dwg.tostring()
    # Renderuj szablon HTML i przekaż kod SVG planszy jako zmienną kontekstu
    return render(request, 'chessfen/index.html', {'board_svg': svg_code})
