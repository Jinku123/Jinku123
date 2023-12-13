import pygame
import random
from pygame.sprite import Group
from time import sleep
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf
from button import Button
from  stars import Star
from  star2 import Star2
        
def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")
    # 创建存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    #添加音乐
    pygame.mixer.music.load("1.mp3")
    # 设置音量（可选）
    pygame.mixer.music.set_volume(0.5)  # 0.0到1.0之间
    pygame.mixer.music.play()
    # #创建星星群组
    # stars = Group()
    # for _ in range(50):
    #     star = Star(ai_settings, screen)
    #     stars.add(star)
    # for star in stars:
    #         star.update()
    #         print(1)
        
    # pygame.display.flip()  # 更新屏幕以显示星星
    i=0
    # 开始游戏的主循环
    while True:
        
        #创建星星群组
        
        if i%10000==0:
            stars1 = Group()
            stars2 = Group()
            for _ in range(5):
                star = Star(ai_settings, screen)
                stars1.add(star)
            for _ in range(5):
                star = Star2(ai_settings, screen)
                stars2.add(star)
        i=i+1      
        for star in stars1:
                star.update()
        for star in stars2:
                star.update()        
        pygame.display.flip()  # 更新屏幕以显示星星
        
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        pygame.display.flip()  # 更新屏幕以显示星星
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)

            
            
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,bullets, play_button)
        
run_game()
