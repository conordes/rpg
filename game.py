
import pygame
import time
import random
from maps import*
from player import*
pygame.mouse.set_cursor(*pygame.cursors.arrow)
pygame.init()
thanks for watching!
#create display window
black = (0, 0, 0)

class s:
    def __init__(self):
        self.tv = 0
        
        SCREEN_HEIGHT = 500
        SCREEN_WIDTH = 800
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
s = s()
pygame.display.set_caption('Button Demo')
#load button images

pygame.init()


start_img = pygame.image.load('img/start_btn.png')
exit_img = pygame.image.load('img/exit_btn.png')
def image():
    

    image = pygame.image.load("img\Sprites\Idle\Adventurer-idle-0.png")
    image = pygame.transform.scale(image, (200, 128))
    return image
class Button():
    def __init__(self, x, y, image, scale):

                width = image.get_width()
                height = image.get_height()
                self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
                self.rect = self.image.get_rect()
                self.rect.topleft = (x, y)
                self.clicked = False

                
    def draw(self):

        action = False

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                print("clicked")
        s.screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

def show_stat(text):

    base_font = pygame.font.Font(None,32)
    player_stat = base_font.render(text,True,(0,0,0))
    rect = pygame.draw.rect(s.screen, (black), (10, 390, 790, 70), 2)
    s.screen.blit(player_stat, (30, 410))

    
#game loop
def start_menu():
    start_button = Button(100, 200, start_img, 0.8)
    exit_button = Button(450, 200, exit_img, 0.8)
    player_maker_button = Button(320, 290, image(), 0.8)
    run = True
    while run:
        for event in pygame.event.get():
        #quit game
            if event.type == pygame.QUIT:
                run = False   
        text = plr.cls_tot
        s.screen.fill((202, 228, 241))

        if start_button.draw():
            start_map_game()
                    
        if exit_button.draw():
                run = False

        if player_maker_button.draw():
            start_game()

        show_stat(text)
        


        #event handler


        pygame.display.update()

    pygame.quit()

start_menu()
