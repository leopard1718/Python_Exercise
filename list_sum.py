#!/usr/bin/python
# -*- coding: UTF-8 -*-

size_list = []

for file_size_list in open('1.txt', 'r'):
    #print file_size_list
    #print type(file_size_list)
    while 1:
        rs = float(file_size_list.strip("\r"))
        size_list.append(rs)
        break
sum_result = sum(size_list)/1024/1024/1024
print sum_result, 'T'
