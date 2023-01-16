import pygame
import random
from enum import Enum
from dataclasses import dataclass, field
import config


class PieceType(Enum):
    King = 1
    Queen = 2
    Rook = 3
    Bishop = 4
    Knight = 5
    Pawn = 6


@dataclass(kw_only=True)
class Piece:
    """
    A piece is defined by :
    - its color (0 for white, 1 for black, None if it belongs to no one or is dead)
    - its type (str)
    - its black and white images for display
    - whether it has moved for castling rights and for pawns
    """

    color: int or None
    ptype: PieceType or None
    value: int or None
    images: list = field(default_factory=lambda: [])
    moved: int = 0

    def defend(self, board, i0, j0):
        """
        List of tiles the piece on the board on the tile [i0, j0] defends (to compute the king's legal moves)
        """


@dataclass(kw_only=True)
class King(Piece):
    ptype: PieceType = PieceType.King
    value: int = 20 or None
    images: list = field(default_factory=lambda: ["wking.png", "bking.png"])

    def defend(self, board, i0, j0):
        krange = [-1, 0, 1]
        defend = []
        for i in krange:
            for j in krange:
                if i != 0 or j != 0:
                    row = j0 + j
                    col = i0 + i
                    if check(col, row, board, 1):
                        defend += [[col, row]]
        return defend


@dataclass(kw_only=True)
class Queen(Piece):
    ptype: PieceType = PieceType.Queen
    value: int = 9 or None
    images: list = field(default_factory=lambda: ["wqueen.png", "bqueen.png"])

    def defend(self, board, i0, j0):
        defend = []
        directions = [[-1, -1], [-1, 1], [1, -1], [1, 1], [-1, 0], [0, -1], [1, 0], [0, 1]]
        for u in directions:
            check_direction(u, i0, j0, board, defend)

        return defend


@dataclass(kw_only=True)
class Rook(Piece):
    ptype: PieceType = PieceType.Rook
    value: int = 5 or None
    images: list = field(default_factory=lambda: ["wrook.png", "brook.png"])

    def defend(self, board, i0, j0):
        defend = []
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        for u in directions:
            check_direction(u, i0, j0, board, defend)

        return defend


@dataclass(kw_only=True)
class Bishop(Piece):
    ptype: PieceType = PieceType.Bishop
    value: int = 3 or None
    images: list = field(default_factory=lambda: ["wbishop.png", "bbishop.png"])

    def defend(self, board, i0, j0):
        defend = []
        directions = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
        for u in directions:
            check_direction(u, i0, j0, board, defend)

        return defend


@dataclass(kw_only=True)
class Knight(Piece):
    ptype: PieceType = PieceType.Knight
    value: int = 3 or None
    images: list = field(default_factory=lambda: ["wknight.png", "bknight.png"])

    def defend(self, board, i0, j0):
        krange = [-2, -1, 1, 2]
        defend = []
        for i in krange:
            for j in krange:
                if (i + j) % 2 == 1:
                    row = j0 + j
                    col = i0 + i
                    if check(col, row, board, 1):
                        defend += [[col, row]]
        return defend


@dataclass(kw_only=True)
class Pawn(Piece):
    ptype: PieceType = PieceType.Pawn
    value: int = 1 or None
    images: list = field(default_factory=lambda: ["wpawn.png", "bpawn.png"])

    def defend(self, board, i0, j0):
        defend = []
        if self.color == 0:
            j = -1
        else:
            j = 1
        for i in [-1, 1]:
            col = i0 + i
            row = j0 + j
            if check(col, row, board, 1):
                defend += [[col, row]]
        return defend


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


@dataclass(kw_only=True)
class Game:
    """
    A Game is defined by :
    - whose turn it is to play (0 if it's white's turn and 1 if it's black's turn)
    - a board matrice containing the pieces on the board (board[j][i] is the piece on column i and row j)
    - a list of 2 players
    - a list of 2 ints to indicate wether an en-passant is possible and on which tiles
    """

    turn: int = 0
    board: list = field(default_factory=lambda: Board)
    players: list = field(default_factory=lambda: [])
    en_passant: list = field(default_factory=lambda: [0, -1])
    promotion: int = 0
    promotion_row: int = 0
    promotion_col: int = 0

    def set_board(self, piece, i0, j0):
        """
        Changes the [i0, j0] tile on the board to a chosen piece
        """
        self.board[j0][i0] = piece

    def moves(self, i0, j0):
        """
        Returns the list of the tiles the piece on the [i0, j0] tile can move to without checking if it puts the
        player's own king in check
        """
        board = self.board
        defend = board[j0][i0].defend(board, i0, j0)
        colour = board[j0][i0].color
        moves = []
        if board[j0][i0].ptype != PieceType.Pawn:
            for [i, j] in defend:
                if board[j][i].color != colour:
                    moves.append([i, j])
        elif board[j0][i0].ptype == PieceType.Pawn and board[j0][i0].color is not None:
            for [i, j] in defend:
                if colour is not None and board[j][i].color == 1 - colour:
                    moves.append([i, j])
            k = 2 * colour - 1
            if board[j0 + k][i0].color is None:
                moves.append([i0, j0 + k])
                if not board[j0][i0].moved and board[j0 + 2 * k][i0].color is None:
                    moves.append([i0, j0 + 2 * k])
            if self.en_passant[0] and j0 == 3 + 4 * color and (
                    i0 == self.en_passant[1] - 1 or i0 == self.en_passant[1] + 1):
                moves.append([self.en_passant[1], 2 + 5 * color])
                self.en_passant[0] += 1

        return moves

    def check_legal_move(self):
        """
        Checks if a certain board state is legal (if the player whose turn it is can take the other player's king)
        """

        player1 = self.players[self.turn]
        player2 = self.players[1 - self.turn]

        king_cords = player1.coords[7]

        for k in range(16):
            if king_cords in player2.pieces[k].defend(self.board, player2.coords[k][0], player2.coords[k][1]) \
                    and not player2.pieces[k].color is None:
                return False

        return True

    def legal_moves(self, i0, j0):
        """
        Returns the list of legal moves the piece on the [i0, j0] tile can play
        """
        moves = self.moves(i0, j0)
        piece = self.board[j0][i0]
        legal_moves = []
        self.set_board(Pawn(color=None, ptype=PieceType.Pawn, value=1), i0, j0)
        player1 = self.players[self.turn]
        player2 = self.players[1 - self.turn]
        for [i, j] in moves:
            eaten_piece = self.board[j][i]
            player2.update_type(i, j, Pawn(color=None, ptype=PieceType.Pawn, value=1))
            player1.update_piece(i0, j0, i, j)
            self.update_player(player1, player1.color)
            self.update_player(player2, player2.color)
            self.set_board(piece, i, j)
            if self.check_legal_move():
                legal_moves.append([i, j])
            player1.update_piece(i, j, i0, j0)
            player2.update_type(i, j, eaten_piece)
            self.update_player(player1, player1.color)
            self.update_player(player2, player2.color)
            self.set_board(eaten_piece, i, j)
        self.set_board(piece, i0, j0)
        if piece.ptype == PieceType.King:
            self.castle_left(legal_moves)
            self.castle_right(legal_moves)
        return legal_moves

    def move(self, i0, j0, i, j):
        """
        Changes the board state and the player attributes when the piece on [i0, j0] moves to [i, j]
        """
        piece = self.board[j0][i0]
        moved = piece.moved
        piece.moved = 1
        self.set_board(Pawn(color=None, ptype=PieceType.Pawn, value=1), i0, j0)
        self.set_board(piece, i, j)
        colour = piece.color
        player1 = self.players[colour]
        player1.update_piece(i0, j0, i, j)
        player1.update_type(i, j, piece)
        player2 = self.players[1 - colour]
        player2.update_type(i, j, Pawn(color=None, ptype=PieceType.Pawn, value=1))
        self.update_player(player2, 1 - colour)
        if piece.ptype == PieceType.Pawn and j * (7 - j) == 0:
            if player1.type == 0:
                self.set_board(piece, i, j)
                self.promotion = 1
                self.promotion_col = i
                self.promotion_row = j
            else:
                self.set_board(Queen(color=colour), i, j)
                player1.update_type(i, j, Queen(color=colour))
        if piece.ptype == PieceType.King and [i, j] == [1, 7 * (1 - colour)] and not moved:
            player1.update_piece(0, 7 * (1 - colour), 2, 7 * (1 - colour))
            self.set_board(Pawn(color=None, ptype=PieceType.Pawn, value=1), 0, 7 * (1 - color))
            self.set_board(Rook(color=colour), 2, 7 * (1 - colour))
        if piece.ptype == PieceType.King and [i, j] == [6, 7 * (1 - colour)] and not moved:
            player1.update_piece(7, 7 * (1 - colour), 5, 7 * (1 - colour))
            self.set_board(Pawn(color=None, ptype=PieceType.Pawn, value=1), 7, 7 * (1 - colour))
            self.set_board(Rook(color=colour), 5, 7 * (1 - colour))
        self.update_player(player1, colour)
        if self.en_passant[0] == 2:
            player2.update_type(self.en_passant[1], 3 + colour, Pawn(color=None, ptype=PieceType.Pawn, value=1))
            self.update_player(player2, 1 - colour)
            self.set_board(Pawn(color=None, ptype=PieceType.Pawn, value=1), self.en_passant[1], 3 + colour)
        if piece.ptype == PieceType.Pawn and abs(j0 - j) == 2:
            self.en_passant = [1, i]
        else:
            self.en_passant = [0, -1]

    def update_player(self, player, colour):
        self.players[colour] = player

    def castle_left(self, legal_moves):
        """
        If the player whose turn it is can castle to the left, adds that move to legal_moves.
        """
        turn = self.turn
        board = self.board
        player1 = self.players[turn]
        player2 = self.players[1 - turn]
        if player1.pieces[7].moved or player1.pieces[0].moved or player1.pieces[0].color is None:
            return
        yes = True
        for i in [3, 2, 1]:
            yes = yes and board[7 * (1 - player1.color)][i].color is None
            if yes:
                king_cords = [i, 7 * (1 - player1.color)]
                for k in range(16):
                    if king_cords in player2.pieces[k].defend(self.board, player2.coords[k][0],
                                                              player2.coords[k][1]) and not player2.pieces[
                                                                                                k].color is None:
                        yes = False

        if yes:
            legal_moves.append([1, 7 * (1 - player1.color)])

    def castle_right(self, legal_moves):
        """
        If the player whose turn it is can castle to the right, adds that move to legal_moves.
        """
        turn = self.turn
        board = self.board
        player1 = self.players[turn]
        player2 = self.players[1 - turn]
        if player1.pieces[7].moved + player1.pieces[1].moved == 0 and player1.pieces[1].color is not None:
            yes = True
            for i in [5, 6]:
                yes = yes and board[7 * (1 - player1.color)][i].color is None
                if yes:
                    yes = yes and board[7 * (1 - player1.color)][i].color is None
                    if yes:
                        king_cords = [i, 7 * (1 - player1.color)]
                        for k in range(16):
                            if king_cords in player2.pieces[k].defend(self.board, player2.coords[k][0],
                                                                      player2.coords[k][1]) and not \
                                    player2.pieces[k].color is None:
                                yes = False
            if yes:
                legal_moves.append([6, 7 * (1 - player1.color)])

    def check_stalemate(self):
        """
        Returns True if the player whose turn it is still has a legal move and False otherwise.
        """
        player = self.players[self.turn]
        pieces = player.pieces
        coords = player.coords
        moves = []
        k = 0
        while moves == [] and k < 16:
            if pieces[k].color is not None:
                moves = self.legal_moves(coords[k][0], coords[k][1])
            k += 1
        return moves == []


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


@dataclass(kw_only=True)
class Player:
    """
    A player is defined by :
    - their color (0 for white, 1 for black)
    - a list of all their pieces
    - a list of coordinates of each piece
    - the state of their turn
    """

    color: int or None
    type: int
    pieces: list = field(default_factory=lambda: [])
    coords: list = field(default_factory=lambda: [])
    state: int = 0

    def update_piece(self, i0, j0, i, j):
        for k in range(16):
            if [i0, j0] == self.coords[k]:
                self.coords[k] = [i, j]

    def update_type(self, i0, j0, piece):
        for k in range(16):
            if [i0, j0] == self.coords[k]:
                self.pieces[k] = piece


@dataclass(kw_only=True)
class HumanPlayer(Player):
    type: int = 0


@dataclass(kw_only=True)
class ComputerPlayer(Player):
    type: int = 1

    def play_random_move(self, game):
        k = random.randint(0, 15)
        legal_moves = game.legal_moves(self.coords[k][0], self.coords[k][1])
        while self.pieces[k].color is None or legal_moves == []:
            k = random.randint(0, 15)
            legal_moves = game.legal_moves(self.coords[k][0], self.coords[k][1])
        move = random.sample(legal_moves, 1)[0]
        return move + self.coords[k]

    def play_smart_move_v1(self, game):
        smart_moves = []
        max_val = -20
        defended_tiles = []
        player2 = game.players[1 - self.color]
        board = game.board
        pieces = player2.pieces
        coords = player2.coords
        for k in range(16):
            if pieces[k].color is not None:
                defended_tiles += pieces[k].defend(board, coords[k][0], coords[k][1])

        for k in range(16):
            if self.pieces[k].color is not None:
                legal_moves = game.legal_moves(self.coords[k][0], self.coords[k][1])
                for [i, j] in legal_moves:
                    val = (self.coords[k] in defended_tiles) * self.pieces[k].value
                    if board[j][i].color is not None:
                        val = val + board[j][i].value
                    if [i, j] in defended_tiles:
                        val = val - self.pieces[k].value
                    game.turn = 1 - game.turn
                    if not game.check_legal_move():
                        val = val + 1
                    game.turn = 1 - game.turn
                    if val > max_val:
                        max_val = val
                        smart_moves = [[i, j, k]]
                    if val == max_val:
                        smart_moves.append([i, j, k])
        [i, j, k] = random.sample(smart_moves, 1)[0]
        return [i, j, self.coords[k][0], self.coords[k][1]]


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
    if piece.color is None:
        return
    screen.blit(pygame.image.load(config.p.joinpath(piece.images[piece.color])), (10 + i * 60, 10 + j * 60))


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
    if board[j][i].color == turn:
        highlight(i, j, screen)
        return True
    return False


def check(i, j, board, m):
    """
    Checks if (i,j) is on the board, and if m is equal to 0 checks if there is a piece on (i,j)
    """
    return -1 < i < 8 and -1 < j < 8 and (board[j][i].color is None or m)


def check_direction(u, i, j, board, defend):
    """
    Returns the list of coordinates (i,j) along the direction u that are on the board
    """
    k = 1
    while check(i + k * u[0], j + k * u[1], board, 0):
        defend += [[i + k * u[0], j + k * u[1]]]
        k += 1
    if check(i + k * u[0], j + k * u[1], board, 1):
        defend += [[i + k * u[0], j + k * u[1]]]


def display_promotion(i, j, color, screen):
    k = 7 - j
    l = color * 2 - 1
    piece1 = Queen(color=color)
    screen.fill((255, 255, 0), (10 + 60 * i, 10 + 60 * k, 60, 60))
    screen.blit(pygame.image.load(config.p.joinpath(piece1.images[color])), (10 + i * 60, 10 + k * 60))
    piece2 = Rook(color=color)
    screen.fill((255, 255, 0), (10 + 60 * i, 10 + 60 * (k + l), 60, 60))
    screen.blit(pygame.image.load(config.p.joinpath(piece2.images[color])), (10 + i * 60, 10 + (k + l) * 60))
    piece3 = Bishop(color=color)
    screen.fill((255, 255, 0), (10 + 60 * i, 10 + 60 * (k + 2 * l), 60, 60))
    screen.blit(pygame.image.load(config.p.joinpath(piece3.images[color])), (10 + i * 60, 10 + (k + 2 * l) * 60))
    piece4 = Knight(color=color)
    screen.fill((255, 255, 0), (10 + 60 * i, 10 + 60 * (k + 3 * l), 60, 60))
    screen.blit(pygame.image.load(config.p.joinpath(piece4.images[color])), (10 + i * 60, 10 + (k + 3 * l) * 60))


def promotion(i, j, i0, j0, color):
    """
    Lets the player choose to which piece his pawn will promote
    """
    k = 7 - j
    l = color * 2 - 1
    if l == -1:
        if i0 == i and k + 1 > j0 > k - 4:
            if j0 - k == 0:
                return Queen(color=color)
            elif j0 - k == -1:
                return Rook(color=color)
            elif j0 - k == -2:
                return Bishop(color=color)
            elif j0 - k == -3:
                return Knight(color=color)
    if l == 1:
        if i0 == i and k + 4 > j0 > k - 1:
            if j0 - k == 0:
                return Queen(color=color)
            elif j0 - k == 1:
                return Rook(color=color)
            elif j0 - k == 2:
                return Bishop(color=color)
            elif j0 - k == 3:
                return Knight(color=color)
    return None
