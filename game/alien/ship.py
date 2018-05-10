import pygame

class Ship():
    def  __init__(self,screen,ai_settings):
        """初始化飞船并设置其初始位置"""
        self.screen=screen
        self.ai_settings=ai_settings
        #加载飞船图像并获取其外接矩形
        self.image=pygame.image.load("F:\pycharm\images\shipps.jpg")
        self.rect=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()

        #将每艘飞船放在屏幕底部中央
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        #移动标志
        self.moving_right=False
        self.moving_left = False


        #为了在飞船的速度属性（self.rect.centerx只能为整数）中存储小数
        self.center=float(self.rect.centerx)


    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)
    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center+=self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            self.center -= self.ai_settings.ship_speed_factor
        #根据self.center更新rect对象
        self.rect.centerx=self.center

    def center_ship(self):
        """让飞船在屏幕居中"""
        self.center=self.screen_rect.centerx