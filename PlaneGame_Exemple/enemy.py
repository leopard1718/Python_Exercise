# -*- coding: utf-8 -*-
# ===============================================================================
# ��Ҫ���ܣ�����з��ɻ��������õз��ɻ����������
# �㷨���̣�1�����طɻ�ͼƬ������ɻ�����λ��
#           2������л����ƶ���Խ������
# ע�����1�����͵л�����ʱ��֡�л���Ч�������ض�������Ч
#           2��ע�����active�������жϷɻ�����������
# ===============================================================================
# �������ģ��

import pygame
from random import *


# ====================����С�͵л�������Ϊ====================
class SmallEnemy(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/enemy1.png")  # ���صз��ɻ�ͼƬ
        self.mask = pygame.mask.from_surface(self.image)
        self.destroy_images = []  # ���طɻ����ͼƬ
        self.destroy_images.extend([pygame.image.load("image/enemy1_down1.png"),
                                    pygame.image.load("image/enemy1_down2.png"),
                                    pygame.image.load("image/enemy1_down3.png"),
                                    pygame.image.load("image/enemy1_down4.png")])
        self.rect = self.image.get_rect()  # ��õз��ɻ���λ��
        self.width, self.height = bg_size[0], bg_size[1]  # ���ػ�����ͼƬλ��
        self.speed = 2  # ���õл����ٶ�
        self.rect.left, self.rect.top = (randint(0, self.width - self.rect.width),  # ����л����ֵ�λ��
                                         randint(-5 * self.rect.height, 0)  # ��֤�л������ڳ����ѿ�ʼ����������
                                         )
        self.active = True  # ���÷ɻ���ǰ�Ĵ������ԣ�True��ʾ�ɻ��������У�False��ʾ�ɻ������

    def move(self):  # ����л����ƶ�����
        if self.rect.top < self.height - 60:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):  # ���л������ƶ�����Ļʱ
        self.rect.left, self.rect.top = (randint(0, self.width - self.rect.width),
                                         randint(-5 * self.rect.height, 0)
                                         )
        self.active = True  # ���÷ɻ��Ĵ���־λ�������л�����


# ====================�������͵л�������Ϊ====================
class MidEnemy(pygame.sprite.Sprite):
    energy = 5  # �л�Ѫ��

    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/enemy2.png")  # ���صз��ɻ�ͼƬ
        self.image_hit = pygame.image.load("image/enemy2_hit.png")  # ���صз��ɻ��е�ͼƬ
        self.mask = pygame.mask.from_surface(self.image)
        self.destroy_images = []  # ���طɻ����ͼƬ
        self.destroy_images.extend([pygame.image.load("image/enemy2_down1.png"),
                                    pygame.image.load("image/enemy2_down2.png"),
                                    pygame.image.load("image/enemy2_down3.png"),
                                    pygame.image.load("image/enemy2_down4.png")])
        self.rect = self.image.get_rect()  # ��õз��ɻ���λ��
        self.width, self.height = bg_size[0], bg_size[1]  # ���ػ�����ͼƬλ��
        self.speed = 1  # ���õл����ٶȣ�Ӧ�ñ�С�͵л��ٶ�����
        self.rect.left, self.rect.top = (randint(0, self.width - self.rect.width),  # ����л����ֵ�λ��
                                         randint(-10 * self.rect.height, -self.rect.height)
                                         )
        self.active = True
        self.energy = MidEnemy.energy
        self.hit = False  # �ɻ��Ƿ񱻻��б�־λ

    def move(self):  # ����л����ƶ�����
        if self.rect.top < self.height - 60:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):  # ���л������ƶ�����Ļʱ
        self.rect.left, self.rect.top = (randint(0, self.width - self.rect.width),  # ����л����ֵ�λ��
                                         randint(-10 * self.rect.height, -self.rect.height)  # ��֤һ��ʼ���������͵л�����
                                         )
        self.active = True
        self.energy = MidEnemy.energy
        self.hit = False


# ====================������͵л�������Ϊ====================
class BigEnemy(pygame.sprite.Sprite):
    energy = 15

    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load("image/enemy3_n1.png")  # ���صз��ɻ�ͼƬ�����д��ͷɻ���֡�л�����Ч
        self.image2 = pygame.image.load("image/enemy3_n2.png")
        self.image_hit = pygame.image.load("image/enemy3_hit.png")  # ���صз��ɻ��е�ͼƬ
        self.mask = pygame.mask.from_surface(self.image1)
        self.destroy_images = []  # ���طɻ����ͼƬ
        self.destroy_images.extend([pygame.image.load("image/enemy3_down1.png"),
                                    pygame.image.load("image/enemy3_down2.png"),
                                    pygame.image.load("image/enemy3_down3.png"),
                                    pygame.image.load("image/enemy3_down4.png"),
                                    pygame.image.load("image/enemy3_down5.png"),
                                    pygame.image.load("image/enemy3_down6.png")])
        self.rect = self.image1.get_rect()  # ��õз��ɻ���λ��
        self.width, self.height = bg_size[0], bg_size[1]  # ���ػ�����ͼƬλ��
        self.speed = 2  # ���õл����ٶ�
        self.rect.left, self.rect.top = (randint(0, self.width - self.rect.width),  # ����л����ֵ�λ��
                                         randint(-15 * self.rect.height, -5 * self.rect.height)
                                         )
        self.active = True
        self.energy = BigEnemy.energy
        self.hit = False  # �ɻ��Ƿ񱻻��б�־λ

    def move(self):  # ����л����ƶ�����
        if self.rect.top < self.height - 60:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):  # ���л������ƶ�����Ļʱ
        self.rect.left, self.rect.top = (randint(0, self.width - self.rect.width),  # ����л����ֵ�λ��
                                         randint(-15 * self.rect.height, -5 * self.rect.height)
                                         )
        self.active = True
        self.energy = BigEnemy.energy
        self.hit = False
