import pygame

class speech_bubble(pygame.sprite.Sprite):
    def __init__(self, game, x, y, text, screen):
        self.game = game
        self._layer = 12
        self.groups = self.game.all_sprites, self.game.speech_bubble
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.colour = (255, 255, 255)
        self.orange = (255, 200, 0)
        self.text = text
        self.font = pygame.font.SysFont(None, 25)

        self.x = x
        self.y = y

        self.make()

    def draw(self, text, x, y, on):
        self.text = text
        self.x = x
        self.y = y
        self.make()
        if on:
            self.image = pygame.Surface([self.width, self.height])
            self.image.blit(self.text_img, (0, 0))
            pygame.draw.rect(self.image, self.orange, pygame.Rect(0, 0, self.width, self.height), 2)
    def make(self):
        self.text_img = self.font.render(self.text, True, self.colour)
        
        self.width = self.text_img.get_width()
        self.height = self.text_img.get_height()
        
        self.image = pygame.Surface([self.width, self.height])
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.speech_bubble = pygame.image.load("img\Speech_box.jpg")
        self.speech_bubble = pygame.transform.scale(self.speech_bubble, (self.width, self.height))
