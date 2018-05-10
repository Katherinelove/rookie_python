import  sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import Gamestats
from button import Button


def run_game():
    #初始化游戏并创建一个屏幕
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #设置背景色
    #bg_color=(230,230,230)

    #创建一艘飞船
    ship=Ship(screen,ai_settings)
    #创建一个用于存储子弹的编组
    bullets=Group()
    #创建一个外星人
    #alien=Alien(ai_settings,screen)
    aliens=Group()

    #创建外星人群（在主循环外创建一批即可）
    gf.create_fleet(ai_settings,screen,ship,aliens)

    #创建一个用于储存游戏统计信息的实例
    stats=Gamestats(ai_settings)

    #创建play按钮
    play_button=Button(ai_settings,screen,"play")

    #开始游戏主循环
    while True:
        #监听键盘和鼠标事件
        gf.check_events(ai_settings,screen,stats,play_button,ship,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,aliens,ship,bullets)
        gf.update_screen(ai_settings,screen,stats,ship,bullets,aliens,play_button)


run_game()
