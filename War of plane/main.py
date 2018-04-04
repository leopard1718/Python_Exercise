# -*- coding: utf-8 -*-
# 导入相关模块

import pygame
import sys
import traceback
import myplane
import enemy
from random import *
from pygame.locals import *

# ===================initialize====================
pygame.init()
pygame.mixer.init()   # mixer initialize
bg_size = width, height = 480, 640   # background size
screen = pygame.display.set_mode(bg_size) #set up background display
pygame.display.set_caption("WAR OF PLANE")
background = pygame.image.load("image/background.png")


# ===================load game music======================
pygame.mixer.music.load("sound/game_music.wav")
pygame.mixer.music.set_volume(0.2)
bullet_sound = pygame.mixer.Sound("sound/bullet.wav")
bullet_sound.set_volume(0.2)
big_enemy_flying_sound = pygame.mixer.Sound("sound/big_spaceship_flying.wav")
big_enemy_flying_sound.set_volume(0.2)
enemy1_down_sound = pygame.mixer.Sound("sound/enemy1_down.wav")
enemy1_down_sound.set_volume(0.2)
enemy2_down_sound = pygame.mixer.Sound("sound/enemy2_down.wav")
enemy2_down_sound.set_volume(0.2)
enemy3_down_sound = pygame.mixer.Sound("sound/enemy3_down.wav")
enemy3_down_sound.set_volume(0.2)
me_down_sound = pygame.mixer.Sound("sound/game_over.wav")
me_down_sound.set_volume(0.2)
button_down_sound = pygame.mixer.Sound("sound/button.wav")
button_down_sound.set_volume(0.2)
level_up_sound = pygame.mixer.Sound("sound/achievement.wav")
level_up_sound.set_volume(0.2)
bomb_sound = pygame.mixer.Sound("sound/use_bomb.wav")
bomb_sound.set_volume(0.2)
get_bomb_sound = pygame.mixer.Sound("sound/get_bomb.wav")
get_bomb_sound.set_volume(0.2)
get_bullet_sound = pygame.mixer.Sound("sound/get_double_laser.wav")
get_bullet_sound.set_volume(0.2)

# ====================敌方飞机生成控制函数====================
def add_small_enemies(group1, group2, num):
    for i in range(num):
        e1 = enemy.SmallEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)


def main():
    pygame.mixer.music.play(-1)
    me = myplane.MyPlane(bg_size)  # 生成我方飞机
    running = True
    switch_image = False
    delay = 60     # 延时60帧


    # ====================实例化敌方飞机====================
    enemies = pygame.sprite.Group()  # 生成敌方飞机组
    small_enemies = pygame.sprite.Group()   # 敌方小型飞机组
    add_small_enemies(small_enemies, enemies, 1)  # 生成若干敌方小型飞机

    while running:
        clock = pygame.time.Clock()  # 设置帧率
        clock.tick(60)  # 设置帧数为60
        switch_image = not switch_image
        screen.blit(background, (0, 0))

        if delay == 0:
            delay = 60
        delay -= 1

        if not delay % 3:
            switch_image = not switch_image

        if switch_image:
            screen.blit(me.image1, me.rect)
        else:
            screen.blit(me.image2, me.rect)

        key_pressed = pygame.key.get_pressed()  # 获得用户所有的键盘输入序列
        if key_pressed[K_w] or key_pressed[K_UP]:  # 如果用户通过键盘发出“向上”的指令,其他类似
            me.move_up()
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            me.move_down()
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            me.move_left()
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            me.move_right()

        for each in small_enemies:  # 绘制小型敌机并自动移动
            each.move()
            screen.blit(each.image, each.rect)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()



if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()

