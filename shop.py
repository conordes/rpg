import pygame
import sys
from maps_helper import*
import random
from player import*
pygame.init()
pygame.font.init()
plr.__init__(plr)
page = False
#create global variable basket
global basket
basket = []
basket = list(dict.fromkeys(basket))
# initializing the constructor
pygame.init()
screen_h = 700  
  
# white color
color = (255,255,255)
  
  
# defining a font
smallfont = pygame.font.SysFont('Corbel',35)
bigfont =  pygame.font.SysFont('Times New Roman', 26)
  
# rendering a text written in
# this font
class Button():
        def __init__(self, surface, x, y, image, size_x, size_y):
                white = (255, 255, 255)
                self.image = pygame.transform.scale(image, (size_x, size_y)).convert_alpha()
                self.image.set_colorkey((0, 0, 0))
                self.image.set_colorkey((255, 255, 255))
                self.rect = self.image.get_rect()
                self.rect.topleft = (x, y)
                self.clicked = False
                self.surface = surface
        def draw(self):
                white = (255, 255, 255)
                action = False

                #get mouse position
                pos = pygame.mouse.get_pos()

                #check mouseover and clicked conditions
                if self.rect.collidepoint(pos):
                        if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                                action = True
                                self.clicked = True

                if pygame.mouse.get_pressed()[0] == 0:
                        self.clicked = False

                #draw button
                self.surface.blit(self.image, (self.rect.x, self.rect.y))
                return action
def shop_items(item, cost, button, amount):
        if button:
                if plr.money >= 3:
                        plr.item_img.append(entire_items[item]['img'])
                        plr.items.append(entire_items[item]['item'])
                        consumablse[item]['amount'] += amount
                        plr.money -= cost
                        basket.append(item)
class quest:
        def __init__(self, x, y, mis, text_a, screen, img):
# mis_type : 1=in a list, 2=kill something
                black = (0, 0, 0)
                self.text = bigfont.render(text_a, True, black)
                self.x = x
                self.y = y
                self.screen = screen
                self.mission = mis
                self.quest_button = Button(self.screen, self.x+300, self.y, img, 50, 50)
                
        def draw(self, a):
                hit = False
                if a:
                        if self.quest_button.draw():
                                plr.quest = self.mission
                                hit = True
                        self.screen.blit(self.text, (self.x, self.y))
                return hit        
                
def start_bar(bar):
    screen = pygame.display.set_mode((screen_width, screen_h))
    def draw_img(img, x, y, size_x, size_y):
        img = pygame.image.load(img)
        image = pygame.transform.scale(img, (size_x, size_y))
        image.set_colorkey((255, 255, 255))
        screen.blit(image, (x, y))

    def draw_text(text, font, text_col, x, y, size_x, size_y):
        img = font.render(text, True, text_col)
        img = pygame.transform.scale(img, (size_x, size_y)) 
        screen.blit(img, (x, y))
        


    def imges(name):
            img = pygame.image.load(entire_items[name]['img'])
            return img
            
    e_img = pygame.image.load("img/Exit_ton.jpg")

    
    eit_button = Button(screen, screen_h, 0, e_img, 50, 50)

    
    run = True
    quest_slot = True
    quest_range = {'gold key':quest(420, 60, 'gold key', 'find the gold key', screen, key_img),
                   'kill bandits': quest(420, 110, 'kill bandits', 'kill the bandits to free the town', screen, bandit_img)}
    on = True
    while run:   
        for ev in pygame.event.get():     
            if ev.type == pygame.QUIT:
                pygame.quit()
                
                      	
        # fills the screen with a color


        # stores the (x,y) coordinates into
        # the variable as a tuple
        mouse = pygame.mouse.get_pos()
        if eit_button.draw():
            page = True
            return page
            screen = pygame.display.set_mode((window_width, window_height))
            run = False

        # updates the frames of the game
        pygame.display.update()
