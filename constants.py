"""所有常量"""
import pygame

# 指定最大帧率
MAX_FRAMERATE = 60
# 在垂直刻度,窗口尺寸占电脑屏幕尺寸的比例
SCALE_VERTICAL = 4 / 5
# 在水平刻度,窗口尺寸占电脑屏幕尺寸的比例
SCALE_HORIZONTAL = 2 / 5
# 自定义事件'创建子弹'的ID
ID_OF_CREATE_BULLET = pygame.USEREVENT
# 自定义事件'创建子弹'的时间间隔
INTERVAL_OF_CREATE_BULLET = 500
# 自定义事件'创建敌机'的ID
ID_OF_CREATE_SMALL_ENEMY = pygame.USEREVENT + 1
# 自定义事件'创建小型敌机'的时间间隔
INTERVAL_OF_CREATE_SMALL_ENEMY = 2000
# 自定义事件'创建中型敌机'的ID
ID_OF_CREATE_MID_ENEMY = pygame.USEREVENT + 2
# 自定义事件'创建中型敌机'的时间间隔
INTERVAL_OF_CREATE_MID_ENEMY = 3500
