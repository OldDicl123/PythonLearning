"""我方飞机"""
import pygame


class MyPlane:
    """我方飞机类"""

    def __init__(self, window):
        """初始化我方飞机"""
        # 获取我方飞机的坐标(坐标位置POS接收一个元组,并赋值给pos_x和pos_y)
        # self.pos_x, self.pos_y = pos
        # 初始化飞机移动的参数
        self.offset = 10
        # 加载我方飞机图片并赋值给变量
        self.image = pygame.image.load('images/PlaneB.jpg')
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




