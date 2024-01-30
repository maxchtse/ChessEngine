"""
This is the main driver file. It is used to display current game state and to handle user input
"""

import pygame as p
import chessEngine  


WIDTH = HEIGHT  = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 
IMAGE = {}

"""
Initialize a global dir of images.
"""

def loadImages():
    pieces = ["bR", "bN", "bB", "bQ", "bK", "bp", "wR", "wN", "wB", "wQ", "wK", "wp"]
    for piece in pieces:
        IMAGE[piece] = p.transform.scale(p.image.load("assets/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
        # Note: access image by typing 'IMAGES['wp']'

"""
The main driver for the code. This will handle user input and update the graphics
"""

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color('white'))
    gs = chessEngine.GameState()
    loadImages()
    running = True

    # Keep track of the last selected location from the user (tuple: (row, col))
    sqSelected = () # No square is selected originally
    sqClicked = [] # Keep track of the user click (two tuple:[(6,4), (4,4)])

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()  # Return (x,y) location of the mouse
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                # Play undo the selection logic
                if sqClicked == (row, col):
                    sqSelected = () # Change the square selected back
                    sqClicked = [] # Clear player click
                sqSelected = (row, col)
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()
        

"""
These methods are for all the graphics within a game current state
"""
def drawGameState(screen, gs):
    drawBoard(screen) #Draw squares on the board
    drawPieces(screen, gs.board) #Draw pieces on top of those squares


"""
Draw squares on the board. The top left square is always light
"""
def drawBoard(screen):
    colors = [p.Color(255,248,220), p.Color(221,138,60)]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c)%2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


"""
Draw pieces on the board using the current GameState.board
"""
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--": #not empty square
                screen.blit(IMAGE[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

if __name__ == "__main__":
    main()