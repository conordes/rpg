import pygame
from maps_helper import*
import player
from all_items import*

class equip_screen(pygame.sprite.Sprite):
    def __init__(self, game, x, y, screen):
        self.game = game
        self._layer = 11
        self.groups = self.game.all_sprites, self.game.UI
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.screen = screen

        self.x = x
        self.y = y
        self.width = 400
        self.height = 150
        self.on = True
        self.font = pygame.font.SysFont('SH Pinscher Regular', 30)

        self.make()
    def draw(self, x, y, on):
        self.x = x
        self.y = y
        self.on = on
        self.make()
        if self.on:
            self.image = pygame.Surface([self.width, self.height])
            self.image.set_colorkey((0, 0, 0))
            self.image.blit(self.bar_img, (0, 0))
            for i in self.armour_img:
                img = pygame.image.load(i).convert()
                img = pygame.transform.scale(img, (50, 50))
                img.set_colorkey((255, 255, 255))
                fx = self.armour_img.index(i)+1
                sx = fx*50
                y = 30
                if sx>350:
                    y = 90
                    fx = self.armour_img.index(i)-2
                    sx = fx*50
                self.image.blit(img, (sx, y))


    def make(self):
        self.image = pygame.Surface([self.width, self.height])
        self.image.set_colorkey((0, 0, 0))
        self.bar_img = pygame.image.load("img\Inventory_image.png")
        self.bar_img = pygame.transform.scale(self.bar_img, (self.width, self.height))

        self.armour_img = [armour_items[plr.armour['helmet']['name']]['img'], armour_items[plr.armour['chestplate']['name']]['img'],
                           armour_items[plr.armour['gauntlets']['name']]['img'], armour_items[plr.armour['leggings']['name']]['img'],
                           armour_items[plr.armour['boots']['name']]['img'], entire_items[plr.weap]['img']]
        
        self.armour_n = [armour_items[plr.armour['helmet']['name']]['item'], armour_items[plr.armour['chestplate']['name']]['img'],
                           armour_items[plr.armour['gauntlets']['name']]['img'], armour_items[plr.armour['leggings']['name']]['img'],
                           armour_items[plr.armour['boots']['name']]['img'], entire_items[plr.weap]['img']]
    
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def draw_text(self, text, x, y):
        img = self.font.render(text, True, green)
        img = pygame.transform.scale(img, (50, 20)) 
        self.screen.blit(img, (x, y))







