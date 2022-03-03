import pygame
from player import*
import random
from battle_button import Button
import time
page = False
pygame.init()

clock = pygame.time.Clock()
fps = 60
bottom_panel = 150
screen_width  = 800
screen_height = 400
scr_height = 400 + bottom_panel
red = (255, 0, 0)
green = (0, 255, 0)
pygame.display.set_caption('Battle')

current_fighter = 1
total_fighters = 3
action_cooldown = 0
action_wait_time = 90
        
class fighter():
    def __init__(self, x, y, name, max_hp, strength, potions, screen, damage, knight):
        self.screen = screen
        self.name = name
        self.damage = damage
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.start_potions = potions
        self.potions = potions
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        self.block = 0
        self.action = 0 #0:idle 1:attack 2:hurt 3:dead 4:fireball 5:block 6:block idle
        self.update_time = pygame.time.get_ticks()
        # load idle images
        temp_list = []
        for i in range(8):
            image = pygame.image.load(f"img\Sprites\Idle\{self.name}_idle_{i}.png")
            image = pygame.transform.scale(image, (image.get_width()*2, image.get_height()*3))
            temp_list.append(image)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range(8):
            if plr.weap == 'bow' or plr.weap == 'electric bow' and knight == True:
                image = pygame.image.load(f"img\Sprites\Attack\{self.name}_Bow_Attack_{i}.png")
            else:
                image = pygame.image.load(f"img\Sprites\Attack\{self.name}_Attack_{i}.png")
            image = pygame.transform.scale(image, (image.get_width()*2, image.get_height()*3))
            temp_list.append(image)
        self.animation_list.append(temp_list)
        temp_list = []        
        for i in range(3):
            image = pygame.image.load(f"img\Sprites\Hurt\{self.name}_Hurt_{i}.png")
            image = pygame.transform.scale(image, (image.get_width()*2, image.get_height()*3))
            temp_list.append(image)
        self.animation_list.append(temp_list)
        temp_list = []        
        for i in range(10):
            image = pygame.image.load(f"img\Sprites\Death\{self.name}_Death_{i}.png")
            image = pygame.transform.scale(image, (image.get_width()*2, image.get_height()*3))
            temp_list.append(image)
        self.animation_list.append(temp_list)
        temp_list = []        
        for i in range(4):
            image = pygame.image.load(f"img\Sprites\Burnt\{self.name}_Hurt_{i}.png")
            image = pygame.transform.scale(image, (image.get_width()*2, image.get_height()*3))
            temp_list.append(image)
        self.animation_list.append(temp_list)
        temp_list = []        
        for i in range(4):
            image = pygame.image.load(f"img\Sprites\HeroKnight\Block\HeroKnight_Block_{i}.png")
            image = pygame.transform.scale(image, (image.get_width()*2, image.get_height()*3))
            temp_list.append(image)
        self.animation_list.append(temp_list)
        temp_list = []        
        for i in range(8):
            image = pygame.image.load(f"img\Sprites\HeroKnight\BlockIdle\HeroKnight_Block Idle_{i}.png")
            image = pygame.transform.scale(image, (image.get_width()*2, image.get_height()*3))
            temp_list.append(image)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    def update(self):
        animation_cooldown = 100
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                if self.block > 0:
                    self.block_idle()
                else:
                    self.idle()
                

    def idle(self):
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()



    def attack(self, target):
        white = (255, 255, 255)
        rand = random.randint(1, 5)
        damz = plr.level + random.randint(round(plr.str/4, 0), 9)
        print(damz)
        damage = self.damage + random.randint(-1, damz)
        if damage <= 0:
            damage = 1
        target.hp -= damage
        target.hurt()
                
        if target.hp < 1:
            target.hp = 0
            target.dead()
            target.alive = False

        damage_text = damagetext(target.rect.centerx, target.rect.y, str(damage), red)
        damage_text_group.add(damage_text)

        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def fireball(self, target):
        self.action = 4
        damage = 5+random.randint(1, 4)
        target.hp -= damage
        self.frame_index = 0
        if target.hp < 1:
            target.hp = 0
            target.dead()
            target.alive = False
        self.update_time = pygame.time.get_ticks()
    def hurt(self):
        self.action = 2
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
    def dead(self):
        self.action = 3
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
    def blocks(self):
        self.action = 5
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
    def block_idle(self):
        self.action = 6
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()   
        
    def draw(self):
        self.screen.blit(self.image, self.rect)


class healthbar():
    def __init__(self, x, y, hp, max_hp, screen):
        self.screen = screen
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp

    def draw(self, hp):

        self.hp = hp

        ratio = self.hp / self.max_hp
        pygame.draw.rect(self.screen, red, (self.x, self.y, 150, 20))
        pygame.draw.rect(self.screen, green, (self.x, self.y, 150*ratio, 20))

class damagetext(pygame.sprite.Sprite):
    def __init__(self, x, y, damage, colour):
        font = pygame.font.SysFont('Times New Roman', 26)
        pygame.sprite.Sprite.__init__(self)
        self.image  = font.render(damage, True, colour)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.counter = 0
        self.upwards = 2

    def update(self):
        self.rect.y -= self.upwards
        self.counter += 0.5
        if self.counter > 30:
            self.kill()



damage_text_group = pygame.sprite.Group()            
            
def start_battle(page):
    hp = plr.hp
    potions = plr.potions
    yellow = (255, 255, 0)
    green = (0, 255, 0)
    current_fighter = 1
    total_fighters = 3
    action_cooldown = 0
    action_wait_time = 90
    attack = False
    potion = False
    clicked = False
    game_over = 0
    font = pygame.font.SysFont('Times New Roman', 26)
    red = (255, 0, 0)
    green = (0, 255, 0)
    white = (254, 254, 254)
    whiteless = (235, 235, 235)
    whiter = (255, 255, 255)
    back_img = pygame.image.load("img\Background.png")
    bar_img = pygame.image.load('img\panel.png')
    sword_img = pygame.image.load("img\items\Weapons\Sword_mouse.png")
    potion_img = pygame.image.load("img\items\Potions\Hp_potion.png")
    runaway_img = pygame.image.load("img\items\Run_away_button.png")
    fireball_img = pygame.image.load("img\Fireball button.jpg")
    block_img = pygame.image.load("img\items\Weapons\Sheild_img.png")
    fireball_img.set_colorkey(whiter)
    runaway_img.set_colorkey(white)
    runaway_img.set_colorkey(whiteless)
    warrior = "HeroKnight"
    bandit = "LightBandit"
    dam_a = plr.mon_dam + random.randint(1, 7)
    dam_b = plr.mon_dam + random.randint(1, random.randint(2, 10))
    fps = 60
    bottom_panel = 150
    screen_width  = 800
    screen_height = 400
    armour_stop = round(plr.defense/5, 0)+plr.level/2
    scr_height = 400 + bottom_panel
    screen = pygame.display.set_mode((screen_width, scr_height))
    choose = random.choice([True, False])
    plr.mon_hp += random.randint(1, 10)
    block_button = Button(screen, 200, screen_height - bottom_panel + 220, block_img, 50, 50)  
    knight = fighter(200, 320, warrior, hp, plr.plwd, potions, screen, plr.plwd, True)
    bandit1 = fighter(550, 320, bandit, plr.mon_hp, plr.mon_dam, 1, screen, dam_a - armour_stop, False)
    bandit2 = fighter(750, 320, bandit, plr.mon_hp, plr.mon_dam, 1, screen, dam_b - armour_stop, False)
    potion_button = Button(screen, 100, screen_height - bottom_panel + 220, potion_img, 50, 50)
    run_away_button = Button(screen, 150, screen_height - bottom_panel + 220, runaway_img, 50, 50)
    knight_health_bar = healthbar(100, screen_height - bottom_panel + 180, knight.hp, knight.max_hp, screen)
    bandit1_health_bar = healthbar(560, screen_height - bottom_panel + 180, bandit1.hp, bandit1.max_hp, screen)
    bandit2_health_bar = healthbar(560, screen_height - bottom_panel + 235, bandit2.hp, bandit2.max_hp, screen)
    fireball_button = Button(screen, 45, screen_height - bottom_panel + 220, fireball_img, 50, 50)
    bandit_list = []
    bandit_list.append(bandit1)
    bandit_list.append(bandit2)
    clock = pygame.time.Clock()
    blue = (0, 0, 255)
    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))
        
    def draw_img(img):
        image = pygame.transform.scale(img, (screen_width, screen_height))
        screen.blit(image, (0, 0))

    def draw_bar(img):
        screen.blit(img,(0, screen_height))
        #show knight stance
        draw_text(f'{knight.name} HP: {knight.hp}', font, red, 100, screen_height - bottom_panel + 150)
        for count, i in enumerate(bandit_list):
            draw_text(f'{i.name} HP: {i.hp}', font, red, 550, (screen_height - bottom_panel + 150) + count * 60)
    def gamez_over():
        black = (0, 0, 0)
        game_over =pygame.image.load("img\game_over.webp")
        game_over.set_colorkey(black)
        screen.blit(game_over, (150, 150))
        page = True

    mana_count = ('mana: {}'.format(plr.mana))
    run = True   
    while run:  
        plr.mana = plr.mana
        potions = knight.potions
        hp = knight.hp
        plr.hp = hp
        plr.potions = potions
        clock.tick(fps)
        #drw page
        draw_img(back_img)
        #drw bar
        draw_bar(bar_img)
        
        knight_health_bar.draw(knight.hp)
        bandit1_health_bar.draw(bandit1.hp)
        bandit2_health_bar.draw(bandit2.hp)
        #drw knight
        knight.update()
        knight.draw()
        draw_text(str(plr.potions), font, red, 120, screen_height - bottom_panel+265)
        draw_text(('mana:{}'.format(plr.mana)), font, blue, 0, screen_height - bottom_panel+265)
        #drw bandit
        for bandit in bandit_list:
            bandit.update()
            bandit.draw()
        if current_fighter == 1:
            action_cooldown += 1
            if fireball_button.draw() and plr.mana >= 40:
                plr.mana -= 40
                current_fighter += 1
                action_cooldown = 0
                for bandit in bandit_list:
                    bandit.fireball(bandit)
            if block_button.draw():
                knight.block = 4
                current_fighter += 1
                action_cooldown = 0
            if run_away_button.draw():
                x = random.choice([True, False, False])
                if x:
                    game_over += 1
                    plr.bandits_killed -= 2
                    plr.xp -= 50
                    plr.money -= 25
                    run_suc_text = damagetext(knight.rect.centerx, knight.rect.y, 'run success', green)
                    damage_text_group.add(run_suc_text)
                    damage_text_group.update()
                    damage_text_group.draw(screen)
                else:
                    run_text = damagetext(knight.rect.centerx, knight.rect.y, 'run failed', red)
                    damage_text_group.add(run_text)
                    damage_text_group.update()
                    damage_text_group.draw(screen)
                    current_fighter += 1
                    action_cooldown = 0

        #damage text
        damage_text_group.update()
        damage_text_group.draw(screen)
            
            
        # player actions    
        attack = False
        potion = False
        target = None
        
        pygame.mouse.set_visible(True)
        pos = pygame.mouse.get_pos()
        for count, bandit in enumerate(bandit_list):
            if bandit.rect.collidepoint(pos):
                pygame.mouse.set_visible(False)
                screen.blit(sword_img, pos)
                if clicked == True and bandit.alive == True:                  
                    attack = True
                    target = bandit_list[count]
        if potion_button.draw():
            potion = True
        

        potion_effect = 4
        # player action
        if knight.alive == True:
            if current_fighter == 1:
                action_cooldown += 1
                if action_cooldown >= action_wait_time:
                    if attack == True and target != None:
                        knight.attack(target)
                        current_fighter += 1
                        action_cooldown = 0
                    if potion == True:
                        if knight.potions > 0:                      
                            if (knight.max_hp - knight.hp) > potion_effect:
                                heal_amount = potion_effect
                            else:
                                heal_amount = knight.max_hp - knight.hp
                            knight.hp += heal_amount
                            knight.potions -= 1
                    
                            damage_text = damagetext(knight.rect.centerx, knight.rect.y, str(potion_effect), green)
                            damage_text_group.add(damage_text)
                            action_cooldown = 0
                            potion = False
                        else:
                            potion = False
        else:
            game_over = -1

        #enemy action
        for count, bandit in enumerate(bandit_list):
           if current_fighter == 2 + count:
               if bandit.alive == True:
                   block_work = False
                   action_cooldown += 1
                   if action_cooldown >= action_wait_time:
                       if knight.block == 4:
                           bandit.attack(knight)
                           knight.block = 3
                       elif knight.block > 0 and knight.block < 4:
                           works = random.choice([True, True, True, False])
                           knight.blocks()
                           bandit.action = 1
                           if works:
                               block_text = damagetext(knight.rect.centerx, knight.rect.y, 'block', green)
                               damage_text_group.add(block_text)
                               damage_text_group.update()
                               damage_text_group.draw(screen)
                           else:
                               block_text_a = damagetext(knight.rect.centerx, knight.rect.y, 'block failed', red)
                               block_text_a.upwards = 1
                               bandit.attack(knight)
                               damage_text_group.add(block_text_a)
                               damage_text_group.update()
                               damage_text_group.draw(screen)
                           knight.block -= 1
                       else:
                           bandit.attack(knight)
                       current_fighter += 1
                       action_cooldown = 0
               else:                  
                   current_fighter += 1
        # reset fight
        if current_fighter > total_fighters:
            current_fighter = 1

        #are bandits ded
        alive_bandits = 0
        for bandit in bandit_list:
            if bandit.alive == True:
                alive_bandits += 1
        if alive_bandits == 0:
            game_over += 1
        if game_over > 0:
            exit_img = pygame.image.load("img/Exit_ton.jpg")
            exit_button = Button(screen, 210, screen_height - bottom_panel + 170, exit_img, 50, 50)
            if exit_button.draw():
                time.sleep(2)
                plr.bandits_killed += 2
                page = True
                return page
                run = False
        elif game_over < 0:
            death_img = pygame.image.load("img/Exit_ton.jpg")
            death_button = Button(screen, 210, screen_height - bottom_panel + 170, death_img, 50, 50)
            gamez_over()
            if death_button.draw():
                run = False

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True
    
            else:
                clicked = False
                

        pygame.display.update()
    pygame.quit()
    run = False

