#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
使用python自带函数
'''

from itertools import permutations
t = 0
for i in permutations('1234', 3):
    print(''.join(i))
    t += 1  # 通过每次循环自加，计算组合数量

print("不重复的数量有:%s"%t)