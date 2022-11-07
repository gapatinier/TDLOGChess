import pygame


class Piece:
    """
    A piece is defined by :
    - its color (0 for white, 1 for black, None if it belongs to no one or is dead)
    - its type (str)
    - its black and white images for display
    - wether or not it has moved for castling rights and for pawns
    """

    def __init__(self, color):
        self._color = color
        self._type = ""
        self._images = pygame.image
        self._moved = 0

    def color(self):
        return self._color

    def type(self):
        return self._type

    def images(self):
        return self._images

    def moved(self):
        return self._moved

    def die(self):
        """
        When a piece is eaten, its color is turned to None
        """
        self._color = None

    def defend(self, board, i0, j0):
        """
        List of tiles the piece on the board on the tile [i0, j0] defends (to compute the king's legal moves)
        """

    def move(self):
        """"
        Changes a piece's status to moved
        """
        self._moved = 1


class King(Piece):

    def __init__(self, color):
        Piece.__init__(self, color)
        self._images = [pygame.image.load("wking.png"), pygame.image.load("bking.png")]
        self._type = "king"

    def defend(self, board, i0, j0):
        krange = [-1, 0, 1]
        defend = []
        for i in krange:
            for j in krange:
                if i or j:
                    row = j0 + j
                    col = i0 + i
                    if -1 < row < 8 and -1 < col < 8:
                        defend += [[col, row]]
        return defend


class Queen(Piece):

    def __init__(self, color):
        Piece.__init__(self, color)
        self._images = [pygame.image.load("wqueen.png"), pygame.image.load("bqueen.png")]
        self._type = "queen"

    def defend(self, board, i0, j0):
        defend = []
        i = 1
        while j0 + i < 8 and i0 + i < 8 and board[j0 + i][i0 + i].color() is None:
            defend += [[i0 + i, j0 + i]]
            i += 1
        if j0 + i < 8 and i0 + i < 8:
            defend += [[i0 + i, j0 + i]]

        i = 1
        while j0 - i > -1 and i0 - i > -1 and board[j0 - i][i0 - i].color() is None:
            defend += [[i0 - i, j0 - i]]
            i += 1
        if j0 - i > -1 and i0 - i > -1:
            defend += [[i0 - i, j0 - i]]

        i = 1
        while j0 - i > -1 and i0 + i < 8 and board[j0 - i][i0 + i].color() is None:
            defend += [[i0 + i, j0 - i]]
            i += 1
        if j0 - i > -1 and i0 + i < 8:
            defend += [[i0 + i, j0 - i]]

        i = 1
        while j0 + i < 8 and i0 - i > -1 and board[j0 + i][i0 - i].color() is None:
            defend += [[i0 - i, j0 + i]]
            i += 1
        if j0 + i < 8 and i0 - i > -1:
            defend += [[i0 - i, j0 + i]]

        i = 1
        while j0 + i < 8 and board[j0 + i][i0].color() is None:
            defend += [[i0, j0 + i]]
            i += 1
        if j0 + i < 8:
            defend += [[i0, j0 + i]]

        i = 1
        while j0 - i > -1 and board[j0 - i][i0].color() is None:
            defend += [[i0, j0 - i]]
            i += 1
        if j0 - i > -1:
            defend += [[i0, j0 - i]]

        i = 1
        while i0 + i < 8 and board[j0][i0 + i].color() is None:
            defend += [[i0 + i, j0]]
            i += 1
        if i0 + i < 8:
            defend += [[i0 + i, j0]]

        i = 1
        while i0 - i > -1 and board[j0][i0 - i].color() is None:
            defend += [[i0 - i, j0]]
            i += 1
        if i0 - i > -1:
            defend += [[i0 - i, j0]]

        return defend


class Rook(Piece):

    def __init__(self, color):
        Piece.__init__(self, color)
        self._images = [pygame.image.load("wrook.png"), pygame.image.load("brook.png")]
        self._type = "rook"

    def defend(self, board, i0, j0):
        defend = []
        i = 1
        while j0 + i < 8 and board[j0 + i][i0].color() is None:
            defend += [[i0, j0 + i]]
            i += 1
        if j0 + i < 8:
            defend += [[i0, j0 + i]]

        i = 1
        while j0 - i > -1 and board[j0 - i][i0].color() is None:
            defend += [[i0, j0 - i]]
            i += 1
        if j0 - i > -1:
            defend += [[i0, j0 - i]]

        i = 1
        while i0 + i < 8 and board[j0][i0 + i].color() is None:
            defend += [[i0 + i, j0]]
            i += 1
        if i0 + i < 8:
            defend += [[i0 + i, j0]]

        i = 1
        while i0 - i > -1 and board[j0][i0 - i].color() is None:
            defend += [[i0 - i, j0]]
            i += 1
        if i0 - i > -1:
            defend += [[i0 - i, j0]]

        return defend


class Bishop(Piece):

    def __init__(self, color):
        Piece.__init__(self, color)
        self._images = [pygame.image.load("wbishop.png"), pygame.image.load("bbishop.png")]
        self._type = "bishop"

    def defend(self, board, i0, j0):
        defend = []
        i = 1
        while j0 + i < 8 and i0 + i < 8 and board[j0 + i][i0 + i].color() is None:
            defend += [[i0 + i, j0 + i]]
            i += 1
        if j0 + i < 8 and i0 + i < 8:
            defend += [[i0 + i, j0 + i]]

        i = 1
        while j0 - i > -1 and i0 - i > -1 and board[j0 - i][i0 - i].color() is None:
            defend += [[i0 - i, j0 - i]]
            i += 1
        if j0 - i > -1 and i0 - i > -1:
            defend += [[i0 - i, j0 - i]]

        i = 1
        while j0 - i > -1 and i0 + i < 8 and board[j0 - i][i0 + i].color() is None:
            defend += [[i0 + i, j0 - i]]
            i += 1
        if j0 - i > -1 and i0 + i < 8:
            defend += [[i0 + i, j0 - i]]

        i = 1
        while j0 + i < 8 and i0 - i > -1 and board[j0 + i][i0 - i].color() is None:
            defend += [[i0 - i, j0 + i]]
            i += 1
        if j0 + i < 8 and i0 - i > -1:
            defend += [[i0 - i, j0 + i]]

        return defend


class Knight(Piece):

    def __init__(self, color):
        Piece.__init__(self, color)
        self._images = [pygame.image.load("wknight.png"), pygame.image.load("bknight.png")]
        self._type = "knight"

    def defend(self, board, i0, j0):
        krange = [-2, -1, 1, 2]
        defend = []
        for i in krange:
            for j in krange:
                if (i + j) % 2 == 1:
                    row = j0 + j
                    col = i0 + i
                    if -1 < row < 8 and -1 < col < 8:
                        defend += [[col, row]]
        return defend


class Pawn(Piece):

    def __init__(self, color):
        Piece.__init__(self, color)
        self._images = [pygame.image.load("wpawn.png"), pygame.image.load("bpawn.png")]
        self._type = "pawn"

    def defend(self, board, i0, j0):
        defend = []
        if self._color == 0:
            j = -1
        else:
            j = 1
        for i in [-1, 1]:
            col = i0 + i
            row = j0 + j
            if -1 < row < 8 and -1 < col < 8:
                defend += [[col, row]]
        return defend


class Game:
    """
    A Game is defined by :
    - whose turn it is to play (0 if it's white's turn and 1 if it's black's turn)
    - a board matrice containing the pieces on the board (board[j][i] is the piece on column i and row j)
    - a list of 2 players
    - a list of 2 ints to indicate wether an en-passant is possible and on which tiles
    """

    def __init__(self):
        self._turn = 0
        self._board = [[Piece(None) for i in range(8)] for j in range(8)]
        color = 1
        self._board[0] = [Rook(color), Knight(color), Bishop(color), Queen(color),
                          King(color), Bishop(color), Knight(color), Rook(color)]
        self._board[1] = [Pawn(color), Pawn(color), Pawn(color), Pawn(color),
                          Pawn(color), Pawn(color), Pawn(color), Pawn(color)]
        color = 0
        self._board[7] = [Rook(color), Knight(color), Bishop(color), Queen(color),
                          King(color), Bishop(color), Knight(color), Rook(color)]
        self._board[6] = [Pawn(color), Pawn(color), Pawn(color), Pawn(color),
                          Pawn(color), Pawn(color), Pawn(color), Pawn(color)]
        self._players = [Player(0), Player(1)]
        self._en_passant = [0, -1]

    def turn(self):
        return self._turn

    def board(self):
        return self._board

    def players(self):
        return self._players

    def set_board(self, piece, i0, j0):
        """
        Changes the [i0, j0] tile on the board to a chosen piece
        """
        self._board[j0][i0] = piece

    def moves(self, i0, j0):
        """
        Returns the list of the tiles the piece on the [i0, j0] tile can move to without checking if it puts the
        player's own king in check
        """
        board = self.board()
        defend = board[j0][i0].defend(board, i0, j0)
        color = board[j0][i0].color()
        moves = []
        if board[j0][i0].type() != "pawn":
            for [i, j] in defend:
                if board[j][i].color() != color:
                    moves.append([i, j])
        elif board[j0][i0].type() == "pawn":
            for [i, j] in defend:
                if color is not None and board[j][i].color() == 1 - color:
                    moves.append([i, j])
            k = 2 * color - 1
            if board[j0 + k][i0].color() is None:
                moves.append([i0, j0 + k])
                if board[j0 + 2 * k][i0].color() is None and not board[j0][i0].moved():
                    moves.append([i0, j0 + 2 * k])
            if self._en_passant[0] and j0 == 3 + 4*color and (i0 == self._en_passant[1] - 1 or i0 == self._en_passant[1] + 1):
                moves.append([self._en_passant[1], 2 + 5*color])
                self._en_passant[0] += 1

        return moves

    def check_legal_move(self):
        """
        Checks if a certain board state is legal (if the player whose turn it is can take the other player's king)
        """

        player1 = self._players[self._turn]
        player2 = self._players[1 - self._turn]

        king_cords = player1.coords()[7]

        for k in range(16):
            if king_cords in player2.pieces()[k].defend(self._board, player2.coords()[k][0], player2.coords()[k][1]) \
                    and not player2.pieces()[k].color() is None:
                return False

        return True

    def legal_moves(self, i0, j0):
        """
        Returns the list of legal moves the piece on the [i0, j0] tile can play
        """
        moves = self.moves(i0, j0)
        piece = self._board[j0][i0]
        legal_moves = []
        self.set_board(Pawn(None), i0, j0)
        player1 = self._players[self._turn]
        player2 = self._players[1 - self._turn]
        for [i, j] in moves:
            eaten_piece = self._board[j][i]
            player2.update_type(i, j, Pawn(None))
            player1.update_piece(i0, j0, i, j)
            self.update_player(player1, player1.color())
            self.update_player(player2, player2.color())
            self.set_board(piece, i, j)
            if self.check_legal_move():
                legal_moves.append([i, j])
            player1.update_piece(i, j, i0, j0)
            player2.update_type(i, j, eaten_piece)
            self.update_player(player1, player1.color())
            self.update_player(player2, player2.color())
            self.set_board(eaten_piece, i, j)
        self.set_board(piece, i0, j0)
        if piece.type() == "king":
            self.castle_left(legal_moves)
            self.castle_right(legal_moves)
        return legal_moves

    def move(self, i0, j0, i, j):
        """
        Changes the board state and the player attributes when the piece on [i0, j0] moves to [i, j]
        """
        piece = self._board[j0][i0]
        piece.move()
        self.set_board(Pawn(None), i0, j0)
        self.set_board(piece, i, j)
        color = piece.color()
        player1 = self._players[color]
        player1.update_piece(i0, j0, i, j)
        player2 = self._players[1 - color]
        player2.update_type(i, j, Pawn(None))
        self.update_player(player2, 1 - color)
        if piece.type() == "pawn" and j*(7-j) == 0:
            player1.update_type(i, j, Queen(color))
            self.set_board(Queen(color), i, j)
        if piece.type() == "king" and [i, j] == [1, 7 * (1 - color)]:
            player1.update_piece(0, 7 * (1 - color), 2, 7 * (1 - color))
            self.set_board(Pawn(None), 0, 7 * (1 - color))
            self.set_board(Rook(color), 2, 7 * (1 - color))
        if piece.type() == "king" and [i, j] == [6, 7 * (1 - color)]:
            player1.update_piece(7, 7 * (1 - color), 5, 7 * (1 - color))
            self.set_board(Pawn(None), 7, 7 * (1 - color))
            self.set_board(Rook(color), 5, 7 * (1 - color))
        self.update_player(player1, color)
        if self._en_passant[0] == 2:
            player2.update_type(self._en_passant[1], 3 + color, Pawn(None))
            self.update_player(player2, 1-color)
            self.set_board(Pawn(None), self._en_passant[1], 3 + color)
        if piece.type() == "pawn" and abs(j0 - j) == 2:
            self._en_passant = [1, i]
        else:
            self._en_passant = [0, -1]

    def next_turn(self):
        self._turn = 1 - self._turn
        return

    def update_player(self, player, color):
        self._players[color] = player

    def update_board(self, board):
        self._board = board

    def castle_left(self, legal_moves):
        turn = self.turn()
        board = self.board()
        player1 = self.players()[turn]
        player2 = self.players()[1 - turn]
        [i0, j0] = player1.coords()[7]
        if player1.pieces()[7].moved() + player1.pieces()[0].moved() == 0 and player1.pieces()[0].color() is not None:
            yes = True
            for i in [3, 2, 1]:
                yes = yes and board[7 * (1 - player1.color())][i].color() is None
                if yes:
                    king_cords = [i, 7 * (1 - player1.color())]
                    for k in range(16):
                        if king_cords in player2.pieces()[k].defend(self._board, player2.coords()[k][0], player2.coords()[k][1]) and not player2.pieces()[k].color() is None:
                            yes = False

            if yes:
                legal_moves.append([1, 7 * (1 - player1.color())])

    def castle_right(self, legal_moves):
        turn = self.turn()
        board = self.board()
        player1 = self.players()[turn]
        player2 = self.players()[1 - turn]
        [i0, j0] = player1.coords()[7]
        if player1.pieces()[7].moved() + player1.pieces()[1].moved() == 0 and player1.pieces()[1].color() is not None:
            yes = True
            for i in [5, 6]:
                yes = yes and board[7 * (1 - player1.color())][i].color() is None
                if yes:
                    yes = yes and board[7 * (1 - player1.color())][i].color() is None
                    if yes:
                        king_cords = [i, 7 * (1 - player1.color())]
                        for k in range(16):
                            if king_cords in player2.pieces()[k].defend(self._board, player2.coords()[k][0], player2.coords()[k][1]) and not player2.pieces()[k].color() is None:
                                yes = False
            if yes:
                legal_moves.append([6, 7 * (1 - player1.color())])

    def check_stalemate(self):
        player = self._players[self._turn]
        pieces = player.pieces()
        coords = player.coords()
        moves = []
        k = 0
        while moves == [] and k < 16:
            if pieces[k].color() is not None:
                moves += self.legal_moves(coords[k][0], coords[k][1])
            k += 1
        return moves == []


class Player:
    """
    A player is defined by :
    - their color (0 for white, 1 for black)
    - a list of all their pieces
    - a list of coordinates of each piece
    - the state of their turn
    """

    def __init__(self, color):
        self._color = color
        self._pieces = [Rook(color), Rook(color), Knight(color), Knight(color),
                        Bishop(color), Bishop(color), Queen(color), King(color),
                        Pawn(color), Pawn(color), Pawn(color), Pawn(color),
                        Pawn(color), Pawn(color), Pawn(color), Pawn(color)]
        self._coords = [[0, 7 * (1 - color)], [7, 7 * (1 - color)], [1, 7 * (1 - color)], [6, 7 * (1 - color)],
                        [2, 7 * (1 - color)], [5, 7 * (1 - color)], [3, 7 * (1 - color)], [4, 7 * (1 - color)],
                        [0, 5 * (1 - color) + 1], [1, 5 * (1 - color) + 1], [2, 5 * (1 - color) + 1],
                        [3, 5 * (1 - color) + 1],
                        [4, 5 * (1 - color) + 1], [5, 5 * (1 - color) + 1], [6, 5 * (1 - color) + 1],
                        [7, 5 * (1 - color) + 1]]
        self._state = 0

    def color(self):
        return self._color

    def pieces(self):
        return self._pieces

    def coords(self):
        return self._coords

    def state(self):
        return self._state

    def change_state(self):
        self._state = 1 - self._state

    def update_pieces(self, pieces):
        self._pieces = pieces

    def update_coords(self, coords):
        self._coords = coords

    def update_piece(self, i0, j0, i, j):
        coords = self.coords()
        for k in range(16):
            if [i0, j0] == coords[k]:
                coords[k] = [i, j]
        self.update_coords(coords)

    def update_type(self, i0, j0, piece):
        coords = self.coords()
        pieces = self.pieces()
        for k in range(16):
            if [i0, j0] == coords[k]:
                pieces[k] = piece
        self.update_pieces(pieces)


class HumanPlayer(Player):
    pass


class ComputerPlayer(Player):
    pass


# Colors
Color = [(173, 216, 230), (0, 0, 255)]

s = pygame.Surface((60, 60))
s.set_alpha(128)
s.fill((255, 0, 0))
[i1, j1] = [0, 0]

# Display functions


def highlight(i, j, screen):
    """
    Highlights the piece on the board using its coordinates
    """
    screen.blit(s, (10 + i * 60, 10 + j * 60))


def display_piece(board, i, j, screen):
    """
    Displays a piece on the board using its coordinates and its color

    """
    piece = board[j][i]
    screen.fill(Color[1 - (i + j) % 2], (10 + 60 * i, 10 + 60 * j, 60, 60))
    if not piece.color() is None:
        screen.blit(piece.images()[piece.color()], (10 + i * 60, 10 + j * 60))


def display_board(screen, board):
    """
    Diplays all the pieces on the board
    """
    for i in range(8):
        for j in range(8):
            display_piece(board, i, j, screen)


def choose_piece(screen, board, turn, i, j):
    """
    Highlights the selected piece on the board and returns True if it belongs to the player whose turn it is
    """
    if board[j][i].color() == turn:
        highlight(i, j, screen)
        return True
    return False
