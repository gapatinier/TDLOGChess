class Piece:

    def __init__(self, color, i, j):
        self._color = color
        self._row = i
        self._col = j
        self._alive = 1
        self._type = ""

    def color(self):
        return self._color

    def alive(self):
        return self._alive

    def die(self, player):
        for piece in player.pieces:
            if self.cords == piece.cords:
                piece.alive = 0

    def defend(self, board):
        pass

    def move(self, board, i, j, game):
        player2 = game.players[1 - board.turn]
        if self._type != "pawn":
            if [i, j] in self.defend(board):
                board.board[self._row][self._col] = Pawn(None, self._row, self._col)
                eaten_piece = board.board[i][j]
                board.board[i][j] = self
                if board.check_legal_move(game):
                    self._row = i
                    self._col = j
                    eaten_piece.die(player2)
                    return True
                else:
                    board.board[self._row][self._col] = self
                    board.board[i][j] = eaten_piece
            return False
        else:
            if [i, j] in self.defend(board) and board.board[i][j].color == 1 - self._color:
                board.board[self._row][self._col] = Pawn(None, self._row, self._col)
                eaten_piece = board.board[i][j]
                board.board[i][j] = self
                self._row = i
                self._col = j
                eaten_piece.die(player2)
                return True
            else:
                if self.color == 0:
                    k = 1
                else:
                    k = -1
                if [i, j] == [self._row + k, self._col] and board.board[self._row + k][self._col].color is None:
                    board.board[self._row][self._col] = Pawn(None, self._row, self._col)
                    board.board[i][j] = self
                    return True
                elif [i, j] == [self._row + 2*k, self._col] and board.board[self._row + 2*k][self._col].color is None:
                    board.board[self._row][self._col] = Pawn(None, self._row, self._col)
                    board.board[i][j] = self
                    return True
            return False

    def cords(self):
        return [self._row, self._col]


class King(Piece):

    type = "king"

    def __init__(self, color, i, j):
        Piece.__init__(self, color, i, j)
        self._moved = 0

    def defend(self, board):
        krange = [-1, 0, 1]
        defend = []
        for i in krange:
            for j in krange:
                if not i or not j:
                    row = self._row + i
                    col = self._col + j
                    if -1 < row < 8 and -1 < col < 8:
                        defend += [row, col]
        return defend


class Queen(Piece):

    type = "queen"

    def defend(self, board):
        defend = []
        i = 1
        while self._row + i < 8 and self._col + i < 8 and board.board[self._row + i][self._col].color is None:
            defend += [self._row + i, self._col + i]
            i += 1
        if self._row + i < 8 and self._col + i < 8 and board.board[self._row + i][self._col].color == 1 - self._color:
            defend += [self._row + i, self._col + i]

        i = 1
        while self._row - i > -1 and self._col - i > -1 and board.board[self._row - i][self._col].color is None:
            defend += [self._row - i, self._col - i]
            i += 1
        if self._row - i > -1 and self._col - i > -1 and board.board[self._row - i][self._col].color == 1 - self._color:
            defend += [self._row - i, self._col - i]

        i = 1
        while self._row - i > -1 and self._col + i < 8 and board.board[self._row][self._col + i].color is None:
            defend += [self._row - i, self._col + i]
            i += 1
        if self._row - i > -1 and self._col + i < 8 and board.board[self._row][self._col + i].color == 1 - self._color:
            defend += [self._row - i, self._col + i]

        i = 1
        while self._row + i < 8 and self._col - i > -1 and board.board[self._row][self._col - i].color is None:
            defend += [self._row + i, self._col - i]
            i += 1
        if self._row + i < 8 and self._col - i > -1 and board.board[self._row][self._col - i].color == 1 - self._color:
            defend += [self._row + i, self._col - i]

        i = 1
        while self._row + i < 8 and board.board[self._row + i][self._col].color is None:
            defend += [self._row + i, self._col]
            i += 1
        if self._row + i < 8 and board.board[self._row + i][self._col].color == 1 - self._color:
            defend += [self._row + i, self._col]

        i = 1
        while self._row - i > -1 and board.board[self._row - i][self._col].color is None:
            defend += [self._row - i, self._col]
            i += 1
        if self._row - i > -1 and board.board[self._row - i][self._col].color == 1 - self._color:
            defend += [self._row - i, self._col]

        i = 1
        while self._col + i < 8 and board.board[self._row][self._col + i].color is None:
            defend += [self._row, self._col + i]
            i += 1
        if self._col + i < 8 and board.board[self._row][self._col + i].color == 1 - self._color:
            defend += [self._row, self._col + i]

        i = 1
        while self._row - i > -1 and board.board[self._row][self._col - i].color is None:
            defend += [self._row, self._col - 1]
            i += 1
        if self._row - i > -1 and board.board[self._row][self._col - i].color == 1 - self._color:
            defend += [self._row, self._col - 1]

        return defend


class Rook(Piece):

    type = "rook"

    def __init__(self, color, i, j):
        Piece.__init__(self, color, i, j)
        self._moved = 0

    def defend(self, board):
        defend = []
        i = 1
        while self._row + i < 8 and board.board[self._row + i][self._col].color is None:
            defend += [self._row + i, self._col]
            i += 1
        if self._row + i < 8 and board.board[self._row + i][self._col].color == 1 - self._color:
            defend += [self._row + i, self._col]

        i = 1
        while self._row - i > -1 and board.board[self._row - i][self._col].color is None:
            defend += [self._row - i, self._col]
            i += 1
        if self._row - i > -1 and board.board[self._row - i][self._col].color == 1 - self._color:
            defend += [self._row - i, self._col]

        i = 1
        while self._col + i < 8 and board.board[self._row][self._col + i].color is None:
            defend += [self._row, self._col + i]
            i += 1
        if self._col + i < 8 and board.board[self._row][self._col + i].color == 1 - self._color:
            defend += [self._row, self._col + i]

        i = 1
        while self._row - i > -1 and board.board[self._row][self._col - i].color is None:
            defend += [self._row, self._col - 1]
            i += 1
        if self._row - i > -1 and board.board[self._row][self._col - i].color == 1 - self._color:
            defend += [self._row, self._col - 1]

        return defend


class Bishop(Piece):

    type = "bishop"

    def defend(self, board):
        defend = []
        i = 1
        while self._row + i < 8 and self._col + i < 8 and board.board[self._row + i][self._col].color is None:
            defend += [self._row + i, self._col + i]
            i += 1
        if self._row + i < 8 and self._col + i < 8 and board.board[self._row + i][self._col].color == 1 - self._color:
            defend += [self._row + i, self._col + i]

        i = 1
        while self._row - i > -1 and self._col - i > -1 and board.board[self._row - i][self._col].color is None:
            defend += [self._row - i, self._col - i]
            i += 1
        if self._row - i > -1 and self._col - i > -1 and board.board[self._row - i][self._col].color == 1 - self._color:
            defend += [self._row - i, self._col - i]

        i = 1
        while self._row - i > -1 and self._col + i < 8 and board.board[self._row][self._col + i].color is None:
            defend += [self._row - i, self._col + i]
            i += 1
        if self._row - i > -1 and self._col + i < 8 and board.board[self._row][self._col + i].color == 1 - self._color:
            defend += [self._row - i, self._col + i]

        i = 1
        while self._row + i < 8 and self._col - i > -1 and board.board[self._row][self._col - i].color is None:
            defend += [self._row + i, self._col - i]
            i += 1
        if self._row + i < 8 and self._col - i > -1 and board.board[self._row][self._col - i].color == 1 - self._color:
            defend += [self._row + i, self._col - i]

        return defend


class Knight(Piece):

    type = "knight"

    def defend(self, board):
        krange = [-2, -1, 1, 2]
        defend = []
        for i in krange:
            for j in krange:
                if (i + j) % 2 == 1:
                    row = self._row + i
                    col = self._col + j
                    if -1 < row < 8 and -1 < col < 8:
                        defend += [row, col]
        return defend


class Pawn(Piece):

    type = "pawn"

    def defend(self, board):
        defend = []
        if self._color == 0:
            i = 1
        else:
            i = -1
        for j in [-1, 1]:
            row = self._row + i
            col = self._col + j
            if -1 < row < 8 and -1 < col < 8:
                defend += [row, col]
        return defend


class Board:

    def __init__(self, turn):
        self._turn = turn
        self._board = [[Piece(None, i, j) for j in range(8)] for i in range(8)]
        color = 0
        self._board[0] = [Rook(color, 0, 0), Rook(color, 0, 7), Knight(color, 0, 1), Knight(color, 0, 6),
                          Bishop(color, 0, 2), Bishop(color, 0, 5), Queen(color, 0, 3), King(color, 0, 4)]
        self._board[1] = [Pawn(color, 1, 0), Pawn(color, 1, 1), Pawn(color, 1, 2), Pawn(color, 1, 3),
                          Pawn(color, 1, 4), Pawn(color, 1, 5), Pawn(color, 1, 6), Pawn(color, 1, 7)]
        color = 1
        self._board[7] = [Rook(color, 7, 0), Rook(color, 7, 7), Knight(color, 7, 1), Knight(color, 7, 6),
                          Bishop(color, 7, 2), Bishop(color, 7, 5), Queen(color, 7, 3), King(color, 7, 4)]
        self._board[6] = [Pawn(color, 6, 0), Pawn(color, 6, 1), Pawn(color, 6, 2), Pawn(color, 6, 3),
                          Pawn(color, 6, 4), Pawn(color, 6, 5), Pawn(color, 6, 6), Pawn(color, 6, 7)]

    def board(self):
        return self._board

    def turn(self):
        return self._turn

    def check_legal_move(self, game):

        player1 = game.players[self._turn]
        player2 = game.players[1 - self._turn]

        king_cords = player1.pieces[7].coords

        for piece in player2.pieces:
            if king_cords in piece.defend(self) and piece.alive:
                return False

        return True

    def next_turn(self):
        self._turn = 1 - self._turn
        return


class Player:

    def __init__(self, color):
        self._color = color
        if color == 0:
            self._pieces = [Rook(color, 0, 0), Rook(color, 0, 7), Knight(color, 0, 1), Knight(color, 0, 6),
                            Bishop(color, 0, 2), Bishop(color, 0, 5), Queen(color, 0, 3), King(color, 0, 4),
                            Pawn(color, 1, 0), Pawn(color, 1, 1), Pawn(color, 1, 2), Pawn(color, 1, 3),
                            Pawn(color, 1, 4), Pawn(color, 1, 5), Pawn(color, 1, 6), Pawn(color, 1, 7)]
        else:
            self._pieces = [Rook(color, 7, 0), Rook(color, 7, 7), Knight(color, 7, 1), Knight(color, 7, 6),
                            Bishop(color, 7, 2), Bishop(color, 7, 5), Queen(color, 7, 3), King(color, 7, 4),
                            Pawn(color, 6, 0), Pawn(color, 6, 1), Pawn(color, 6, 2), Pawn(color, 6, 3),
                            Pawn(color, 6, 4), Pawn(color, 6, 5), Pawn(color, 6, 6), Pawn(color, 6, 7)]

    def pieces(self):
        return self._pieces


class HumanPlayer(Player):
    pass


class ComputerPlayer(Player):
    pass


class Game:

    def __init__(self):
        self._board = Board(0)
        self._players = [Player, Player]

    def players(self):
        return self._players
