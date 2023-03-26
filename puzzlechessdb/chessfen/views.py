from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
import chess
import svgwrite
from .models import ChessFen
from .add_pieces_to_board import add_pieces_to_board
from .generate_board_svg import generate_board_svg




def index(request):
    if request.method == 'POST':
        # Pobierz dane z formularza
        fen = request.POST.get('chess-fen')

        # Sprawdź poprawność FEN
        try:
            board = chess.Board(fen)
        except ValueError:
            # Wyświetl błąd w przeglądarce i zwróć odpowiedź HTTP z błędem
            error_message = 'Nieprawidłowy FEN'
            return render(request, 'chessfen/index.html', {'error_message': error_message})

        # Zapisz FEN w bazie danych
        chess_fen = ChessFen(fen=fen)
        chess_fen.save()

        # Wyświetl informację o sukcesie w przeglądarce
        success_message = 'Zapisano FEN: ' + fen
        return render(request, 'chessfen/index.html', {'success_message': success_message})

    else:
        # Utwórz planszę SVG dla domyślnego FEN
        board = chess.Board('5rk1/4n1b1/2Pqb1pp/rpp1pp2/N1P5/1Q1PP1P1/3N1PBP/1R1R2K1 w - - 0 1')
        dwg = svgwrite.Drawing(size=('100%', '100%'))
        square_size = 50
        for y in range(8):
            for x in range(8):
                fill = '#D18B47' if (x + y) % 2 else '#FFCE9E'
                dwg.add(dwg.rect(insert=(x * square_size, y * square_size), size=(square_size, square_size), fill=fill))
        add_pieces_to_board(dwg, board, square_size)
        svg_code = dwg.tostring()

        # Wyświetl planszę SVG i formularz
        return render(request, 'chessfen/index.html', {'board_svg': svg_code})


def inst(request):

    return render(request, 'chessfen/inst.html')
def dcp(request):
    latest_fen = ChessFen.objects.order_by('-id').last()
    fen_str = latest_fen.fen
    board = chess.Board(fen_str)

    dwg = svgwrite.Drawing(size=('100%', '100%'))
    square_size = 50
    for y in range(8):
        for x in range(8):
            fill = '#D18B47' if (x + y) % 2 else '#FFCE9E'
            dwg.add(dwg.rect(insert=(x * square_size, y * square_size), size=(square_size, square_size), fill=fill))
    add_pieces_to_board(dwg, board, square_size)
    svg_code = dwg.tostring()
    print(latest_fen.fen)
    print(type(latest_fen.id))

    # Wyświetl planszę SVG
    return render(request, 'chessfen/dcp.html', {'board_svg': svg_code})