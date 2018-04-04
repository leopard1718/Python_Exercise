#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
使用列表计算组合数量。
'''

d = []   # 创建列表
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if(i != j) and (j != k) and (i != k):
                #  还可以写成“i != j != k and i != k” 但是不要直接写成i != j != k
                d.append([i, j, k])  # 将不同的三位数写入列表
print "总数量：", len(d)   # 使用len函数读取列表长度 并输出
print d   # 打印列表中数据
