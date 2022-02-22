"""测试PyGame矩形"""
import pygame

# Rect(left, top, width, height) -> Rect
rect = pygame.Rect(100, 50, 180, 120)
print('left =', rect.left)
print('top =', rect.top)
print('width =', rect.width)
print('height =', rect.height)
# right = left + width
print('right =', rect.right)
# bottom = top + height
print('bottom =', rect.bottom)
# center x = left + width / 2
print('center x =', rect.centerx)
# center y = top + height / 2
print('center y =', rect.centery)

# x = left
print('x = ', rect.x)
# y = top
print('y = ', rect.y)
# w = width
print('w = ', rect.w)
# h = height
print('h = ', rect.h)

# size = (width, height) 矩形大小
print('size =', rect.size)
# center = (center x, center y) 矩形中心坐标
print('center =', rect.center)
# top_left = (left, top) 矩形左上角坐标
print('top_left =', rect.topleft)
# bottom_left = (bottom, left) 矩形左下角坐标
print('bottom_left', rect.bottomleft)
# top_right = (top, right) 矩形右上角
print('top_right =', rect.topright)
# bottom_right = (bottom, right) 矩形右下角
print('bottom_right = ', rect.bottomright)
# mid_top = (center_x, top) 矩形上方中心坐标
print('mid_top = ', rect.midtop)
# mid_left = (left, center_y) 矩形左方中心坐标
print('mid_left = ', rect.midleft)
# mid_bottom = (center_x, bottom) 矩形下方中心坐标
print('mid_bottom = ', rect.midbottom)
# mid_right = (right, center_y)  矩形右方中心坐标
print('mid_right = ', rect.midright)
