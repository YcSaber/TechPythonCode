import sys
import pygame
from settings import Settings
from ship import Ship
import game_function as gf

def run_game():
    # 初始化游戏并创建屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen_height = ai_settings.screen_height
    screen_width = ai_settings.screen_width
    bg_color = ai_settings.bg_color
    screen = pygame.display.set_mode((screen_height,screen_width))
    pygame.display.set_caption('Alien Invasion')
    
    # 创建一艘飞船
    ship = Ship(ai_settings,screen)
    
    # 开始游戏主循环
    while True:
        # 监听键鼠事件
        gf.check_events(ship)
        ship.update_moving()
        # 屏幕事件
        gf.update_screen(bg_color,screen,ship)

run_game()