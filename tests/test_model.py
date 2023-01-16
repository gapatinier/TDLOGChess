from model import *
import unittest

def test_defend():
    board = [[Piece(None) for _ in range(8)] for _ in range(8)]
    color = 1
    board[0] = [Rook(color), Knight(color), Bishop(color), Queen(color),
                      King(color), Bishop(color), Knight(color), Rook(color)]
    board[1] = [Pawn(color), Pawn(color), Pawn(color), Pawn(color),
                      Pawn(color), Pawn(color), Pawn(color), Pawn(color)]
    color = 0
    board[7] = [Rook(color), Knight(color), Bishop(color), Queen(color),
                      King(color), Bishop(color), Knight(color), Rook(color)]
    board[6] = [Pawn(color), Pawn(color), Pawn(color), Pawn(color),
                      Pawn(color), Pawn(color), Pawn(color), Pawn(color)]

    queen = Queen(0)
    assert (sorted(queen.defend(board, 3, 3)) == sorted([[3, 1], [3, 2], [3, 4], [3, 5], [3, 6], [0, 3], [1, 3], [2, 3],
                                            [4, 3], [5, 3], [6, 3], [7, 3], [2, 2], [1, 1], [4, 4], [5, 5],
                                            [6, 6], [4, 2], [5, 1], [2, 4], [1, 5], [0, 6]]))
