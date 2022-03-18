"""所有常量"""
import pygame

# 指定最大帧率
MAX_FRAMERATE = 30

# 在垂直刻度,窗口尺寸占电脑屏幕尺寸的比例
SCALE_VERTICAL = 4 / 5
# 在水平刻度,窗口尺寸占电脑屏幕尺寸的比例
SCALE_HORIZONTAL = 2 / 5

# 自定义事件'创建子弹'的ID
ID_OF_CREATE_BULLET = pygame.USEREVENT
# 自定义事件'创建子弹'的时间间隔
INTERVAL_OF_CREATE_BULLET = 300

# 自定义事件'创建敌机'的ID
ID_OF_CREATE_SMALL_ENEMY = pygame.USEREVENT + 1
# 自定义事件'创建小型敌机'的时间间隔
INTERVAL_OF_CREATE_SMALL_ENEMY = 2000
# 自定义事件'创建中型敌机'的ID

ID_OF_CREATE_MID_ENEMY = pygame.USEREVENT + 2
# 自定义事件'创建中型敌机'的时间间隔
INTERVAL_OF_CREATE_MID_ENEMY = 4800

# 自定义事件'创建大型敌机'的ID
ID_OF_CREATE_BIG_ENEMY = pygame.USEREVENT + 3
# 自定义事件'创建大型敌机'的时间间隔
INTERVAL_OF_CREATE_BIG_ENEMY = 18000

# 自定义事件'解除我方飞机的无敌状态'的ID
ID_OF_CANCEL_INVINCIBLE = pygame.USEREVENT + 4
# 自定义事件'解除我方飞机的无敌状态'的时间间隔
INTERVAL_OF_CANCEL_INVINCIBLE = 5000

# 我方飞机图片切换频率
MY_PLANE_SWITCH_TIME_FREQUENCY = 3

# 小型敌机爆炸时的音量
SMALL_ENEMY_EXPLODE_SOUND = 0.8

# 小型敌机爆炸时的图片切换频率
SMALL_ENEMY_SWITCH_EXPLODE_IMAGE_FREQUENCY = 4

# 中型敌机爆炸时的音量
MID_ENEMY_EXPLODE_SOUND = 0.8

# 中型敌机爆炸时的图片切换频率
MID_ENEMY_SWITCH_EXPLODE_IMAGE_FREQUENCY = 3

# 中型敌机的初始能量
MID_ENEMY_INITIAL_ENERGY = 3

# 中型敌机击中特性的图片切换频率
MID_PLANE_SWITCH_HIT_IMAGE_FREQUENCY = 3

# 大型敌机爆炸时的音量
BIG_ENEMY_EXPLODE_SOUND = 0.8

# 大型敌机爆炸时的图片切换频率
BIG_ENEMY_SWITCH_EXPLODE_IMAGE_FREQUENCY = 6

# 大型敌机的初始能量
BIG_ENEMY_INITIAL_ENERGY = 6

# 大型敌机击中效果的图片切换频率
BIG_PLANE_SWITCH_HIT_IMAGE_FREQUENCY = 3

# 大型敌机飞行效果图片切换频率
BIG_ENEMY_SWITCH_TIME_FREQUENCY = 3

# 间距
MARGIN = 10

# 字体大小
FONT_SIZE_36 = 36

# 白色
WHITE_COLOR = (255,255,255)
