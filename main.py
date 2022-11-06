import pygame
import sys


def main():
    pygame.init()

    WIDTH, HEIGHT = 1500, 1000
    screen_color = (73, 232, 255) #Light Blue
    FPS = 60 #frames per second

    pygame.display.set_caption("Hunter's Tower Defense Game")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(screen_color)   

    #Setting the refresh rate
    frames_per_second = pygame.time.Clock()

    #boolean to check if game is running.
    game_is_running = True

    #start button for start menu.
    start_button = pygame.Rect(400, 300, 50, 50)
    test_button = pygame.Rect(700, 700, 100, 100)


    game_state = 'start menu'
    #main game loop
    while game_is_running:
        frames_per_second.tick(FPS)
        pygame.display.update()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_is_running = False

            if game_state == 'start menu':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button.collidepoint(event.pos):
                        game_state = 'game'


        if game_state == 'start menu':
            pygame.draw.rect(screen, 'Red', start_button)
        elif game_state == 'game':
            pygame.draw.rect(screen, 'Green', test_button)




    pygame.quit()

if __name__ == "__main__":
    main()










