#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。

'''

for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != k) and (i != j) and (j != k):  # 判断三个变量互不相等
                print i, j, k

