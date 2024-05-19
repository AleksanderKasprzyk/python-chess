import pygame as p
from Chess import chessengine

width = height = 720
dimension = 8
sq_size = height // dimension
max_fps = 15
Chessimages = {}

def loadimages():
    pieces = ["whitepawn", "whiterook", "whiteknight", "whitebishop", "whitequeen", "whiteking", "blackpawn",
              "blackrook", "blackknight", "blackbishop", "blackking", "blackqueen"]
    for piece in pieces:
        Chessimages[piece] = p.transform.scale(p.image.load("E:/Python projects/Chessimages/" + piece + ".png"), (sq_size, sq_size))

def main():
    p.init()
    screen = p.display.set_mode((width, height))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = chessengine.gamestate()
    loadimages()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

        drawgamestate(screen, gs)
        clock.tick(max_fps)
        p.display.flip()

def drawgamestate(screen, gs):
    drawboard(screen)
    drawpieces(screen, gs.board)

def drawboard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(dimension):
        for c in range(dimension):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(c * sq_size, r*sq_size, sq_size, sq_size))

def drawpieces(screen, board):
    for r in range(dimension):
        for c in range(dimension):
            piece = board[r][c]
            if piece != "--":
                screen.blit(Chessimages[piece], p.Rect(c * sq_size, r * sq_size, sq_size, sq_size))

if __name__ == "__main__":
    main()