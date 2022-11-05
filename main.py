import pygame
import sys
from menu import start_menu


def main():
    pygame.init()

    WIDTH, HEIGHT = 1500, 1000
    screen_color = (73, 232, 255) #Light Blue
    FPS = 60 #frames per second

    pygame.display.set_caption("Hunter's Tower Defense Game")

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(screen_color)    

    test_surface = pygame.Surface((100,200))
    test_surface.fill('Red')

    #Setting the refresh rate
    frames_per_second = pygame.time.Clock()

    #boolean to check if game is running.
    game_is_running = True

    #main game loop
    while game_is_running:
        start_menu()
        frames_per_second.tick(FPS)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_is_running = False
        screen.blit(test_surface, (0,0))
    pygame.quit()

if __name__ == "__main__":
    main()










