# import pygame
# from pygame.sprite import Sprite
# import random
# import pygame.font
# from pygame.sprite import Group


# class Star(Sprite):
#     """表示单个星星的类。"""       
#     def __init__(self, ai_settings, screen):
#         """初始化星星并设置其随机位置。"""
#         super(Star, self).__init__()
#         self.screen = screen
#         self.ai_settings = ai_settings
#         self.image = pygame.image.load('images/stars.bmp')
#         self.rect = self.image.get_rect()
        

#         # 准备包含最高得分和当前得分的图像
#         self.createstar()
#         self.updatestar()
        
#     def createstar(self):    
#         self.stars = Group()
#         for _ in range(50):  # 添加星星的循环
#             star = Star(self.ai_settings, self.screen)
#             star.rect.x = random.randint(0, self.ai_settings.screen_width - star.rect.width)
#             star.rect.y = random.randint(0, self.ai_settings.screen_height - star.rect.height)
#             self.stars.add(star) 
            
#     def  updatestar(self):
#         # Draw the stars
#         self.stars.draw(self.screen)


import pygame
from pygame.sprite import Sprite
import random


class Star(Sprite):
    """表示单个星星的类。"""       
    def __init__(self, ai_settings, screen):
        """初始化星星并设置其随机位置。"""
        super(Star, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/stars.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = random.randint(0, self.ai_settings.screen_width - 5*self.rect.width)
        self.rect.y = random.randint(0, self.ai_settings.screen_height - 5*self.rect.height)
        

    def update(self):
        # Draw the star
        self.screen.blit(self.image, self.rect)
