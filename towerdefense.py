import pygame
import sys

#future game class for the enitre game. 
class TowerDefense:
    def on_start(self):
        pass

def main():
    pygame.init()
    pygame.display.set_caption("Hello Bitches")
    
    #setting the size of the screen.
    screen = pygame.display.set_mode((800,800))

    game_is_running = True

    #main game loop
    while game_is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_is_running = False


if __name__ == "__main__":
    main()










