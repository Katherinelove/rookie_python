class Settings():
    """存储外星人入侵的所有设置的类"""
    def __init__(self):
        """初始化游戏设置"""
        #屏幕设置
        self.screen_width=600
        self.screen_height=600
        self.bg_color=(230,230,230)
        #飞船设置
        self.ship_speed_factor=3.5
        self.ship_limit=3
        #bullet设置
        self.bullet_speed_factor=3
        self.bullet_width=20
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullets_allowed=20


        # 外星人移动速度
        self.alien_speed_factor =1
        #撞到边缘下移速度
        self.fleet_drop_speed=10
        #fleet_direction 为1表示向右移动，为-1表示向左移动（因为只有两个方向--x坐标，这儿用1，-1表示）
        self.fleet_direction=1

