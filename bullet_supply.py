"""子弹补给"""
import pygame
import random
from pygame.sprite import Sprit


class BulletSupply(Sprite):
    """子弹补给类"""

    def __init__(self, window):
        """初始化子弹补给"""

        # 调用父类Sprite的特殊方法__init__
        super().__init__()
        # 获取窗口对象
        self.window = window
        # 生成一个切换图片的计数器
        self.switch_explode_counter = 0
        # 加载子弹补给图片
        self.image = pygame.image.load('images/bullet_supply.png')
        # 获取子弹补给的矩形
        self.rect = self.image.get_rect()
        # 获取窗口的矩形
        self.window_rect = self.window.get_rect()
        # 设置子弹补给的矩形位置，位于窗口的顶部位置
        self.rect.bottom = self.window_rect.top
        self.rect.left = random.randint(0, self.window_rect.width - self.rect.width)
        # 初始化飞机移动的参数
        self.offset = 5

    def update(self):
        """更新子弹补给的位置"""
        # 对敌方飞机矩形的top坐标进行更改
        self.rect.top += self.offset

    def draw(self):
        """绘制子弹补给"""
        # 在窗口的指定位置绘制子弹补给图片
        self.window.blit(self.image, self.rect)


