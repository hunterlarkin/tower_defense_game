import pygame

WIDTH, HEIGHT = 800, 800
SCREEN_COLOR = (73, 232, 255) #Light Blue
FPS = 60 #frames per second

pygame.display.set_caption("Tower Defense Game")


def draw_main_game_window():
    #setting the size of the screen and drawing the background.
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    SCREEN.fill(SCREEN_COLOR)
    pygame.display.update()

def main():
    pygame.init()

    #Setting the refresh rate
    frames_per_second = pygame.time.Clock()

    #boolean to check if game is running.
    game_is_running = True
    #main game loop
    while game_is_running:
        frames_per_second.tick(FPS)
        draw_main_game_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_is_running = False
        
    pygame.quit()

if __name__ == "__main__":
    main()










