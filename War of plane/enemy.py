# -*- coding: utf-8 -*-
# 导入相关模块

import pygame
from random import *

class SmallEnemy(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/enemy1.png")  # 加载敌机图片
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]   # 本地化背景图片位置
        self.speed = 10    # 设置敌机速度

        self.rect.left, self.rect.top = (randint(0, self.width - self.rect.width),
                                         randint(-5 * self.rect.height, 0)
                                         )

    def move(self):     # 定义敌机移动函数
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.rect.left, self.rect.top = (randint(0, self.width - self.rect.width),
                                         randint(-5 * self.rect.height, 0)
                                         )








