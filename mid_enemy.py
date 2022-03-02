"""敌方飞机"""
import pygame
import random
from pygame.sprite import Sprite


class MidEnemy(Sprite):
    """敌方类"""

    def __init__(self, window):
        """初始化敌方飞机"""

        # 调用父类Sprite的特殊方法__init__
        super().__init__()
        # 获取窗口对象
        self.window = window
        # 加载敌方飞机图片并赋值给变量
        self.image = pygame.image.load('images/mid_enemy.png')
        # 获取敌方飞机的矩形
        self.rect = self.image.get_rect()
        # 获取窗口的矩形
        self.window_rect = self.window.get_rect()
        # 设置敌方飞机的矩形位置，位于窗口的顶部位置   设置敌方飞机
        self.rect.bottom = self.window_rect.top
        self.rect.left = random.randint(0, self.window_rect.width - self.rect.width)
        # 初始化飞机移动的参数
        self.offset = 2

    def update(self):
        """更新敌方飞机位置"""
        # 对敌方飞机矩形的top坐标进行更改
        self.rect.top += self.offset

    def draw(self):
        """绘制敌方飞机"""
        # 在窗口的指定位置绘制一架敌方飞机
        self.window.blit(self.image, self.rect)

