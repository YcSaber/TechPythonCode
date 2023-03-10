import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        """初始化飞船并设置其初始位置"""
        super(Ship,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('Alien Invasion/img/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        # 将每艘新飞船放在屏幕中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # 飞行移动标志
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        # 在飞船属性center中存储小数
        self.center = float(self.rect.centerx)
        self.center1 = float(self.rect.centery)
    def update_moving(self):
        """根据移动标志调整飞行位置"""
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
        if self.moving_up and self.rect.top > 0:
            self.center1 -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center1 += self.ai_settings.ship_speed_factor
        self.rect.centery = self.center1
    def center_ship(self):
        self.center = self.screen_rect.centerx
        self.center1 = self.screen_rect.bottom
        # self.rect.bottom = self.screen_rect.bottom
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    
    