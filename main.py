import pygame
from pygame.locals import *

# Initialisation
pygame.init()

# Display
screen = pygame.display.set_mode((500, 500))

# Colors
color = [(173, 216, 230), (0, 0, 255)]

# Title and Icon
pygame.display.set_caption("Chess")
icon = pygame.image.load("strategy.png")
pygame.display.set_icon(icon)

# Chess board
boardImg = pygame.image.load("chessboard.png")
boardImg = pygame.transform.scale(boardImg, (480, 480))

# Chess pieces
bbishop = pygame.image.load("bbishop.png")
wbishop = pygame.image.load("wbishop.png")
bknight = pygame.image.load("bknight.png")
wknight = pygame.image.load("wknight.png")
brook = pygame.image.load("brook.png")
wrook = pygame.image.load("wrook.png")
bqueen = pygame.image.load("bqueen.png")
wqueen = pygame.image.load("wqueen.png")
bking = pygame.image.load("bking.png")
wking = pygame.image.load("wking.png")
bpawn = pygame.image.load("bpawn.png")
wpawn = pygame.image.load("wpawn.png")

# Running
running = True

# Display
for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 1:
            screen.fill(color[0], (10+60*i, 10+60*j, 60, 60))
        else:
            screen.fill(color[1], (10 + 60 * i, 10 + 60 * j, 60, 60))
screen.blit(brook, (10, 10))
screen.blit(bknight, (70, 10))
screen.blit(bbishop, (130, 10))
screen.blit(bqueen, (190, 10))
screen.blit(bking, (250, 10))
screen.blit(bbishop, (310, 10))
screen.blit(bknight, (370, 10))
screen.blit(brook, (430, 10))

screen.blit(wrook, (10, 430))
screen.blit(wknight, (70, 430))
screen.blit(wbishop, (130, 430))
screen.blit(wqueen, (190, 430))
screen.blit(wking, (250, 430))
screen.blit(wbishop, (310, 430))
screen.blit(wknight, (370, 430))
screen.blit(wrook, (430, 430))

for i in range(8):
    screen.blit(bpawn, (10 + i*60, 70))
    screen.blit(wpawn, (10 + i*60, 370))
s = pygame.Surface((60, 60))
s.set_alpha(128)
s.fill((255, 0, 0))


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
                [x, y] = pygame.mouse.get_pos()
                [i, j] = [(x-10)//60, (y-10)//60]
                screen.blit(s, (10 + i*60, 10 + j*60, 60, 60))

    pygame.display.update()
