import pygame

class speech_bubble(pygame.sprite.Sprite):
    def __init__(self, game, x, y, text, spr, screen):
        self.game = game
        self._layer = 10
        self.groups = self.game.text_sprites, self.game.speech_bubble
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.y = y

        self.text = text
        self.font = pygame.font.SysFont('SH Pinscher Regular', 30)

        self.width 

    def draw(self, text):
        self.text = text
        self.make()

    def make(self):
        self.col = (0, 0, 0)
