import unittest
import pygame
from ship import Ship
from settings import Settings

class TestShipMovement(unittest.TestCase):

    def setUp(self):
        """初始化测试"""
        pygame.init()
        self.ai_settings = Settings()
        self.screen = pygame.display.set_mode((self.ai_settings.screen_width, self.ai_settings.screen_height))
        pygame.display.set_caption("Test Ship Movement")
        self.ship = Ship(self.ai_settings, self.screen)

    def test_move_right(self):
        """测试向右移动"""
        self.ship.moving_right = True
        original_center = self.ship.rect.centerx
        self.ship.update()
        self.assertGreater(self.ship.rect.centerx, original_center)

    def test_move_left(self):
        """测试向左移动"""
        self.ship.moving_left = True
        original_center = self.ship.rect.centerx
        self.ship.update()
        self.assertLess(self.ship.rect.centerx, original_center)

    def test_move_up(self):
        """测试向上移动"""
        self.ship.moving_up = True
        original_center = self.ship.rect.centery
        self.ship.update()
        self.assertLess(self.ship.rect.centery, original_center)


    def tearDown(self):
        """清理测试"""
        pygame.quit()
        self.screen = None
        self.ai_settings = None

if __name__ == '__main__':
    unittest.main()
