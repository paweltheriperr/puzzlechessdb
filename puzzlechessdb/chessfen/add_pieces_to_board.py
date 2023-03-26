from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
import chess
import svgwrite
def add_pieces_to_board(dwg, board, square_size):
    # Twórz słownik z nazwami plików obrazków figur szachowych
    # Twórz słownik z linkami do obrazków figur szachowych
    piece_images = {
        'P': 'https://upload.wikimedia.org/wikipedia/commons/4/45/Chess_plt45.svg',
        'N': 'https://upload.wikimedia.org/wikipedia/commons/7/70/Chess_nlt45.svg',
        'B': 'https://upload.wikimedia.org/wikipedia/commons/b/b1/Chess_blt45.svg',
        'R': 'https://upload.wikimedia.org/wikipedia/commons/7/72/Chess_rlt45.svg',
        'Q': 'https://upload.wikimedia.org/wikipedia/commons/1/15/Chess_qlt45.svg',
        'K': 'https://upload.wikimedia.org/wikipedia/commons/4/42/Chess_klt45.svg',
        'p': 'https://upload.wikimedia.org/wikipedia/commons/c/c7/Chess_pdt45.svg',
        'n': 'https://upload.wikimedia.org/wikipedia/commons/e/ef/Chess_ndt45.svg',
        'b': 'https://upload.wikimedia.org/wikipedia/commons/9/98/Chess_bdt45.svg',
        'r': 'https://upload.wikimedia.org/wikipedia/commons/f/ff/Chess_rdt45.svg',
        'q': 'https://upload.wikimedia.org/wikipedia/commons/4/47/Chess_qdt45.svg',
        'k': 'https://upload.wikimedia.org/wikipedia/commons/f/f0/Chess_kdt45.svg',
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