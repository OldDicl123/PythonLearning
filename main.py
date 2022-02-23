"""游戏的入口"""

import pygame
import sys
from my_plane import MyPlane
from bullet import  Bullet

# import datetime
# 指定最大帧率
MAX_FRAMERATE = 60
# 在垂直刻度,窗口尺寸占电脑屏幕尺寸的比例
SCALE_VERTICAL = 3 / 5
# 在水平刻度,窗口尺寸占电脑屏幕尺寸的比例
SCALE_HORIZONTAL = 2 / 5


class PlaneWar:
    """管理游戏的总体类"""
    def __init__(self):
        # 初始化pygame库
        pygame.init()
        # 获得当前屏幕的尺寸
        screen_widths, screen_heights = self.get_screen_size()
        # 根据屏幕尺寸计算窗口尺寸
        window_width, window_height = screen_widths * SCALE_HORIZONTAL, screen_heights * SCALE_VERTICAL
        # 定义游戏界面大小,将返回的界面赋值给window,方便后续修改
        self.window = pygame.display.set_mode((window_width, window_height))
        # self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # 设置窗口
        self._set_window()
        # 创建一个用于跟踪时间的时钟对象
        self.clock = pygame.time.Clock()
        # 创建我方飞机的实例对象
        self.my_plane = MyPlane(self.window)
        # 创建一个用于存储所有子弹的列表
        self.bullet_list = []

    def get_screen_size(self):
        """获取屏幕尺寸"""
        info = pygame.display.Info()
        screen_width = info.current_w
        screen_height = info.current_h
        return screen_width, screen_height

    def _set_window(self):
        """设置游戏窗口"""
        # 设置游戏界面的标题
        pygame.display.set_caption('飞机大战')
        # 加载窗口图标,并赋值给变量
        window_icon = pygame.image.load('images/PlaneA.jpg')
        # 调用窗口图标变量
        pygame.display.set_icon(window_icon)

    def run_game(self):
        """运行游戏"""
        # 定义一个死循环,让游戏界面一直存在
        while True:
            # 从事件队列中将所有事件全部取出并逐个进行处理
            self._handle_evens()
            # 设置游戏界面的颜色,每次绘制图像的时候清空屏幕
            self.window.fill(pygame.Color('light sky blue'))
            # 在窗口的指定位置绘制一架我方飞机
            # self.window.blit(self.my_plane, (299, self.pos_y))
            self.my_plane.draw()
            # 在窗口的指定位置绘制列表中所有子弹
            for bullet in self.bullet_list:
                bullet.draw()
            # 将内存中的窗口对象绘制到屏幕上已更新界面
            pygame.display.flip()
            # 更新我方飞机位置
            self.my_plane.update()
            # 更新列表中所有子弹的位置
            for bullet in self.bullet_list:
                bullet.update()
            # i += 1
            # if i == 150:
            #    print(datetime.datetime.now())
            # 设置while循环体再一秒内执行的最大次数(设置动画效果的最大帧率)
            self.clock.tick(MAX_FRAMERATE)

    def _handle_evens(self):
        # 从事件队列中将所有事件全部取出并逐个进行处理
        for event in pygame.event.get():
            # 如果某个事件是退出程序
            if event.type == pygame.QUIT:
                # print(event.type) # 256
                # 卸载pygame库
                pygame.quit()
                # 退出程序
                sys.exit()
            # 如果某个事件是用户按下了键盘上的某个键
            elif event.type == pygame.KEYDOWN:
                # 调用处理键盘按下的方法函数
                self._handle_keydown_events(event)
            # 如果某个事件是用户松开了键盘上的某个键
            elif event.type == pygame.KEYUP:
                # 调用处理键盘松开的方法函数
                self._handel_keyup_events(event)

    def _handle_keydown_events(self, event):
        """处理键盘按下的事件"""
        # 如果按下的键是上箭头或w
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            # 标记我方飞机向上移动
            self.my_plane.is_move_up = True
        # 如果按下的键是下箭头或s
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            # 标记我方飞机向下移动
            self.my_plane.is_move_down = True
        # 如果按下的键是左箭头或a
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            # 标记我方飞行向左移动
            self.my_plane.is_move_left = True
        # 如果按下的键是右箭头或d
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            # 标记我方飞机想右移动
            self.my_plane.is_move_right = True
        # 如果按下的键是esc
        elif event.key == pygame.K_ESCAPE:
            # 卸载pygame库
            pygame.quit()
            # 退出程序
            sys.exit()
        elif event.key == pygame.K_SPACE:
            # 生成子弹
            bullets = Bullet(self.window, self.my_plane)
            self.bullet_list.append(bullets)

    def _handel_keyup_events(self, event):
        """处理键盘松开的事件"""
        # 如果松开的键是上箭头或w
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.my_plane.is_move_up = False
        # 如果松开的键是下箭头或s
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.my_plane.is_move_down = False
        # 如果松开的键是左箭头或a
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.my_plane.is_move_left = False
        # 如果松开的键是右箭头或d
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.my_plane.is_move_right = False


# 只有当直接运行main.py的时候
if __name__ == '__main__':
    # 运行游戏
    PlaneWar().run_game()
    # print('run_game被调用了')
# 1
