import pygame
from pygame.locals import *


WIDTH, HEIGHT = 1500, 1000
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
FPS = 60 #frames per second
frames_per_second = pygame.time.Clock()
frames_per_second.tick(FPS) #Setting the frame rate


class Rectangle:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Hunter's Tower Defense Game")
        self.font = pygame.font.SysFont('Arial', 35)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.screen.fill((WHITE))

    def draw_rectangle(self, color, x_pos, y_pos, width, height):
        self.rect = pygame.draw.rect(self.screen, color, (x_pos, y_pos, width, height))
    
    def add_text(self, text, color, x_pos, y_pos):
        self.screen.blit(self.font.render(text, True, color), (x_pos, y_pos))



def main():
    #boolean to check if game is running.
    game_is_running = True

    #start button for start menu.
    start_button = Rectangle()
    start_button.draw_rectangle(BLACK, 600, 600, 200, 125)
    start_button.add_text('START', WHITE, 640, 685)

    #start_button_label = game_font.render('START', False, (255,255,255))
    #screen.blit(start_button_label, (700, 400))
    #game window background and colors.
    #background = pygame.Surface((WIDTH, HEIGHT))
    #pygame.draw.rect(background, 'White', (0,0, WIDTH, HEIGHT))

    #game_state = 'start menu'
    #main game loop
    while game_is_running:
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_is_running = False

            #if game_state == 'start menu':
             #   if event.type == pygame.MOUSEBUTTONDOWN:
              #      pass
                    #if start_button.collidepoint(event.pos):
                        #game_state = 'game'


        #if game_state == 'start menu':
         #   pygame.draw.rect(screen, 'Red', start_button)
        #elif game_state == 'game':
         #   screen.blit(background, (0,0))
    pygame.quit()

if __name__ == "__main__":
    main()










