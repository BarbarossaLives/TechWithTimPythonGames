import pygame

pygame.init
BLACK = (0,0,0)
GREY = (128,128,128)
YELLOW = (255,255,0)


# !!!  can play with this size for production version
WIDTH, HEIGHT = 800,800
TILE_SIZE = 20

GRID_WIDTH = WIDTH/TILE_SIZE
GRID HEIGHT = HEIGHT/TILE_SIZE

FPS = 60

screen = pygame.display/pygame.display.set_mode(WIDTH, HEIGHT)

clock = pygame.time.Clock

# Main Loop
def main():
    running = Trwe
    
    while running:
        clock.tick(FPS)
        
        for event in pygame.event.get():
             