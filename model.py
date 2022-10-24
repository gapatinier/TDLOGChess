class Piece:

    def __init__(self, color, i, j):
        self._color = color
        self._row = i
        self._col = j


class King(Piece):

    def defend(self):
        krange = [-1, 0, 1]
        defend = []
        for i in krange:
            for j in krange:
                if not i or not j:
                    row = self._row + i
                    col = self._col + j
                    if -1 < row < 9 and -1 < col < 9:
                        defend += [row, col]
        return defend


class Queen(Piece):

    def defend(self, board):
        defend = []
        i = 1
        while self._row + i < 9 and self._col + i < 9 and board.board[self._row + i][self._col].color is None:
            defend += [self._row + i, self._col + i]
            i += 1

        i = 1
        while self._row - i > -1 and self._col - i > -1 and board.board[self._row - i][self._col].color is None:
            defend += [self._row - i, self._col - i]
            i += 1

        i = 1
        while self._row - i > -1 and self._col + i < 9 and board.board[self._row][self._col + i].color is None:
            defend += [self._row - i, self._col + i]
            i += 1

        i = 1
        while self._row + i < 9 and self._col - i > -1 and board.board[self._row][self._col - i].color is None:
            defend += [self._row + i, self._col - i]
            i += 1

        i = 1
        while self._row + i < 9 and board.board[self._row + i][self._col].color is None:
            defend += [self._row + i, self._col]
            i += 1

        i = 1
        while self._row - i > -1 and board.board[self._row - i][self._col].color is None:
            defend += [self._row - i, self._col]
            i += 1

        i = 1
        while self._col + i < 9 and board.board[self._row][self._col + i].color is None:
            defend += [self._row, self._col + i]
            i += 1

        i = 1
        while self._row - i > -1 and board.board[self._row][self._col - i].color is None:
            defend += [self._row, self._col - 1]
            i += 1

        return defend


class Rook(Piece):

    def defend(self, board):
        defend = []
        i = 1
        while self._row + i < 9 and board.board[self._row + i][self._col].color is None:
            defend += [self._row + i, self._col]
            i += 1

        i = 1
        while self._row - i > -1 and board.board[self._row - i][self._col].color is None:
            defend += [self._row - i, self._col]
            i += 1

        i = 1
        while self._col + i < 9 and board.board[self._row][self._col + i].color is None:
            defend += [self._row, self._col + i]
            i += 1

        i = 1
        while self._row - i > -1 and board.board[self._row][self._col - i].color is None:
            defend += [self._row, self._col - 1]
            i += 1

        return defend


class Bishop(Piece):

    def defend(self, board):
        defend = []
        i = 1
        while self._row + i < 9 and self._col + i < 9 and board.board[self._row + i][self._col].color is None:
            defend += [self._row + i, self._col + i]
            i += 1

        i = 1
        while self._row - i > -1 and self._col - i > -1 and board.board[self._row - i][self._col].color is None:
            defend += [self._row - i, self._col - i]
            i += 1

        i = 1
        while self._row - i > -1 and self._col + i < 9 and board.board[self._row][self._col + i].color is None:
            defend += [self._row - i, self._col + i]
            i += 1

        i = 1
        while self._row + i < 9 and self._col - i > -1 and board.board[self._row][self._col - i].color is None:
            defend += [self._row + i, self._col - i]
            i += 1

        return defend


class Knight(Piece):

    def defend(self):
        krange = [-2, -1, 1, 2]
        defend = []
        for i in krange:
            for j in krange:
                if (i+j) % 2 == 1:
                    row = self._row + i
                    col = self._col + j
                    if -1 < row < 9 and -1 < col < 9:
                        defend += [row, col]
        return defend


class Pawn(Piece):

    def defend(self):
        defend = []
        if self._color == 0:
            i = 1
        else:
            i = -1
        for j in [-1, 1]:
            row = self._row + i
            col = self._col + j
            if -1 < row < 9 and -1 < col < 9:
                defend += [row, col]
        return defend


class Board:

    def __init__(self, turn):
        self._turn = turn
        self._board = [[Piece(None, i, j) for j in range(8)] for i in range(8)]

    def board(self):
        return self._board


class Player:

    def __init__(self, color):
        self._color = color
        if color == 0:
            self._pieces = [Rook(color, 1, 1), Rook(color, 1, 8), Knight(color, 1, 2), Knight(color, 1, 7),
                            Bishop(color, 1, 3), Bishop(color, 1, 6), Queen(color, 1, 4), King(color, 1, 5),
                            Pawn(color, 2, 1), Pawn(color, 2, 2), Pawn(color, 2, 3), Pawn(color, 2, 4),
                            Pawn(color, 2, 5), Pawn(color, 2, 6), Pawn(color, 2, 7), Pawn(color, 2, 8)]
        else:
            self._pieces = [Rook(color, 8, 1), Rook(color, 8, 8), Knight(color, 8, 2), Knight(color, 8, 7),
                            Bishop(color, 8, 3), Bishop(color, 8, 6), Queen(color, 8, 4), King(color, 8, 5),
                            Pawn(color, 7, 1), Pawn(color, 7, 2), Pawn(color, 7, 3), Pawn(color, 7, 4),
                            Pawn(color, 7, 5), Pawn(color, 7, 6), Pawn(color, 7, 7), Pawn(color, 7, 8)]


class HumanPlayer(Player):

    pass


class ComputerPlayer(Player):

    pass
