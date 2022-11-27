import pygame
from pygame.locals import *
import player
import towers


WIDTH, HEIGHT = 1500, 1250
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
ORANGE = (255,140,0)

FPS = 60 #frames per second
clock = pygame.time.Clock()
frames_per_second = str(clock.get_fps())

class Rectangle:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Hunter's Tower Defense Game")
        pygame.mouse.set_visible = True
        self.font = pygame.font.SysFont('Arial', 30)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.screen.fill((ORANGE))

    def draw_rectangle(self, color, x_pos, y_pos, width, height):
        self.rect = pygame.draw.rect(self.screen, color, (x_pos, y_pos, width, height))
    
    def create_Rect_object(self, x_pos, y_pos, width, height):
        return pygame.rect.Rect(x_pos, y_pos, width, height)
    
    def add_text(self, text, color, x_pos, y_pos):
        self.screen.blit(self.font.render(text, True, color), (x_pos, y_pos))


def main():
    #boolean to check if game is running.
    game_is_running = True

    #instantiating different class objects
    start_button = Rectangle()
    exit_button = Rectangle() 
    game_screen = Rectangle() 
    tower = Rectangle()
    fps_font = Rectangle()
    fps_display = fps_font.font.render(frames_per_second, False, (0,0,0))

    #rect object for tower/button instances.
    tower_rect_object = tower.create_Rect_object(1000, 670, 125, 125)
    start_rect_object = start_button.create_Rect_object(650, 300, 200, 125)   
    exit_rect_object = exit_button.create_Rect_object(650, 450, 200, 125)   

    #boolean if rect's are being dragged by cursor
    being_dragged = False

    game_state = 'start menu'
    #main game loop
    while game_is_running:
        fps_font.screen.blit(fps_display, (25, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_is_running = False

            if game_state == 'start menu':
                if event.type == pygame.MOUSEBUTTONDOWN:                                                      
                    if start_rect_object.collidepoint(event.pos):
                        game_state = 'game' #enters the game state
                    if exit_rect_object.collidepoint(event.pos):
                        game_is_running = False #quits the game if exit button is clicked  
                game_screen.screen.fill((ORANGE))                  


            if game_state == 'start menu':
                start_button.draw_rectangle(BLACK, start_rect_object.x, start_rect_object.y, start_rect_object.width, start_rect_object.height)
                start_button.add_text('START', WHITE, start_rect_object.x, start_rect_object.y)

                exit_button.draw_rectangle(BLACK, exit_rect_object.x, exit_rect_object.y, exit_rect_object.width, exit_rect_object.height)
                exit_button.add_text('EXIT', WHITE, exit_rect_object.x, exit_rect_object.y)
            
            elif game_state == 'game':
                #game screen drawing
                game_screen.draw_rectangle(BLUE, 0, 0, WIDTH, HEIGHT)
                game_screen.add_text('Welcome', WHITE, 1000, 70)

                #tower test rectangle
                #tower.draw_rectangle(BLACK, 1000, 670, 125, 125)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if tower_rect_object.collidepoint(event.pos):
                            being_dragged = True
                            mouse_x_pos, mouse_y_pos = event.pos
                            x_offset = (tower_rect_object.x - event.pos[0])
                            y_offset = (tower_rect_object.y - event.pos[1])


                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        being_dragged = False

                elif event.type == pygame.MOUSEMOTION:
                    if being_dragged:
                        tower_rect_object.x = (event.pos[0] + x_offset)
                        tower_rect_object.y = (event.pos[1] + y_offset)

                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        game_state = 'start menu'


                tower.draw_rectangle(BLACK, tower_rect_object.x, tower_rect_object.y, tower_rect_object.width, tower_rect_object.height)
        
        clock.tick(60)
        pygame.display.update()
            
    pygame.quit()

if __name__ == "__main__":
    main()










