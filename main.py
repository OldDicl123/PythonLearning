"""游戏的入口"""

import pygame
import sys
from my_plane import MyPlane
from bullet import Bullet
from small_enemy import SmallEnemy
from mid_enemy import MidEnemy
from big_enemy import BigEnemy
from pygame.sprite import Group
import constants

# import datetime


class PlaneWar:
    """管理游戏的总体类"""
    def __init__(self):
        # 初始化pygame库
        pygame.init()
        # 获得当前屏幕的尺寸
        screen_widths, screen_heights = self.get_screen_size()
        # 根据屏幕尺寸计算窗口尺寸
        window_width, window_height = \
            screen_widths * constants.SCALE_HORIZONTAL, screen_heights * constants.SCALE_VERTICAL
        # 定义游戏界面大小,将返回的界面赋值给window,方便后续修改
        self.window = pygame.display.set_mode((window_width, window_height))
        # self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # 设置窗口图标和标题
        self._set_window()
        # 创建一个用于跟踪时间的时钟对象
        self.clock = pygame.time.Clock()
        # 设置自定义事件定时器
        self._set_custom_events_timer()
        # 创建我方飞机的实例对象
        self.my_plane = MyPlane(self.window)
        # 创建存储元素所使用列表
        self._create_groups()

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

    def _create_groups(self):
        """创建所有元素存储的分组"""

        # 创建一个用于存储所有子弹的精灵分组
        self.bullet_group = Group()
        # 创建一个用于存储所有小型敌方飞机的分组
        self.small_enemy_group = Group()
        # 创建一个用于存储所有中型敌方飞机的分组
        self.mid_enemy_group = Group()
        # 创建一个用于存储所有大型敌方飞机的分组
        self.big_enemy_group = Group()
        # 创建一个用于存储所有敌方单位的分组
        self.enemy_group = Group()

    def _set_custom_events_timer(self):
        """设置自定义事件定时器"""

        # 在事件队列中每隔一段时间就生成一个自定义事件'创建子弹'
        pygame.time.set_timer(constants.ID_OF_CREATE_BULLET, constants.INTERVAL_OF_CREATE_BULLET)
        # 在事件队列中每隔一段时间就生成一个自定义事件'创建小型敌机'
        pygame.time.set_timer(constants.ID_OF_CREATE_SMALL_ENEMY, constants.INTERVAL_OF_CREATE_SMALL_ENEMY)
        # 在事件队列中每隔一段时间就生成一个自定义事件'创建中型敌机'
        pygame.time.set_timer(constants.ID_OF_CREATE_MID_ENEMY, constants.INTERVAL_OF_CREATE_MID_ENEMY)
        # 在事件队列中每隔一段时间就生成一个自定义事件'创建大型敌机'
        pygame.time.set_timer(constants.ID_OF_CREATE_BIG_ENEMY, constants.INTERVAL_OF_CREATE_BIG_ENEMY)

    def run_game(self):
        """运行游戏"""

        # 定义一个死循环,让游戏界面一直存在
        while True:
            # 从事件队列中将所有事件全部取出并逐个进行处理
            self._handle_evens()
            # 设置游戏界面的颜色,每次绘制图像的时候清空屏幕
            self.window.fill(pygame.Color('light sky blue'))
            # 子弹和小型飞机的碰撞检测
            self._check_collision_bullets_small()
            # 绘制飞机和子弹等元素
            self._draw_elements()
            # 将内存中的窗口对象绘制到屏幕上已更新界面
            pygame.display.flip()
            # 更新飞机和子弹的位置
            self._update_positions()
            # 删除所有不可见的元素
            self._delete_invisible_elements()
            # 切换我方飞机图片
            self.my_plane.switch_image()
            # 设置while循环体再一秒内执行的最大次数(设置动画效果的最大帧率)
            self.clock.tick(constants.MAX_FRAMERATE)

    def _handle_evens(self):
        """提取处理所有事件"""

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
            # 如果某个事件是用户自定义事件
            elif event.type == constants.ID_OF_CREATE_BULLET:
                # 生成子弹
                bullet = Bullet(self.window, self.my_plane)
                self.bullet_group.add(bullet)
            # 如果某个事件是用户自定义事件1
            elif event.type == constants.ID_OF_CREATE_SMALL_ENEMY:
                # 生成小型飞机
                small_enemy = SmallEnemy(self.window)
                # 添加到分组
                self.small_enemy_group.add(small_enemy)
                self.enemy_group.add(small_enemy)
            # 如果某个事件是用户自定义事件2
            elif event.type == constants.ID_OF_CREATE_MID_ENEMY:
                # 生成中型飞机
                mid_enemy = MidEnemy(self.window)
                # 添加到分组
                self.mid_enemy_group.add(mid_enemy)
                self.enemy_group.add(mid_enemy)
            # 如果某个事件是用户自定义事件3
            elif event.type == constants.ID_OF_CREATE_BIG_ENEMY:
                # 生成大型飞机
                big_enemy = BigEnemy(self.window)
                # 添加到分组
                self.big_enemy_group.add(big_enemy)
                self.enemy_group.add(big_enemy)

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

    def _check_collision_bullets_small(self):
        # 子弹和小型敌机碰撞

        # 碰撞检测，并将返回值赋值给变量
        dict_collided = pygame.sprite.groupcollide(self.small_enemy_group, self.bullet_group, False, True)
        if len(dict_collided) > 0:
            # 遍历所有发生碰撞的小型敌机
            for small_enemy in dict_collided.keys():
                # 播放小型敌机爆炸的声音
                small_enemy.play_explode_sound()

    def _draw_elements(self):
        """绘制所有元素"""

        # 在窗口的指定位置绘制一架我方飞机
        self.my_plane.draw()
        # 在窗口的指定位置绘制分组中所有子弹
        self.bullet_group.draw(self.window)
        # 在窗口的指定位置绘制列表中所有小型敌机
        self.small_enemy_group.draw(self.window)
        # 在窗口的指定位置绘制列表中的所有中型敌机
        self.mid_enemy_group.draw(self.window)
        # 在窗口的指定位置绘制列表中的所有大型敌机
        self.big_enemy_group.draw(self.window)

    def _update_positions(self):
        """更新所有元素的位置"""

        # 更新我方飞机位置
        self.my_plane.update()
        # 更新列表中所有子弹的位置
        for bullet in self.bullet_group.sprites():
            bullet.update()
        # 更新列表中所有小型敌方飞机的位置
        for small_enemy in self.small_enemy_group.sprites():
            small_enemy.update()
        # 更新列表中所有中型敌方飞机的位置
        for mid_enemy in self.mid_enemy_group.sprites():
            mid_enemy.update()
        # 更新列表中所有大型敌方飞机的位置
        for big_enemy in self.big_enemy_group.sprites():
            big_enemy.update()

    def _delete_invisible_elements(self):
        """删除所有不可见的元素"""

        # 删除窗口中不可见的子弹
        self._delete_invisible_bullets()
        # 删除窗口中不可见的敌方飞机
        self._delete_invisible_enemy()

    def _delete_invisible_bullets(self):
        """删除窗口中所有不可见的子弹"""

        # 遍历子弹分组
        for bullet in self.bullet_group.sprites():
            # 如果某颗子弹从窗口中不可见
            if bullet.rect.bottom <= 0:
                # 删除该子弹
                self.bullet_group.remove(bullet)

    def _delete_invisible_enemy(self):
        """删除窗口中所有不可见的敌机"""

        # 遍历敌机列表
        for enemy in self.enemy_group.sprites():
            # 如果某架敌机在窗口中不可见
            if enemy.rect.top >= self.window.get_rect().height:
                # 调用方法kill,把敌机实例从所有精灵分组中删除
                enemy.kill()


# 只有当直接运行main.py的时候
if __name__ == '__main__':
    # 运行游戏
    PlaneWar().run_game()
    # print('run_game被调用了')
