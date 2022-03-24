"""所有常量"""

import pygame


# 在水平方向上，窗口尺寸占电脑屏幕尺寸的比例
SCALE_HORIZONTAL = 2 / 5
# 在竖直方向上，窗口尺寸占电脑屏幕尺寸的比例
SCALE_VERTICAL = 4 / 5

# 动画的最大帧率
MAX_FRAMERATE = 30

# 自定义事件"创建子弹"的id
ID_OF_CREATE_BULLET = pygame.USEREVENT
# 自定义事件"创建双发子弹"的id
ID_OF_CREATE_DOUBLE_BULLET = pygame.USEREVENT + 6
# 自定义事件"创建子弹补给"的id
ID_OF_CREATE_BULLET_SUPPLY = pygame.USEREVENT + 5
# 自定义事件"创建小型敌机"的id
ID_OF_CREATE_SMALL_ENEMY = pygame.USEREVENT + 1
# 自定义事件"创建中型敌机"的id
ID_OF_CREATE_MID_ENEMY = pygame.USEREVENT + 2
# 自定义事件"创建大型敌机"的id
ID_OF_CREATE_BIG_ENEMY = pygame.USEREVENT + 3
# 自定义事件"解除我方飞机的无敌状态"的id
ID_OF_CANCEL_INVINCIBLE = pygame.USEREVENT + 4

# 自定义事件"创建子弹"的时间间隔
INTERVAL_OF_CREATE_BULLET = 500
# 自定义事件"创建双发子弹"的时间间隔
INTERVAL_OF_CREATE_DOUBLE_BULLET = 500
# 自定义事件"创建子弹补给"的时间间隔
INTERVAL_OF_CREATE_BULLET_SUPPLY = 25000
# 自定义事件"创建小型敌机"的时间间隔
INTERVAL_OF_CREATE_SMALL_ENEMY = 2000
# 自定义事件"创建中型敌机"的时间间隔
INTERVAL_OF_CREATE_MID_ENEMY = 3600
# 自定义事件"创建大型敌机"的时间间隔
INTERVAL_OF_CREATE_BIG_ENEMY = 18000
# 自定义事件"解除我方飞机的无敌状态"的时间间隔
INTERVAL_OF_CANCEL_INVINCIBLE = 5000

# 爆炸声音的音量
EXPLODE_SOUND_VOLUME = 0.8
# 碰撞声音的音量
COLLIDE_SOUND_VOLUME = 0.8

# 切换我方飞机图片的频率
MY_PLANE_SWITCH_IMAGE_FREQUENCY = 3
# 切换大型敌机图片的频率
BIG_ENEMY_SWITCH_IMAGE_FREQUENCY = 3
# 切换小型敌机爆炸图片的频率
SMALL_ENEMY_SWITCH_EXPLODE_IMAGE_FREQUENCY = 8
# 切换中型敌机爆炸图片的频率
MID_ENEMY_SWITCH_EXPLODE_IMAGE_FREQUENCY = 8
# 切换大型敌机爆炸图片的频率
BIG_ENEMY_SWITCH_EXPLODE_IMAGE_FREQUENCY = 6
# 切换中型敌机被击中图片的频率
MID_ENEMY_SWITCH_HIT_IMAGE_FREQUENCY = 3
# 切换大型敌机被击中图片的频率
BIG_ENEMY_SWITCH_HIT_IMAGE_FREQUENCY = 3

# 中型敌机的初始能量
MID_ENEMY_INITIAL_ENERGY = 5
# 大型敌机的初始能量
BIG_ENEMY_INITIAL_ENERGY = 10

# 间距
MARGIN = 10

# 36号字体大小
FONT_SIZE_36 = 36
# 96号字体大小
FONT_SIZE_96 = 96

# 白色
WHITE_COLOR = (255, 255, 255)

# 双发子弹在水平方向上距离我方飞机中心的偏移量
DOUBLE_BULLET_OFFSET = 32

# 双发子弹计数器的最大值
DOUBLE_BULLET_COUNTER_MAX = 16
