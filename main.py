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
        self.font = pygame.font.SysFont('Arial', 30)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.screen.fill((WHITE))

    def draw_rectangle(self, color, x_pos, y_pos, width, height):
        self.rect = pygame.draw.rect(self.screen, color, (x_pos, y_pos, width, height))
    
    def create_Rect_object(self, x_pos, y_pos, width, height):
        return pygame.Rect(x_pos, y_pos, width, height)
    
    def add_text(self, text, color, x_pos, y_pos):
        self.screen.blit(self.font.render(text, True, color), (x_pos, y_pos))

    def in_bounds(self, rect_object, event):        
        return rect_object.collidepoint(event)


def main():
    #boolean to check if game is running.
    game_is_running = True

    #start button object for the start menu.
    start_button = Rectangle()
    exit_button = Rectangle() 
    game_screen = Rectangle()   

    
    game_state = 'start menu'
    #main game loop
    while game_is_running:
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_is_running = False

            if game_state == 'start menu':
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    start_rect_object = start_button.create_Rect_object(650, 300, 200, 125)   
                    exit_rect_object = exit_button.create_Rect_object(650, 450, 200, 125)                                    
                    if start_button.in_bounds(start_rect_object, event.pos):
                        game_state = 'game'
                    if exit_button.in_bounds(exit_rect_object, event.pos):
                        game_is_running = False #quits the game if exit button is clicked
                    


        if game_state == 'start menu':
            start_button.draw_rectangle(BLACK, 650, 300, 200, 125)
            start_button.add_text('START', WHITE, 700, 340)

            exit_button.draw_rectangle(BLACK, 650, 450, 200, 125)
            exit_button.add_text('EXIT', WHITE, 715, 490)
            
        elif game_state == 'game':
            game_screen.draw_rectangle(BLUE, 0, 0, WIDTH, HEIGHT)
            game_screen.add_text('Welcome', WHITE, 700, 70)
            
    pygame.quit()

if __name__ == "__main__":
    main()










