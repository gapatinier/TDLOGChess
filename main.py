from model import *

# Initialisation
pygame.init()

# Display
Screen = pygame.display.set_mode((500, 500))


# Title and Icon
pygame.display.set_caption("Chess")
icon = pygame.image.load("strategy.png")
pygame.display.set_icon(icon)


# Running
running = True

# Display
game_type = int(input("Press 0 for 2 human players or 1 for a human player and a computer player or 2 for 2 computer players"))
if game_type == 0:
    Game = Game(HumanPlayer(0), HumanPlayer(1))
elif game_type == 1:
    Game = Game(HumanPlayer(0), ComputerPlayer(1))
else:
    Game = Game(ComputerPlayer(0), ComputerPlayer(1))
display_board(Screen, Game.board())
Selected_piece = Piece(None)
Highlighted_pieces = []


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if not Game.check_stalemate():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    if Game.players()[Game.turn()] == 0 :
                        [x, y] = pygame.mouse.get_pos()
                        [i0, j0] = [(x-10)//60, (y-10)//60]
                        if Game.players()[Game.turn()].state() == 0 and choose_piece(Screen, Game.board(), Game.turn(), i0, j0):
                            # PIECE SELECTION
                            Game.players()[Game.turn()].change_state()
                            Selected_piece = Game.board()[j0][i0]
                            Highlighted_pieces = [[i0, j0]]
                            for coords in Game.legal_moves(i0, j0):
                                highlight(coords[0], coords[1], Screen)
                                Highlighted_pieces.append(coords)
                        elif Game.players()[Game.turn()].state() == 1 and Highlighted_pieces[0] == [i0, j0]:
                            # PIECE DESELECTION
                            display_board(Screen, Game.board())
                            Game.players()[Game.turn()].change_state()
                        elif Game.players()[Game.turn()].state() == 1 and [i0, j0] in Highlighted_pieces:
                            # MOVE SELECTION
                            [i1, j1] = Highlighted_pieces[0]
                            Highlighted_pieces = []
                            Game.move(i1, j1, i0, j0)
                            Selected_piece = Pawn(None)
                            Game.players()[Game.turn()].change_state()
                            Game.next_turn()
                            display_board(Screen, Game.board())
                        elif Game.players()[Game.turn()].state() == 1\
                                and choose_piece(Screen, Game.board(), Game.turn(), i0, j0):
                            # PIECE RESELCTION
                            for [i, j] in Highlighted_pieces:
                                display_piece(Game.board(), i, j, Screen)
                            Selected_piece = Game.board()[j0][i0]
                            Highlighted_pieces = [[i0, j0]]
                            for coords in Game.legal_moves(i0, j0):
                                highlight(coords[0], coords[1], Screen)
                                Highlighted_pieces.append(coords)

                else:
                    [i0, j0, i, j] = Game.players()[Game.turn()].play_turn()
                    Game.move(i, j, i0, j0)
            if Game.check_legal_move():
                print("STALE MATE")
                Screen.fill((255, 255, 255))
            else:
                Screen.fill((0, 0, 0))

    pygame.display.update()
