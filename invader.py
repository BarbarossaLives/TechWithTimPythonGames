import pygame
import time
import random


# widow setup for a pygame game.  The imports are fairly standard also 
WIDTH = 1000
HEIGHT = 800

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Fire Dodge")

# smple game loop function
def main():
    run=True
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
    pygame.quit
    
    
    if __name__ == "__main__":
        main()