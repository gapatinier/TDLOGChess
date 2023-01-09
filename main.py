import pygame
from model import *
import config

#Menu page
pygame.init()
Screen1 = pygame.display.set_mode((500, 500))
width = Screen1.get_width()
height = Screen1.get_height()
white = (255, 255, 255)
black = (0,0,0)
Screen1.fill(white)
smallfont = pygame.font.SysFont('Corbel', 35)
smallfont1 = pygame.font.SysFont('Corbel', 16)
pygame.draw.rect(Screen1, black, (50, 250, 100, 50))
pygame.draw.rect(Screen1, black, (200, 250, 100, 50))
pygame.draw.rect(Screen1, black, (350, 250, 100, 50))
text = smallfont.render('Choose play mode', True, black)
text1 = smallfont1.render('Player vs Player', True, white)
text2 = smallfont1.render('Player vs AI', True, white)
text3 = smallfont1.render('AI vs AI', True, white)
Screen1.blit(text, (width/4,height/4))
Screen1.blit(text1, (50, 265))
Screen1.blit(text2, (215, 265))
Screen1.blit(text3, (375, 265))
# Title and Icon
pygame.display.set_caption("Chess")
icon = pygame.image.load(config.LOGO)
pygame.display.set_icon(icon)

# Running
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 50 + 100 > mouse[0] > 50 and 250 + 50 > mouse[1] > 250:
                    game_type = 0
                    running = False
                elif 200 + 100 > mouse[0] > 200 and 250 + 50 > mouse[1] > 250:
                    game_type = 1
                    running = False
                elif 350 + 100 > mouse[0] > 350 and 250 + 50 > mouse[1] > 250:
                    game_type = 2
                    running = False
                else:
                    running = True


    pygame.display.update()

#####################################################################################################
#Choose color page
if game_type == 1:
    pygame.init()
    Screen2 = pygame.display.set_mode((500, 500))

    white = (255, 255, 255)
    black = (0,0,0)
    Screen2.fill(white)
    smallfont = pygame.font.SysFont('Corbel', 35)
    text = smallfont.render('Choose color', True, black)
    # create a surface object, image is drawn on it.
    image1 = pygame.image.load(config.WHITE_KNIGHT).convert()
    image2 = pygame.image.load(config.BLACK_KNIGHT).convert()
    image1_width = image1.get_width()
    image1_height = image1.get_height()
    image2_width = image2.get_width()
    image2_height = image2.get_height()
    # Using blit to copy content from one surface to other
    Screen2.blit(image1, (100, 250))
    Screen2.blit(image2, (300, 250))
    Screen2.blit(text, (145, 125))
    # Title and Icon
    pygame.display.set_caption("Chess")
    icon = pygame.image.load(config.LOGO)
    pygame.display.set_icon(icon)
    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 100 + image1_width > mouse[0] > 100 and 250 + image1_height > mouse[1] > 250:
                    chosen_color = 0
                    running = False
                elif 300 + image2_width > mouse[0] > 300 and 250 + image2_height > mouse[1] > 250:
                    chosen_color = 1
                    running = False
                else:
                    running = True

        pygame.display.update()

#####################################################################################################
# Initialisation
pygame.init()

# Display
Screen = pygame.display.set_mode((500, 500))


# Title and Icon
pygame.display.set_caption("Chess")
icon = pygame.image.load(config.LOGO)
pygame.display.set_icon(icon)

# Running
running = True

# Display
#game_type = int(input("Press 0 for 2 human players or 1 for a human player"
                      #+ " and a computer player or 2 for 2 computer players"))
if game_type == 0:
    Game = Game(HumanPlayer(0), HumanPlayer(1))
elif game_type == 1:
    if chosen_color == 0:
        Game = Game(HumanPlayer(0), ComputerPlayer(1))
    else:
        Game = Game(ComputerPlayer(0), HumanPlayer(1))
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
                    if Game.players[Game.turn].type == 0:
                        [x, y] = pygame.mouse.get_pos()
                        [i0, j0] = [(x - 10) // 60, (y - 10) // 60]
                        if Game.promotion == 1:
                            new_piece = promotion(Game.promotion_col, Game.promotion_row, i0, j0, Game.turn)
                            if new_piece is not None:
                                Game.set_board(new_piece, Game.promotion_col, Game.promotion_row)
                                Game.promotion = 0
                                display_board(Screen, Game.board)
                                Game.turn = 1 - Game.turn
                        elif Game.players[Game.turn].state == 0 and choose_piece(Screen, Game.board,
                                                                               Game.turn, i0, j0):
                            # PIECE SELECTION
                            Game.players[Game.turn].state = 1 - Game.players[Game.turn].state
                            Selected_piece = Game.board[j0][i0]
                            Highlighted_pieces = [[i0, j0]]
                            for coords in Game.legal_moves(i0, j0):
                                highlight(coords[0], coords[1], Screen)
                                Highlighted_pieces.append(coords)
                        elif Game.players[Game.turn].state == 1 and Highlighted_pieces[0] == [i0, j0]:
                            # PIECE DESELECTION
                            display_board(Screen, Game.board)
                            Game.players[Game.turn].state = 1 - Game.players[Game.turn].state
                        elif Game.players[Game.turn].state == 1 and [i0, j0] in Highlighted_pieces:
                            # MOVE SELECTION
                            [i1, j1] = Highlighted_pieces[0]
                            Highlighted_pieces = []
                            Game.move(i1, j1, i0, j0)
                            Selected_piece = Pawn(color=None, ptype=PieceType.Pawn, value=1)
                            Game.players[Game.turn].state = 1 - Game.players[Game.turn].state
                            if Game.promotion == 0:
                                Game.turn = 1 - Game.turn
                            display_board(Screen, Game.board)
                            if Game.promotion == 1:
                                display_promotion(Game.promotion_col, Game.promotion_row, Game.turn, Screen)
                        elif Game.players[Game.turn].state == 1 \
                                and choose_piece(Screen, Game.board, Game.turn, i0, j0):
                            # PIECE RESELCTION
                            for [i, j] in Highlighted_pieces:
                                display_piece(Game.board, i, j, Screen)
                            Selected_piece = Game.board[j0][i0]
                            Highlighted_pieces = [[i0, j0]]
                            for coords in Game.legal_moves(i0, j0):
                                highlight(coords[0], coords[1], Screen)
                                Highlighted_pieces.append(coords)

                    else:
                        [i, j, i0, j0] = Game.players[Game.turn].play_smart_move_v1(Game)
                        Game.move(i0, j0, i, j)
                        Game.turn = 1 - Game.turn
                        display_board(Screen, Game.board)


        elif Game.check_legal_move():
            print("STALE MATE")
            Screen.fill((255, 255, 255))
        else:
            print("CHECK MATE")
            Screen.fill((0, 0, 0))

    pygame.display.update()
