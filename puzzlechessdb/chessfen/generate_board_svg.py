from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
import chess
import svgwrite
from .add_pieces_to_board import add_pieces_to_board
def generate_board_svg(fen):
    board = chess.Board(fen)
    dwg = svgwrite.Drawing(size=('100%', '100%'))
    square_size = 50
    for y in range(8):
        for x in range(8):
            fill = '#D18B47' if (x + y) % 2 else '#FFCE9E'
            dwg.add(dwg.rect(insert=(x * square_size, y * square_size), size=(square_size, square_size), fill=fill))
    add_pieces_to_board(dwg, board, square_size)
    return dwg.tostring()
