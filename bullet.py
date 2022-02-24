"""我方子弹"""
import pygame


class Bullet:
    """我方子弹类"""

    def __init__(self, window, my_plane):
        """初始化我方子弹"""

        # 获取窗口对象
        self.window = window
        # 加载我方子弹图片并赋值给变量
        self.image = pygame.image.load('images/bullet.png')
        # 获取我方子弹的矩形
        self.rect = self.image.get_rect()
        # 获取飞机的矩形
        self.my_plane_rect = my_plane.rect
        # 设置我方子弹的矩形位置，位于飞机矩形的顶部中心位置
        self.rect.midtop = self.my_plane_rect.midtop
        # 初始化子弹移动的参数
        self.offset = 30

    def update(self):
        """更新我方子弹位置"""
        # 对我方飞机矩形的top坐标进行更改,并且向上不会超出窗口范围
        self.rect.top -= self.offset

    def draw(self):
        """绘制我方飞机"""
        # 在窗口的指定位置绘制一架飞机
        self.window.blit(self.image, self.rect)




