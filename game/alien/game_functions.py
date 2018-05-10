import sys
import pygame
from pygame.locals import *
from bullet import  Bullet
from alien import Alien
from time import sleep

def check_events(ai_settings,screen,stats,play_button,ship,bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type==KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type==KEYUP:
            check_keyup_events(event,ship)
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_button(stats,play_button,mouse_x,mouse_y)
def check_play_button(stats,play_button,mouse_x,mouse_y):
    """在玩家单机paly按钮开始新游戏"""
    if play_button.rect.collidepoint(mouse_x,mouse_y):
        stats.game_active=True
#重构事件中的 KEYDOWN和KEYUP事件
def check_keydown_events(event,ai_settings,screen,ship,bullets):
    if event.key == K_RIGHT:
        ship.moving_right = True
    elif event.key == K_LEFT:
        ship.moving_left = True
    elif event.key==K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key==K_q:
        sys.exit()
def fire_bullet(ai_settings,screen,ship,bullets):
    # 创建一颗子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
def check_keyup_events(event,ship):
    if event.key == K_RIGHT:
        ship.moving_right = False
    elif event.key == K_LEFT:
        ship.moving_left = False
def update_screen(ai_settings,screen,stats,ship,bullets,aliens,play_button):
    """跟新屏幕图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    #在飞船和外星人外面重新绘制所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    #如果游戏处于非活动状态，就绘制paly按钮
    if not stats.game_active:
        play_button.draw_button()
    # 让屏幕可见
    pygame.display.flip()
def update_bullets(ai_settings, screen, ship, aliens,bullets):
    """更新子弹的位置，并删除已经消失的子弹"""
    #更新子弹的位置
    bullets.update()
    # 删除已经消失的子弹
    for bullet in bullets.copy():  # 为什么遍历副本
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))   #检测子弹是否删除（大大消耗内存）
    # 检查是否有子弹击中了外星人，如果有就删除相应的子弹和外星人
    #sprite.groupcollide()方法返回的是一个字典
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)
def check_bullet_alien_collisions(ai_settings, screen, ship, aliens,bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    # 生成新的外星人
    if len(aliens) == 0:
        # 删除现有子弹并新建一群外星人
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
def update_aliens(ai_settings,stats,screen,aliens,ship,bullets):
    """检查是否有外星人位于屏幕边缘，更新外星人群中所有外星人的位置"""
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    #检查外星人与飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen,aliens,ship,bullets)
        #print("ship hit!!!")
    #检查是否外星人到达屏幕底端
    check_alien_bottom(ai_settings, stats, screen, ship, aliens, bullets)
def get_number_aliens_x(ai_settings,alien_width):
    """计算每行能够容纳多少外星人"""
    # 外星人间距为外星人宽度
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x
def get_number_rows(ai_settings,ship_height,alien_height):
    """计算屏幕可以容纳多好行外星人"""
    available_space_y=ai_settings.screen_height-3*alien_height-ship_height
    number_rows=int(available_space_y/(2*alien_height))
    return number_rows
def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    """创建第一个外星人并将其加入当前行"""
    alien = Alien(ai_settings, screen)
    alien_width=alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number  # 当alien_number=0 有创建一个对象
    alien.rect.x = alien.x
    alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
    aliens.add(alien)
def create_fleet(ai_settings,screen,ship,aliens):
    """创建一个外星人,并计算一行能够能容纳多少外星人"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height=alien.rect.height
    number_aliens_x=get_number_aliens_x(ai_settings,alien_width)
    number_rows=get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
    #创建第一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
def check_fleet_edges(ai_settings,aliens):
    """有外星人叨叨边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break    #不能少  大 bug
def change_fleet_direction(ai_settings,aliens):
    """将整群外星人向下移，并且改变他们的方向"""
    for alien in aliens.sprites():      #向下移动
        alien.rect.y+=ai_settings.fleet_drop_speed
    ai_settings.fleet_direction*=-1  #向左或向右移动
def ship_hit(ai_settings,stats,screen,aliens,ship,bullets):
    """响应被外星人撞到的飞船"""

    if stats.ships_left>0:
        # ship_left减1
        stats.ships_left-=1
        #清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        #创建一群新的外星人，并将飞船放到屏幕底端中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        #暂停
        sleep(0.5)
    else:
        stats.game_active=False
def check_alien_bottom(ai_settings,stats,screen,ship,aliens,bullets):
    """检查外星人是否到达屏幕的底端"""
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom>=screen_rect.bottom:
            #像飞船被撞之后一样处理
            ship_hit(ai_settings,stats,screen,aliens,ship,bullets)
            break

