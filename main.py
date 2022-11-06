import pygame
import sys


WIDTH, HEIGHT = 1500, 1000
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
FPS = 60 #frames per second

class Rectangle:
    def _init_(self):
        pygame.init()
        pygame.display.set_caption("Hunter's Tower Defense Game")
        self.font = pygame.font.SysFont('Times New Roman', 35)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.screen.fill((WHITE))
        pygame.display.update()

    def draw_rectangle(self, color, x_pos, y_pos, width, height):
        self.rect = pygame.draw.rect(self.screen, color, (x_pos, y_pos, width, height))
        pygame.display.update()
    
    def add_text(self, text, color, x_pos, y_pos):
        self.screen.blit(self.font.render(text, True, color, (x_pos, y_pos)))
        pygame.display.update()




def main():
    #Setting the refresh rate
    frames_per_second = pygame.time.Clock()

    #boolean to check if game is running.
    game_is_running = True

    #start button for start menu.
    #start_button = pygame.Rect(700, 400, 10, 10)
    #start_button_label = game_font.render('START', False, (255,255,255))
    #screen.blit(start_button_label, (700, 400))








    test = Rectangle()
    test.draw_rectangle()
    test.add_text('hello', BLACK, 400, 600)






    #game window background and colors.
    #background = pygame.Surface((WIDTH, HEIGHT))
    #pygame.draw.rect(background, 'White', (0,0, WIDTH, HEIGHT))

    game_state = 'start menu'
    #main game loop
    while game_is_running:
        frames_per_second.tick(FPS)
        #pygame.display.update()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_is_running = False

            if game_state == 'start menu':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass
                    #if start_button.collidepoint(event.pos):
                        #game_state = 'game'


        if game_state == 'start menu':
            pygame.draw.rect(screen, 'Red', start_button)
        elif game_state == 'game':
            screen.blit(background, (0,0))




    pygame.quit()

if __name__ == "__main__":
    main()










