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
        
    def draw_item_stats(name, cost, x, y):
        black = (0, 0, 0)
        foods = consumablse[name]['food']
        hps = consumablse[name]['hp']
        cost = ('Cost: {}'.format(cost))
        hp = ('Hp: {}'.format(hps))
        food = ('food: {}'.format(foods))
        x_1 = x+50
        x_2 = x_1+50
        draw_text(cost, bigfont, black, x, y, 40, 40)
        draw_text(hp, bigfont, black, x_1, y, 40, 40)
        draw_text(food, bigfont, black, x_2, y, 40, 40)

    def imges(name):
            img = pygame.image.load(consumablse[name]['img'])
            return img
            
    e_img = pygame.image.load("img/Exit_ton.jpg")
    bread_img = pygame.image.load("img\items\Food\Bread_img.png")
    partition_img = "img\items\Town\Tavern_partition_img.png"
    rum_img = pygame.image.load("img\items\Food\Rum_img.png")
    apple_img = pygame.image.load("img\items\Food\Apple_img.png")
    key_img = pygame.image.load("img\items\gold_key_image.jpg")
    bandit_img = pygame.image.load("img\Sprites\Idle\LightBandit_Idle_0.png")
    carrot_img = imges('carrot')
    cookie_img = imges('cookie')
    fish_img = imges('fish')
    magic_melon_img = imges('magic mellon')
    
    eit_button = Button(screen, screen_h, 0, e_img, 50, 50)
    bread_btn = Button(screen, 50, 100, bread_img, 50, 50)
    rum_btn = Button(screen, 50, 150, rum_img, 50, 50)
    apple_btn = Button(screen, 50, 200, apple_img, 50, 50)
    carrot_btn = Button(screen, 50, 250, carrot_img, 50, 50)
    cookie_btn = Button(screen, 50, 300, cookie_img, 50, 50)
    fish_btn = Button(screen, 50, 350, fish_img, 50, 50)
    mellon_btn = Button(screen, 50, 400, magic_melon_img, 50, 50)
    
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
        back_img = pygame.image.load("img\Inventory_image.png")
        back_img = pygame.transform.scale(back_img, (screen_width, screen_h))
        screen.blit(back_img, (0, 0))
        items_bar = "img\panel.png"
        money_bar = "img\money_panel.jpg"
        draw_img(items_bar, 0, 610, 800, 80)
        draw_img(money_bar, 0, 0, 250, 50)
        draw_img(partition_img, 390, -10, 30, 660)
        draw_text(str(plr.money), bigfont, (255, 255, 0), 60, 10, 80, 25)

        #fill basket
        for i in basket:
                img = entire_items[i]['img']
                xe = basket.index(i)+1
                x = xe*60
                y = 620
                draw_img(img, x, y, 50, 50)

        for i in quest_list:
                x = quest_range[i]
                if on: 
                        if x.draw(True):
                                on = False

        # stores the (x,y) coordinates into
        # the variable as a tuple
        mouse = pygame.mouse.get_pos()
        if eit_button.draw():
            page = True
            return page
            screen = pygame.display.set_mode((window_width, window_height))
            run = False
        shop_items('bread', 3, bread_btn.draw(), 4)
        draw_item_stats('bread', 3, 100, 100)
        shop_items('rum', 5, rum_btn.draw(), 3)
        draw_item_stats('rum', 5, 100, 150)
        shop_items('apple', 6, apple_btn.draw(), 4)
        draw_item_stats('apple', 6, 100, 200)
        shop_items('carrot', 3, carrot_btn.draw(), 4)
        draw_item_stats('carrot', 3, 100, 250)
        shop_items('cookie', 4, cookie_btn.draw(), 4)
        draw_item_stats('cookie', 4, 100, 300)
        shop_items('fish', 5, fish_btn.draw(), 4)
        draw_item_stats('fish', 5, 100, 350)
        shop_items('magic mellon', 16, mellon_btn.draw(), 4)
        draw_item_stats('magic mellon', 16, 100, 400)
        # updates the frames of the game
        pygame.display.update()

