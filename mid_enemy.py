"""敌方飞机"""
import pygame
import random
from pygame.sprite import Sprite
import constants


class MidEnemy(Sprite):
    """敌方类"""

    def __init__(self, window):
        """初始化敌方飞机"""

        # 调用父类Sprite的特殊方法__init__
        super().__init__()
        # 获取窗口对象
        self.window = window
        # 生成一个切换图片的计数器
        self.switch_explode_counter = 0
        # 加载敌方飞机图片并赋值给变量
        self.image = self.mid_image = pygame.image.load('images/mid_enemy.png')
        # 加载敌方飞机图片并赋值给变量
        self.image1 = pygame.image.load('images/mid_enemy_explode1.png')
        # 加载敌方飞机图片并赋值给变量
        self.image2 = pygame.image.load('images/mid_enemy_explode2.png')
        # 加载敌方飞机图片并赋值给变量
        self.image3 = pygame.image.load('images/mid_enemy_explode3.png')
        # 加载敌方飞机图片并赋值给变量
        self.image4 = pygame.image.load('images/mid_enemy_explode4.png')
        # 获取敌方飞机的矩形
        self.rect = self.image.get_rect()
        # 获取窗口的矩形
        self.window_rect = self.window.get_rect()
        # 设置敌方飞机的矩形位置，位于窗口的顶部位置   设置敌方飞机
        self.rect.bottom = self.window_rect.top
        self.rect.left = random.randint(0, self.window_rect.width - self.rect.width)
        # 初始化飞机移动的参数
        self.offset = 2
        # 标记是否在切换图片
        self.is_switching_explode_image = False
        # 中型飞机的能量条变量
        self.energy = constants.MID_ENEMY_INITIAL_ENERGY

    def update(self):
        """更新敌方飞机位置"""
        # 对敌方飞机矩形的top坐标进行更改
        self.rect.top += self.offset

    def draw(self):
        """绘制敌方飞机"""
        # 在窗口的指定位置绘制一架敌方飞机
        self.window.blit(self.image, self.rect)

    def draw_energy_lines(self):
        """在中型敌机的尾部上方绘制一条白色线段"""
        pygame.draw.line(self.window, (255, 255, 255),
                         (self.rect.left, self.rect.top),
                         (self.rect.right, self.rect.top), 2)
        # 剩余能量/初始能量
        energy_left_ratio = self.energy / constants.MID_ENEMY_INITIAL_ENERGY
        """在中型敌机的尾部上方绘制一条红色线段"""
        if self.energy != 0:
            pygame.draw.line(self.window, (255, 0, 0),
                             (self.rect.left, self.rect.top),
                             (self.rect.left + self.rect.width * energy_left_ratio, self.rect.top), 2)

    def play_explode_sound(self):
        """播放中型敌机的爆炸声音"""

        # 加载中型敌机的爆炸声音
        explode_sound = pygame.mixer.Sound('sounds/mid_enemy_explode.wav')
        # 设置音量
        explode_sound.set_volume(constants.MID_ENEMY_EXPLODE_SOUND)
        # 播放声音
        explode_sound.play()

    def switch_explode_image(self):
        """切换我方飞机图片"""

        # 切换我方飞机图片的计数器+1
        self.switch_explode_counter += 1
        # 定义爆炸图片切换频率
        if self.switch_explode_counter == constants.MID_ENEMY_SWITCH_EXPLODE_IMAGE_FREQUENCY:
            if self.image == self.mid_image:
                self.image = self.image1
            # 如果是第一张图片
            elif self.image == self.image1:
                # 切换到第二张图片
                self.image = self.image2
                # 如果是第二张图片
            elif self.image == self.image2:
                # 切换到第三张图片
                self.image = self.image3
                # 如果是第三张图片
            elif self.image == self.image3:
                # 切换到第四张图片
                self.image = self.image4
                # 如果是第四张图片
            elif self.image == self.image4:
                # 删除敌机
                self.kill()
            # 重置计数器
            self.switch_explode_counter = 0

