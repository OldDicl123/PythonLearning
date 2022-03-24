"""游戏的入口"""

import sys
import pygame
from my_plane import MyPlane
from bullet import Bullet
from double_bullet import DoubleBullet
from bullet_supply import BulletSupply
from small_enemy import SmallEnemy
from mid_enemy import MidEnemy
from big_enemy import BigEnemy
from pygame.sprite import Group
import constants


class PlaneWar:
    """管理游戏的总体类"""

    def __init__(self):
        """初始化游戏"""

        # 初始化pygame库
        pygame.init()

        # 创建窗口
        self._create_window()

        # 设置窗口
        self._set_window()

        # 创建一架我方飞机
        self.my_plane = MyPlane(self.window)

        # 创建管理精灵的分组
        self._create_groups()

        # 创建一个用于跟踪时间的时钟对象
        self.clock = pygame.time.Clock()

        # 设置定时器
        self._set_timers()

        # 标记游戏是否结束
        self.is_gameover = False

        # 获得字体对象
        self._get_fonts()

        # 双发子弹的计数器
        self.double_bullet_counter = 0

    def get_screen_size(self):
        """获得当前电脑屏幕的尺寸"""

        # 创建一个视频显示信息对象
        info = pygame.display.Info()

        # 获得当前电脑屏幕的宽度
        screen_width = info.current_w
        # 获得当前电脑屏幕的高度
        screen_height = info.current_h

        # 返回当前电脑屏幕的尺寸
        return screen_width, screen_height

    def _create_window(self):
        """创建窗口"""

        # 获得当前电脑屏幕的尺寸
        screen_width, screen_height = self.get_screen_size()

        # 根据当前电脑屏幕的尺寸计算窗口的尺寸
        window_width, window_height = screen_width * \
            constants.SCALE_HORIZONTAL, \
            screen_height * constants.SCALE_VERTICAL

        # 创建指定尺寸的窗口（游戏画面的所有元素都将在创建的这个窗口中绘制）
        self.window = pygame.display.set_mode((round(window_width),
                                               round(window_height)))
        # 创建全屏模式的窗口（游戏画面的所有元素都将在创建的这个窗口中绘制）
        # self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    def _set_window(self):
        """设置窗口"""

        # 设置窗口的标题
        pygame.display.set_caption("飞机大战")

        # 加载窗口图标
        window_icon = pygame.image.load("images/my_plane1.png")

        # 设置窗口的图标
        pygame.display.set_icon(window_icon)

    def _create_groups(self):
        """创建管理精灵的分组"""

        # 创建一个管理所有子弹的分组
        self.bullet_group = Group()

        # 创建一个管理所有双发子弹的分组
        self.double_bullet_group = Group()

        # 创建一个管理所有子弹补给的分组
        self.bullet_supply_group = Group()

        # 创建一个管理所有小型敌机的分组
        self.small_enemy_group = Group()

        # 创建一个管理所有中型敌机的分组
        self.mid_enemy_group = Group()

        # 创建一个管理所有大型敌机的分组
        self.big_enemy_group = Group()

        # 创建一个管理所有敌机的分组
        self.enemy_group = Group()

    def _set_timers(self):
        """设置定时器"""

        # 在事件队列中每隔一段时间就生成一个自定义事件"创建子弹"
        pygame.time.set_timer(constants.ID_OF_CREATE_BULLET,
                              constants.INTERVAL_OF_CREATE_BULLET)

        # 在事件队列中每隔一段时间就生成一个自定义事件"创建子弹补给"
        pygame.time.set_timer(constants.ID_OF_CREATE_BULLET_SUPPLY,
                              constants.INTERVAL_OF_CREATE_BULLET_SUPPLY)

        # 在事件队列中每隔一段时间就生成一个自定义事件"创建小型敌机"
        pygame.time.set_timer(constants.ID_OF_CREATE_SMALL_ENEMY,
                              constants.INTERVAL_OF_CREATE_SMALL_ENEMY)

        # 在事件队列中每隔一段时间就生成一个自定义事件"创建中型敌机"
        pygame.time.set_timer(constants.ID_OF_CREATE_MID_ENEMY,
                              constants.INTERVAL_OF_CREATE_MID_ENEMY)

        # 在事件队列中每隔一段时间就生成一个自定义事件"创建大型敌机"
        pygame.time.set_timer(constants.ID_OF_CREATE_BIG_ENEMY,
                              constants.INTERVAL_OF_CREATE_BIG_ENEMY)

    def _stop_timers(self):
        """停止定时器"""

        # 在事件队列中停止生成自定义事件"创建子弹"
        pygame.time.set_timer(constants.ID_OF_CREATE_BULLET, 0)

        # 在事件队列中停止生成自定义事件"创建双发子弹"
        pygame.time.set_timer(constants.ID_OF_CREATE_DOUBLE_BULLET, 0)

        # 在事件队列中停止生成自定义事件"创建子弹补给"
        pygame.time.set_timer(constants.ID_OF_CREATE_BULLET_SUPPLY, 0)

        # 在事件队列中停止生成自定义事件"创建小型敌机"
        pygame.time.set_timer(constants.ID_OF_CREATE_SMALL_ENEMY, 0)

        # 在事件队列中停止生成自定义事件"创建中型敌机"
        pygame.time.set_timer(constants.ID_OF_CREATE_MID_ENEMY, 0)

        # 在事件队列中停止生成自定义事件"创建大型敌机"
        pygame.time.set_timer(constants.ID_OF_CREATE_BIG_ENEMY, 0)

    def _get_fonts(self):
        """获得字体对象"""

        # 获得指定字体和指定字体大小的字体对象
        self.font_36 = pygame.font.Font("fonts/wawa.ttf",
                                        constants.FONT_SIZE_36)

        # 获得指定字体和指定字体大小的字体对象
        self.font_96 = pygame.font.Font("fonts/wawa.ttf",
                                        constants.FONT_SIZE_96)

    def run_game(self):
        """运行游戏"""

        # 让创建的窗口一直显示
        while True:
            # 处理事件
            self._handle_events()

            # 设置窗口的背景色
            self.window.fill(pygame.Color("lightskyblue"))

            # 如果游戏没有结束
            if not self.is_gameover:
                # 检测碰撞
                self._check_collisions()

            # 在窗口中绘制所有画面元素
            self._draw_elements()

            # 将内存中的窗口对象绘制到屏幕上以更新屏幕
            pygame.display.flip()

            # 如果游戏没有结束
            if not self.is_gameover:
                # 更新窗口中所有画面元素的位置
                self._update_positions()

                # 删除窗口中所有不可见的画面元素
                self._delete_invisible_elements()

                # 切换窗口中画面元素的图片
                self._switch_images()

            # 设置while循环体在一秒内执行的最大次数（设置动画的最大帧率）
            self.clock.tick(constants.MAX_FRAMERATE)

    def _handle_events(self):
        """处理事件"""

        # 从事件队列中将所有事件全部取出并逐个进行处理
        for event in pygame.event.get():
            # 如果某个事件是退出程序
            if event.type == pygame.QUIT:
                # 卸载pygame库
                pygame.quit()
                # 退出程序
                sys.exit()
            # 如果某个事件是用户按下了键盘上的某个键
            elif event.type == pygame.KEYDOWN:
                # 处理键盘按下的事件
                self._handle_keydown_events(event)
            # 如果某个事件是用户松开了键盘上的某个键
            elif event.type == pygame.KEYUP:
                # 处理键盘松开的事件
                self._handle_keyup_events(event)
            # 如果某个事件是自定义事件"创建子弹"
            elif event.type == constants.ID_OF_CREATE_BULLET:
                # 创建一颗子弹
                bullet = Bullet(self.window, self.my_plane)
                # 将创建的子弹添加到子弹分组中
                self.bullet_group.add(bullet)
            # 如果某个事件是自定义事件"创建双发子弹"
            elif event.type == constants.ID_OF_CREATE_DOUBLE_BULLET:
                # 创建两颗双发子弹
                self._create_two_double_bullets()
            # 如果某个事件是自定义事件"创建子弹补给"
            elif event.type == constants.ID_OF_CREATE_BULLET_SUPPLY:
                # 创建一个子弹补给
                bullet_supply = BulletSupply(self.window)
                # 将创建的子弹补给添加到子弹补给分组中
                self.bullet_supply_group.add(bullet_supply)
            # 如果某个事件是自定义事件"创建小型敌机"
            elif event.type == constants.ID_OF_CREATE_SMALL_ENEMY:
                # 创建一架小型敌机
                small_enemy = SmallEnemy(self.window)
                # 将创建的小型敌机添加到小型敌机分组中
                self.small_enemy_group.add(small_enemy)
                # 将创建的小型敌机添加到管理所有敌机的分组中
                self.enemy_group.add(small_enemy)
            # 如果某个事件是自定义事件"创建中型敌机"
            elif event.type == constants.ID_OF_CREATE_MID_ENEMY:
                # 创建一架中型敌机
                mid_enemy = MidEnemy(self.window)
                # 将创建的中型敌机添加到中型敌机分组中
                self.mid_enemy_group.add(mid_enemy)
                # 将创建的中型敌机添加到管理所有敌机的分组中
                self.enemy_group.add(mid_enemy)
            # 如果某个事件是自定义事件"创建大型敌机"
            elif event.type == constants.ID_OF_CREATE_BIG_ENEMY:
                # 创建一架大型敌机
                big_enemy = BigEnemy(self.window)
                # 将创建的大型敌机添加到大型敌机分组中
                self.big_enemy_group.add(big_enemy)
                # 将创建的大型敌机添加到管理所有敌机的分组中
                self.enemy_group.add(big_enemy)
            # 如果某个事件是自定义事件"解除我方飞机的无敌状态"
            elif event.type == constants.ID_OF_CANCEL_INVINCIBLE:
                # 解除我方飞机的无敌状态
                self.my_plane.is_invincible = False
                # 在事件队列中停止生成自定义事件"解除我方飞机的无敌状态"
                pygame.time.set_timer(constants.ID_OF_CANCEL_INVINCIBLE, 0)

    def _handle_keydown_events(self, event):
        """处理键盘按下的事件"""

        # 如果按下的键是上箭头或W键
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            # 标记我方飞机向上移动
            self.my_plane.is_move_up = True
        # 如果按下的键是下箭头或S键
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            # 标记我方飞机向下移动
            self.my_plane.is_move_down = True
        # 如果按下的键是左箭头或A键
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            # 标记我方飞机向左移动
            self.my_plane.is_move_left = True
        # 如果按下的键是右箭头或D键
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            # 标记我方飞机向右移动
            self.my_plane.is_move_right = True
        # 如果按下的键是Esc键
        elif event.key == pygame.K_ESCAPE:
            # 卸载pygame库
            pygame.quit()
            # 退出游戏
            sys.exit()

    def _handle_keyup_events(self, event):
        """处理键盘松开的事件"""

        # 如果松开的键是上箭头或W键
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            # 标记我方飞机不向上移动
            self.my_plane.is_move_up = False
        # 如果松开的键是下箭头或S键
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            # 标记我方飞机不向下移动
            self.my_plane.is_move_down = False
        # 如果松开的键是左箭头或A键
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            # 标记我方飞机不向左移动
            self.my_plane.is_move_left = False
        # 如果松开的键是右箭头或D键
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            # 标记我方飞机不向右移动
            self.my_plane.is_move_right = False

    def _create_two_double_bullets(self):
        """创建两颗双发子弹"""

        # 双发子弹的计数器加1
        self.double_bullet_counter += 1

        # 如果双发子弹计数器的值没有达到最大值
        if self.double_bullet_counter != constants.DOUBLE_BULLET_COUNTER_MAX:
            # 创建一颗位于我方飞机左翼的双发子弹
            double_bullet1 = DoubleBullet(self.window, self.my_plane)

            # 设置我方飞机左翼的双发子弹的初始位置
            double_bullet1.rect.center = (self.my_plane.rect.centerx -
                                          constants.DOUBLE_BULLET_OFFSET,
                                          self.my_plane.rect.centery)

            # 创建一颗位于我方飞机右翼的双发子弹
            double_bullet2 = DoubleBullet(self.window, self.my_plane)

            # 设置我方飞机右翼的双发子弹的初始位置
            double_bullet2.rect.center = (self.my_plane.rect.centerx +
                                          constants.DOUBLE_BULLET_OFFSET,
                                          self.my_plane.rect.centery)

            # 将创建的两颗双发子弹添加到管理所有双发子弹的分组中
            self.double_bullet_group.add(double_bullet1)
            self.double_bullet_group.add(double_bullet2)
        # 如果双发子弹计数器的值达到最大值
        else:
            # 在事件队列中每隔一段时间就生成一个自定义事件"创建子弹"
            pygame.time.set_timer(constants.ID_OF_CREATE_BULLET,
                                  constants.INTERVAL_OF_CREATE_BULLET)

            # 在事件队列中停止生成自定义事件"创建双发子弹"
            pygame.time.set_timer(constants.ID_OF_CREATE_DOUBLE_BULLET, 0)

            # 双发子弹的计数器重置为0
            self.double_bullet_counter = 0

    def _check_collisions(self):
        """检测碰撞"""

        # 检测子弹与小型敌机的碰撞
        self._check_collision_bullets_smalls()

        # 检测子弹与中型敌机的碰撞
        self._check_collision_bullets_midsorbigs(self.mid_enemy_group)

        # 检测子弹与大型敌机的碰撞
        self._check_collision_bullets_midsorbigs(self.big_enemy_group)

        # 检测我方飞机与敌机的碰撞
        self._check_collision_myplane_enemies()

        # 检测我方飞机与子弹补给的碰撞
        self._check_collision_myplane_bulletsupply()

    def _check_collision_bullets_smalls(self):
        """检测子弹与小型敌机的碰撞"""

        # 检测是否有子弹与小型敌机发生了碰撞
        dict_collided = pygame.sprite.groupcollide(self.small_enemy_group,
                                                   self.bullet_group,
                                                   False, True)

        # 如果检测到有子弹与小型敌机发生了碰撞
        if len(dict_collided) > 0:
            # 遍历所有发生碰撞的小型敌机
            for small_enemy in dict_collided.keys():
                # 如果某架小型敌机被标记为没有在切换爆炸图片
                if not small_enemy.is_switching_explode_image:
                    # 播放小型敌机爆炸的声音
                    small_enemy.play_explode_sound()
                    # 标记小型敌机正在切换爆炸图片
                    small_enemy.is_switching_explode_image = True

        # 遍历小型敌机分组中的所有小型敌机
        for small_enemy in self.small_enemy_group.sprites():
            # 如果某架小型敌机被标记为正在切换爆炸图片
            if small_enemy.is_switching_explode_image:
                # 切换小型敌机爆炸的图片
                small_enemy.switch_explode_image()

    def _check_collision_bullets_midsorbigs(self, enemy_group):
        """检测子弹与中型敌机或大型敌机的碰撞"""

        # 检测是否有子弹与敌机发生了碰撞
        dict_collided = pygame.sprite.groupcollide(enemy_group,
                                                   self.bullet_group,
                                                   False, True)

        # 如果检测到有子弹与敌机发生了碰撞
        if len(dict_collided) > 0:
            # 遍历所有发生碰撞的敌机
            for enemy in dict_collided.keys():
                # 如果敌机的能量大于0
                if enemy.energy > 0:
                    # 敌机的能量减1
                    enemy.energy -= 1
                # 如果敌机的能量等于0
                if enemy.energy == 0:
                    # 如果某架敌机被标记为没有在切换爆炸图片
                    if not enemy.is_switching_explode_image:
                        # 播放敌机爆炸的声音
                        enemy.play_explode_sound()
                        # 标记敌机正在切换爆炸图片
                        enemy.is_switching_explode_image = True
                # 如果敌机的能量不等于0
                else:
                    # 如果某架敌机被标记为没有在切换被击中图片
                    if not enemy.is_switching_hit_image:
                        # 标记敌机正在切换被击中图片
                        enemy.is_switching_hit_image = True

        # 遍历敌机分组中的所有敌机
        for enemy in enemy_group.sprites():
            # 如果某架敌机被标记为正在切换被击中图片
            if enemy.is_switching_hit_image:
                # 切换敌机被击中的图片
                enemy.switch_hit_image()

            # 如果某架敌机被标记为正在切换爆炸图片
            if enemy.is_switching_explode_image:
                # 切换敌机爆炸的图片
                enemy.switch_explode_image()

    def _check_collision_myplane_enemies(self):
        """检测我方飞机与敌机的碰撞"""

        # 检测所有敌机的分组中是否有敌机与我方飞机发生了碰撞
        list_collided = pygame.sprite.spritecollide(self.my_plane,
                                                    self.enemy_group,
                                                    False,
                                                    pygame.sprite.collide_mask)

        # 如果检测到有敌机和我方飞机发生了碰撞
        if len(list_collided) > 0:
            # 如果我方飞机不处于无敌状态
            if not self.my_plane.is_invincible:
                # 我方飞机的生命数减1
                self.my_plane.life_number -= 1

                # 如果我方飞机的生命数大于0
                if self.my_plane.life_number > 0:
                    # 重置我方飞机的位置
                    self.my_plane.reset_position()
                    # 标记我方飞机处于无敌状态
                    self.my_plane.is_invincible = True
                    # 在事件队列中每隔一段时间就生成一个自定义事件"解除我方飞机的无敌状态"
                    pygame.time.set_timer(constants.ID_OF_CANCEL_INVINCIBLE,
                                          constants.
                                          INTERVAL_OF_CANCEL_INVINCIBLE)
                    # 在事件队列中停止生成自定义事件"创建双发子弹"
                    pygame.time.set_timer(constants.ID_OF_CREATE_DOUBLE_BULLET, 0)
                    # 在事件队列中每隔一段时间就生成一个自定义事件"创建子弹"
                    pygame.time.set_timer(constants.ID_OF_CREATE_BULLET,
                                          constants.INTERVAL_OF_CREATE_BULLET)
                # 如果我方飞机的生命数等于0
                elif self.my_plane.life_number == 0:
                    # 标记结束游戏
                    self.is_gameover = True
                    # 停止定时器
                    self._stop_timers()

            # 遍历所有发生碰撞的敌机
            for enemy in list_collided:
                # 如果某架敌机被标记为没有在切换爆炸图片
                if not enemy.is_switching_explode_image:
                    # 播放敌机爆炸的声音
                    enemy.play_explode_sound()
                    # 标记敌机正在切换爆炸图片
                    enemy.is_switching_explode_image = True

        # 遍历所有敌机分组中的敌机
        for enemy in self.enemy_group.sprites():
            # 如果某架敌机被标记为正在切换爆炸图片
            if enemy.is_switching_explode_image:
                # 切换敌机爆炸的图片
                enemy.switch_explode_image()

    def _check_collision_myplane_bulletsupply(self):
        """检测我方飞机与子弹补给的碰撞"""

        # 检测所有子弹补给的分组中是否有子弹补给与我方飞机发生了碰撞
        list_collided = pygame.sprite.spritecollide(self.my_plane,
                                                    self.bullet_supply_group,
                                                    False,
                                                    pygame.sprite.collide_mask)

        # 如果检测到有子弹补给和我方飞机发生了碰撞
        if len(list_collided) > 0:
            # 遍历所有发生碰撞的子弹补给
            for bullet_supply in list_collided:
                # 播放子弹补给与我方飞机碰撞的声音
                bullet_supply.play_collide_sound()
                # 将子弹补给从管理它的所有分组中删除
                bullet_supply.kill()

            # 在事件队列中停止生成自定义事件"创建子弹"
            pygame.time.set_timer(constants.ID_OF_CREATE_BULLET, 0)

            # 在事件队列中每隔一段时间就生成一个自定义事件"创建双发子弹"
            pygame.time.set_timer(constants.ID_OF_CREATE_DOUBLE_BULLET,
                                  constants.
                                  INTERVAL_OF_CREATE_DOUBLE_BULLET)

            # 双发子弹的计数器重置为0
            self.double_bullet_counter = 0

    def _draw_elements(self):
        """在窗口中绘制所有画面元素"""

        # 在窗口中绘制我方飞机
        self.my_plane.draw()

        # 在窗口中绘制所有子弹
        self.bullet_group.draw(self.window)

        # 在窗口中绘制所有双发子弹
        self.double_bullet_group.draw(self.window)

        # 在窗口中绘制所有子弹补给
        self.bullet_supply_group.draw(self.window)

        # 在窗口中绘制所有小型敌机
        self.small_enemy_group.draw(self.window)

        # 在窗口中绘制所有中型敌机
        self.mid_enemy_group.draw(self.window)

        # 在窗口中绘制所有中型敌机的能量线
        for mid_enemy in self.mid_enemy_group.sprites():
            # 在中型敌机的尾部上方绘制能量线
            mid_enemy.draw_energy_lines()

        # 在窗口中绘制所有大型敌机
        self.big_enemy_group.draw(self.window)

        # 在窗口中绘制所有大型敌机的能量线
        for big_enemy in self.big_enemy_group.sprites():
            # 在大型敌机的尾部上方绘制能量线
            big_enemy.draw_energy_lines()

        # 在窗口中绘制我方飞机的所有生命图片
        for i in range(self.my_plane.life_number):
            # 在窗口的指定位置绘制我方飞机的生命图片
            self.window.blit(self.my_plane.life_image,
                             self.my_plane.life_rect_list[i])

        # 如果我方飞机处于无敌状态
        if self.my_plane.is_invincible:
            # 在窗口中绘制我方飞机处于无敌状态时的提示文本
            self._draw_invincible_prompt_text()

        # 如果游戏结束
        if self.is_gameover:
            # 在窗口中绘制游戏结束时的提示文本
            self._draw_gameover_prompt_text()

    def _draw_invincible_prompt_text(self):
        """在窗口中绘制我方飞机处于无敌状态时的提示文本"""

        # 我方飞机处于无敌状态时的提示文本
        prompt_text = "还有{}条命，无敌状态将在该文本消失后解除".\
            format(self.my_plane.life_number)

        # 获得提示文本对应的surface对象
        prompt_text_surface = self.font_36.render(prompt_text,
                                                  True,
                                                  constants.WHITE_COLOR)

        # 获得提示文本的矩形
        prompt_text_surface_rect = prompt_text_surface.get_rect()

        # 将提示文本的矩形定位在窗口的中部
        prompt_text_surface_rect.center = self.window.get_rect().center

        # 在窗口的中部绘制提示文本
        self.window.blit(prompt_text_surface, prompt_text_surface_rect)

    def _draw_gameover_prompt_text(self):
        """在窗口中绘制游戏结束时的提示文本"""

        # 游戏结束时的提示文本
        prompt_text = "游戏结束"

        # 获得提示文本对应的surface对象
        prompt_text_surface = self.font_96.render(prompt_text,
                                                  True,
                                                  constants.WHITE_COLOR)

        # 获得提示文本的矩形
        prompt_text_surface_rect = prompt_text_surface.get_rect()

        # 将提示文本的矩形定位在窗口的中部
        prompt_text_surface_rect.center = self.window.get_rect().center

        # 在窗口的中部绘制提示文本
        self.window.blit(prompt_text_surface, prompt_text_surface_rect)

    def _update_positions(self):
        """更新窗口中所有画面元素的位置"""

        # 更新我方飞机的位置
        self.my_plane.update()

        # 更新所有子弹的位置
        self.bullet_group.update()

        # 更新所有双发子弹的位置
        self.double_bullet_group.update()

        # 更新所有子弹补给的位置
        self.bullet_supply_group.update()

        # 更新所有小型敌机的位置
        self.small_enemy_group.update()

        # 更新所有中型敌机的位置
        self.mid_enemy_group.update()

        # 更新所有大型敌机的位置
        self.big_enemy_group.update()

    def _delete_invisible_elements(self):
        """删除窗口中所有不可见的画面元素"""

        # 删除窗口中所有不可见的子弹
        self._delete_invisible_bulletsordouble(self.bullet_group)

        # 删除窗口中所有不可见的双发子弹
        self._delete_invisible_bulletsordouble(self.double_bullet_group)

        # 删除窗口中所有不可见的子弹补给
        self._delete_invisible_enemies_supplies(self.bullet_supply_group)

        # 删除窗口中所有不可见的敌机
        self._delete_invisible_enemies_supplies(self.enemy_group)

    def _delete_invisible_bulletsordouble(self, group):
        """删除窗口中所有不可见的子弹或双发子弹"""

        # 遍历子弹分组或双发子弹分组
        for sprite in group.sprites():
            # 如果某颗子弹或某颗双发子弹在窗口中不可见了
            if sprite.rect.bottom <= 0:
                # 从管理它的所有分组中删除
                sprite.kill()

    def _delete_invisible_enemies_supplies(self, group):
        """删除窗口中所有不可见的敌机或子弹补给"""

        # 遍历管理所有敌机的分组或子弹补给的分组
        for sprite in group.sprites():
            # 如果某架敌机或某个子弹补给在窗口中不可见了
            if sprite.rect.top >= self.window.get_rect().height:
                # 将该架敌机或该子弹补给从管理它的所有分组中删除
                sprite.kill()

    def _switch_images(self):
        """切换窗口中画面元素的图片"""

        # 切换我方飞机的图片
        self.my_plane.switch_image()

        # 切换所有大型敌机的图片
        for big_enemy in self.big_enemy_group.sprites():
            # 切换大型敌机的图片
            big_enemy.switch_image()


# 只有当直接运行main.py时
if __name__ == '__main__':
    # 运行游戏
    PlaneWar().run_game()
