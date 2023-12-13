import pygame
from pygame.sprite import Sprite
import random


class Star2(Sprite):
    """表示单个星星的类。"""       
    def __init__(self, ai_settings, screen):
        """初始化星星并设置其随机位置。"""
        super(Star2, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/star2.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = random.randint(0, self.ai_settings.screen_width - 5*self.rect.width)
        self.rect.y = random.randint(0, self.ai_settings.screen_height - 5*self.rect.height)
        

    def update(self):
        # Draw the star
        self.screen.blit(self.image, self.rect)
