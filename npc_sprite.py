import random
import pygame
from maps_helper import*
from player import*
from speech_bubble import*

class npc(pygame.sprite.Sprite):
    def __init__(self, game, x, y, image, screen, kert, tav, chosen_text):
        self.game = game
        self.screen = screen
        self._layer = enemy_layer
        self.groups = self.game.all_sprites, self.game.npc
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.tav = tav
        white = (255, 255, 255)

        self.x = x * tilesize
        self.y = y*tilesize
        self.width = tilesize
        self.height = tilesize
        self.chosen_text = chosen_text

        self.image = pygame.transform.scale(image, (42, 42))
        self.image.set_colorkey(white)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.x_change = 0
        self.y_change = 0
        self.movement_loop = 0
        self.frame = {
            'right':0,
            'left':0,
            'up':0,
            'down':0}

        self.speech_wiz1 = speech_bubble(self.game, self.rect.x, self.rect.y, 'find the gold key in the furniture use O', self.screen)
        self.speech_vil1 = speech_bubble(self.game, self.rect.x, self.rect.y, 'thanks for saving us', self.screen)
        self.speech_vil2 = speech_bubble(self.game, self.rect.x, self.rect.y, 'go to the tavern to get a mission', self.screen)
        self.facing = random.choice(['right', 'left', 'up', 'down'])
        self.max_travel = random.randint(10, 20)
        self.move = True
            
    def update(self):
        #speech
        self.player_hit = pygame.sprite.spritecollide(self, self.game.player, False)
        if self.tav:
            if self.move:
                self.movement()
            if doorz.room != 0:
                self.animate()
        self.speech()
        if self.player_hit:
            self.move = False
        else:
            self.move = True

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')
           
        self.x_change = 0
        self.y_change = 0

    def speech(self):
        if self.player_hit:
            if doorz.room == 0:
                self.speech_wiz1.draw('find the gold key in the furniture use O', self.rect.x, self.rect.y, True)
            elif doorz.room == 1:
                self.speech_vil1.draw(self.chosen_text, self.rect.x, self.rect.y, True)
        else:
            self.speech_wiz1.draw('find the gold key in the furniture use O', self.rect.x, self.rect.y, False)
            self.speech_vil1.draw(self.chosen_text, self.rect.x, self.rect.y, False)
    def animate(self):
        if self.frame[self.facing]>=4 and self.facing == 'right':
            self.frame[self.facing] = 0
        if self.frame[self.facing]>=4 and self.facing == 'left':
            self.frame[self.facing] = 0 
        if self.frame[self.facing]>=4 and self.facing == 'up':
            self.frame[self.facing] = 0
        if self.frame[self.facing]>=4 and self.facing == 'down':
            self.frame[self.facing] = 0        
        self.right_animations = []
        self.rs = []
        self.left_animations = []
        self.ls = []
        self.up_animations = []
        self.us = []
        self.down_animations = []
        self.ds = []
        for i in range(4):
            self.rs.append(pygame.image.load(f"img\Sprites\Characters\OldMan\Right_{i}.png"))
        for i in self.rs:
            self.right_animations.append(pygame.transform.scale(i, (tilesize, tilesize)))
        for i in range(4):
            self.ls.append(pygame.image.load(f"img\Sprites\Characters\OldMan\Left_{i}.png"))
        for i in self.ls:
            self.left_animations.append(pygame.transform.scale(i, (tilesize, tilesize)))
        for i in range(4):
            self.us.append(pygame.image.load(f"img\Sprites\Characters\OldMan\p_{i}.png"))
        for i in self.us:
            self.up_animations.append(pygame.transform.scale(i, (tilesize, tilesize)))
        for i in range(4):
            self.ds.append(pygame.image.load(f"img\Sprites\Characters\OldMan\Down_{i}.png"))
        for i in self.ds:
            self.down_animations.append(pygame.transform.scale(i, (tilesize, tilesize)))
        if self.facing == 'right':
            self.image = self.right_animations[self.frame[self.facing]]
            self.frame[self.facing] +=1
        if self.facing == 'left':
            self.image = self.left_animations[self.frame[self.facing]]
            self.frame[self.facing] +=1
        if self.facing == 'up':
            self.image = self.up_animations[self.frame[self.facing]]
            self.frame[self.facing] +=1
        if self.facing == 'down':
            self.image = self.down_animations[self.frame[self.facing]]
            self.frame[self.facing] +=1

    def movement(self):
        if self.facing == 'left':
            self.x_change -= 2
            self.movement_loop -= 1
            if self.movement_loop <= -self.max_travel:
                self.facing = random.choice(['right', 'left', 'up', 'down'])
                    
        if self.facing == 'right':
            self.x_change += 2
            self.movement_loop += 1
            if self.movement_loop >= self.max_travel:
                self.facing = random.choice(['right', 'left', 'up', 'down'])
                
        if self.facing == 'up':
            self.y_change -= 2
            self.movement_loop -= 1
            if self.movement_loop <= -self.max_travel:
                self.facing = random.choice(['right', 'left', 'up', 'down'])
                    
        if self.facing == 'down':
            self.y_change += 2
            self.movement_loop += 1
            if self.movement_loop >= self.max_travel:
                self.facing = random.choice(['right', 'left', 'up', 'down'])
    def collider(self, item, direction):
        if direction == 'x': 
            if item:
                if self.x_change > 0:
                    self.rect.x = item[0].rect.left - self.rect.width
                    self.facing = 'right'
                if self.x_change < 0:
                    self.rect.x = item[0].rect.right
                    self.facing = 'left'
                    

        if direction == 'y':
            if item:
                if self.y_change > 0:
                    self.rect.y = item[0].rect.top - self.rect.height
                    self.facing = 'up'
                if self.y_change < 0:
                    self.rect.y = item[0].rect.bottom
                    self.facing = 'down'
    def collide_blocks(self, direction):
        if direction == 'x':
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            hit_a = pygame.sprite.spritecollide(self, self.game.house_a, False)
            hit_b = pygame.sprite.spritecollide(self, self.game.house_b, False)
            hit_c = pygame.sprite.spritecollide(self, self.game.tavern, False)
            hit_d = pygame.sprite.spritecollide(self, self.game.wizard_tower, False)
            hit_e = pygame.sprite.spritecollide(self, self.game.tree, False)
            hit_f = pygame.sprite.spritecollide(self, self.game.forest_gate, False)
            self.collider(hits, direction)
            self.collider(hit_a, direction)
            self.collider(hit_b, direction)
            self.collider(hit_c, direction)
            self.collider(hit_d, direction)
            self.collider(hit_e, direction)
            self.collider(hit_f, direction)
                    

        if direction == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            hit_a = pygame.sprite.spritecollide(self, self.game.house_a, False)
            hit_b = pygame.sprite.spritecollide(self, self.game.house_b, False)
            hit_c = pygame.sprite.spritecollide(self, self.game.tavern, False)
            hit_d = pygame.sprite.spritecollide(self, self.game.wizard_tower, False)
            hit_e = pygame.sprite.spritecollide(self, self.game.tree, False)
            hit_f = pygame.sprite.spritecollide(self, self.game.forest_gate, False)
            self.collider(hits, direction)
            self.collider(hit_a, direction)
            self.collider(hit_b, direction)
            self.collider(hit_c, direction)
            self.collider(hit_d, direction)
            self.collider(hit_e, direction)
            self.collider(hit_f, direction)
    

    
