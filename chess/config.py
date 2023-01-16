from pathlib import Path
import model

p = Path("./images")

BLACK_BISHOP = p.joinpath("bbishop.png")
BLACK_KING = p.joinpath("bking.png")
BLACK_KNIGHT = p.joinpath("bknight.png")
BLACK_PAWN = p.joinpath("bpawn.png")
BLACK_QUEEN = p.joinpath("bqueen.png")
BLACK_ROOK = p.joinpath("brook.png")
WHITE_BISHOP = p.joinpath("wbishop.png")
WHITE_KING = p.joinpath("wking.png")
WHITE_KNIGHT = p.joinpath("wknight.png")
WHITE_PAWN = p.joinpath("wpawn.png")
WHITE_QUEEN = p.joinpath("wqueen.png")
WHITE_ROOK = p.joinpath("wrook.png")

LOGO = p.joinpath("strategy.png")


Board = [[Piece(color=None, ptype=PieceType.Pawn, value=0) for _ in range(8)] for _ in range(8)]
color = 1
Player_pieces = [[Rook(color=0), Rook(color=0), Knight(color=0), Knight(color=0),
                  Bishop(color=0), Bishop(color=0), Queen(color=0),
                  King(color=0),
                  Pawn(color=0), Pawn(color=0), Pawn(color=0), Pawn(color=0),
                  Pawn(color=0), Pawn(color=0), Pawn(color=0), Pawn(color=0)],
                 [Rook(color=1), Rook(color=1), Knight(color=1), Knight(color=1),
                  Bishop(color=1), Bishop(color=1), Queen(color=1),
                  King(color=1),
                  Pawn(color=1), Pawn(color=1), Pawn(color=1), Pawn(color=1),
                  Pawn(color=1), Pawn(color=1), Pawn(color=1), Pawn(color=1)]
                 ]
Board[0] = [Rook(color=color), Knight(color=color), Bishop(color=color), Queen(color=color),
            King(color=color), Bishop(color=color), Knight(color=color), Rook(color=color)]
Board[1] = [Pawn(color=color), Pawn(color=color), Pawn(color=color), Pawn(color=color),
            Pawn(color=color), Pawn(color=color), Pawn(color=color), Pawn(color=color)]
color = 0
Board[7] = [Rook(color=color), Knight(color=color), Bishop(color=color), Queen(color=color),
            King(color=color), Bishop(color=color), Knight(color=color), Rook(color=color)]
Board[6] = [Pawn(color=color), Pawn(color=color), Pawn(color=color), Pawn(color=color),
            Pawn(color=color), Pawn(color=color), Pawn(color=color), Pawn(color=color)]


pieces_init = [[], []]
coords_init = [[], []]
for color in range(2):
    pieces_init[color] = [Rook(color=color), Rook(color=color), Knight(color=color), Knight(color=color),
                          Bishop(color=color), Bishop(color=color), Queen(color=color),
                          King(color=color),
                          Pawn(color=color), Pawn(color=color), Pawn(color=color), Pawn(color=color),
                          Pawn(color=color), Pawn(color=color), Pawn(color=color), Pawn(color=color)]
    coords_init[color] = [[0, 7 * (1 - color)], [7, 7 * (1 - color)], [1, 7 * (1 - color)], [6, 7 * (1 - color)],
                          [2, 7 * (1 - color)], [5, 7 * (1 - color)], [3, 7 * (1 - color)], [4, 7 * (1 - color)],
                          [0, 5 * (1 - color) + 1], [1, 5 * (1 - color) + 1], [2, 5 * (1 - color) + 1],
                          [3, 5 * (1 - color) + 1],
                          [4, 5 * (1 - color) + 1], [5, 5 * (1 - color) + 1], [6, 5 * (1 - color) + 1],
                          [7, 5 * (1 - color) + 1]]
