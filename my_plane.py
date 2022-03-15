"""我方飞机"""
import pygame
from pygame.sprite import Sprite
import constants

class MyPlane(Sprite):
    """我方飞机类"""

    def __init__(self, window):
        """初始化我方飞机"""

        # 调用父类Sprite的特殊方法__init__
        super().__init__()
        # 初始化飞机移动的参数
        self.offset = 10
        # 图片切换的计数器
        self.switch_counter = 0
        # 加载我方飞机第一张图片并赋值给变量
        self.image1 = pygame.image.load('images/my_plane1.png')
        # 我方飞机的图片是第一张图片
        self.image = self.image1
        # 加载我方飞机第二张图片并赋值给变量
        self.image2 = pygame.image.load('images/my_plane2.png')
        # 获取窗口对象
        self.window = window
        # 获取我方飞机的矩形
        self.rect = self.image.get_rect()
        # 获取窗口对象的矩形
        self.window_rect = self.window.get_rect()
        # 设置我方飞机的矩形位置，位于窗口矩形的中心位置
        self.rect.midbottom = self.window_rect.midbottom
        # 设置我方飞机行为状态
        self.is_move_up = False
        self.is_move_down = False
        self.is_move_left = False
        self.is_move_right = False

    def update(self):
        """更新我方飞机位置"""
        # 对我方飞机矩形的top坐标进行更改,并且向上不会超出窗口范围
        if self.is_move_up:
            if self.rect.top > 0:
                self.rect.top -= self.offset
        # 对我方飞机矩形的bottom坐标进行更改，并且向下不会超出窗口范围
        if self.is_move_down:
            if self.rect.bottom < self.window_rect.height:
                self.rect.bottom += self.offset
        # 对我方飞机矩形的left坐标进行更改，并且向左不会超出窗口范围
        if self.is_move_left:
            if self.rect.left > 0:
                self.rect.left -= self.offset
        # 对我方飞机矩形的right坐标进行更改，并且向右不会超出窗口范围
        if self.is_move_right:
            if self.rect.right < self.window_rect.width:
                self.rect.right += self.offset

    def draw(self):
        """绘制我方飞机"""
        # 在窗口的指定位置绘制一架飞机
        self.window.blit(self.image, self.rect)

    def switch_image(self):
        """切换我方飞机图片"""

        # 切换我方飞机图片的计数器+1
        self.switch_counter += 1
        # 如果是第一张图片
        if self.switch_counter == constants.MY_PLANE_SWITCH_TIME_FREQUENCY:
            if self.image == self.image1:
                # 切换到第二张图片
                self.image = self.image2
                # 如果是第二张图片
            elif self.image == self.image2:
                # 切换到第一张图片
                self.image = self.image1
            self.switch_counter = 0


