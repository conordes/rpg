import random
import time
import os
import pygame
import math
from maps_helper import*
from player import*
from all_items import*
from npc_sprite import*
from speech_bubble import*

pygame.init()
doorz.__init__(doorz)
class player(pygame.sprite.Sprite):
    def __init__(self, game, x, y, screen):
        self.game = game
        self.screen = screen
        self._layer = player_layer
        self.groups = self.game.all_sprites, self.game.player
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x*tilesize
        self.y = y*tilesize
        self.width = tilesize
        self.heigth = tilesize

        self.x_change = 0
        self.y_change = 0
        self.tavern_hits = 0

        self.facing = 'down'
        self.frame = {
            'right':0,
            'left':0,
            'up':0,
            'down':0}
        self.moving = False
    
        self.imgs = plr.clas_img
        image = pygame.transform.scale(self.imgs, (tilesize, tilesize))
        self.image = image
        self.image.set_colorkey((255, 255, 255))

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.opened = False

    def update(self):
        self.movement()
        self.collide_enemy()


        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')

        self.x_change = 0
        self.y_change = 0

    def animate(self):
        if self.frame[self.facing]>=9 and self.facing == 'right':
            self.frame[self.facing] = 0
        if self.frame[self.facing]>=9 and self.facing == 'left':
            self.frame[self.facing] = 0 
        if self.frame[self.facing]>=6 and self.facing == 'up':
            self.frame[self.facing] = 0
        self.right_animations = []
        self.rs = []
        self.left_animations = []
        self.ls = []
        self.up_animations = []
        self.us = []
        for i in range(10):
            self.rs.append((pygame.image.load(f"img\Sprites\HeroKnight\Run\HeroKnight_Run_{i}.png")))
        for i in self.rs:
            self.right_animations.append(pygame.transform.scale(i, (tilesize, tilesize)))
        for i in range(10):
            self.ls.append((pygame.image.load(f"img\Sprites\HeroKnight\Run\HeroKnight_Run_{i}_left.png")))
        for i in self.ls:
            self.left_animations.append(pygame.transform.scale(i, (tilesize, tilesize)))
        for i in range(7):
            self.us.append((pygame.image.load(f"img\Sprites\HeroKnight\Run\HeroKnight_Run_{i}_up.png")))
        for i in self.us:
            self.up_animations.append(pygame.transform.scale(i, (tilesize, tilesize)))
        if self.facing == 'right':
            self.image = self.right_animations[self.frame[self.facing]]
            self.frame[self.facing] +=1
        if self.facing == 'left':
            self.image = self.left_animations[self.frame[self.facing]]
            self.frame[self.facing] +=1
        if self.facing == 'up':
            self.image = self.up_animations[self.frame[self.facing]]
            self.frame[self.facing] +=1
        if self.moving == False:
            self.image = plr.clas_img
        
    def movement(self):
        self.animate()
        if plr.inventory_not_open:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.moving = True
                for sprite in self.game.all_sprites:
                    sprite.rect.x += plr.stamina
                self.x_change -= plr.stamina
                self.facing = 'left'
                self.animate()
            if keys[pygame.K_RIGHT]:
                self.moving = True
                for sprite in self.game.all_sprites:
                    sprite.rect.x -= plr.stamina
                self.x_change += plr.stamina
                self.facing = 'right'
                self.animate()
            if keys[pygame.K_UP]:
                self.moving = True
                for sprite in self.game.all_sprites:
                    sprite.rect.y += plr.stamina
                self.y_change -= plr.stamina
                self.facing = 'up'
                self.animate()
            if keys[pygame.K_DOWN]:
                self.moving = True
                for sprite in self.game.all_sprites:
                    sprite.rect.y -= plr.stamina
                self.y_change += plr.stamina
                self.facing = 'right'
                self.animate()
            self.moving =False
        
    def collide_enemy(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, True)
        if hits:
            plr.xp += 50
            r.__init__(r)
            r.g
            plr.hp -= 1
        rega = pygame.sprite.spritecollide(self, self.game.chest, False)
        t = armour_name[0:10]
        t = [x for x in t if x not in plr.armour_list]
        ite = ['staff', 'staff', 'flame sword', 'electric bow', 'dagger o death', 'bow', 'sword', 'dagger']                                                                                                          
        if rega:
            print('                                                                                                                                                                                                                                                              ')
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_o:
                        plr.xp += 25 + random.randint(1, 25)
                        weapon_rand = random.choice(ite)
                        armour_rand = random.choice(t)
                        plr.item_img.append(entire_items[weapon_rand]['img'])
                        plr.items.append(entire_items[weapon_rand]['item'])
                        plr.item_img.append(entire_items[armour_rand]['img'])
                        plr.items.append(entire_items[armour_rand]['item'])
                        plr.potions += 2+random.randint(1, 8)
                        pygame.sprite.spritecollide(self, self.game.chest, True)
                        plr.money += 15+random.randint(5, 10)
            
        f = pygame.sprite.spritecollide(self, self.game.furniture, False)
        chest_choosers = False
        if f and doorz.room == 0:
           chest_choosers = True
           print('                                                                                                                                                                                                                                                               ')
        if chest_choosers:
            print('                                                                                                                                                                                                                                                              ')
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_o:
                        take = random.choice([True, False, False])
                        pygame.sprite.spritecollide(self, self.game.furniture, True)
                        if take:
                            plr.item_img.append(entire_items['gold key']['img'])
                            plr.items.append(entire_items['gold key']['item'])
                            print("finish")
                            pygame.sprite.spritecollide(self, self.game.inventory, True)

                        else:
                            print("gone")
                            pygame.sprite.spritecollide(self, self.game.inventory, True)
    def collide_blocks(self, direction):
        if direction == 'x':
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                    for sprite in self.game.all_sprites:
                       sprite.rect.x += plr.stamina+1
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
                    for sprite in self.game.all_sprites:
                       sprite.rect.x -= plr.stamina-1
            

        if direction == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                    for sprite in self.game.all_sprites:
                       sprite.rect.y += plr.stamina+1
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
                    for sprite in self.game.all_sprites:
                       sprite.rect.y -= plr.stamina-1




        unlock_a = pygame.sprite.spritecollide(self, self.game.house_a, False)
        if unlock_a and plr.weap == 'gold key' and doorz.locked == True:
            doorz.room = 1
            doorz.unlocked = True
        unlock = pygame.sprite.spritecollide(self, self.game.door, False)

        if unlock and plr.weap == 'gold key' and doorz.locked == False:
            doorz.room = 0
            
            doorz.unlocked = True

        tavern = pygame.sprite.spritecollide(self, self.game.tavern, False)
        if tavern:
            doorz.room = 2
            doorz.unlocked = True
        tavern_door = pygame.sprite.spritecollide(self, self.game.tavern_door, False)
        if tavern_door:
            doorz.room = 0	
            doorz.unlocked = True
        tavern_shop = pygame.sprite.spritecollide(self, self.game.bar_counter, False)
        if tavern_shop and self.tavern_hits<=0:
            self.tavern_hits +=1
            f.__init__(f)
            f.b
            tavern_shop = False
        forest = pygame.sprite.spritecollide(self, self.game.forest_gate, False)
        if forest:
            doorz.room = 3
            doorz.unlocked = True
        gate = pygame.sprite.spritecollide(self, self.game.gate, False)
        if gate:
            doorz.room = 0	
            doorz.unlocked = True
            
            
class attack(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        white = (255, 255, 255)
        self.game = game
        self._layer = player_layer
        self.groups = self.game.all_sprites, self.game.attacks
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x
        self.y = y
        self.width = tilesize
        self.height = tilesize
        
        self.animation_loop = 0

        x = plr.clas[0]
        y = x.upper()
        z = len(plr.clas)
        f = plr.clas[1:z]
        d = ('{}{}'.format(y, f))
        self.image = pygame.image.load(f'img\Sprites\Attack\{d}_attack.png')
        self.image.set_colorkey(white)
        
        self.rect = self.image.get_rect()
        self.rect.y = self.y
        self.rect.x = self.x
        plr.x = self.rect.x

    def update(self):
        self.animate()
        self.collide()
        plr.x = self.rect.x
    def animate(self):
        direction = self.game.player.facing
        animation_direct = [self.image, plr.clas_img]

        if direction == 'up':
            self.image = animation_direct[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 2:
                self.kill()

        if direction == 'down':
            self.image = animation_direct[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 2:
                self.kill()

        if direction == 'left':
            self.image = animation_direct[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 2:
                self.kill()

        if direction == 'right':
            self.image = animation_direct[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 2:
                self.kill()

class text:
    def __init__(self, text, x, y, screen, col):
        self.screen = screen
        font =  pygame.font.SysFont('Times New Roman', 26)
        text_col = col
        self.image = font.render(text, True, text_col)
        self.screen.blit(self.image, (x, y))
        
