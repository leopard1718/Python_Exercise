#!/usr/bin/env python
# coding:utf8
# Author:zhuima
# Date:2015-03-22
# Version:0.1
# Function:display a list and add date


def menu():
    '''设置munu目录，提供给用户的操作接口 '''
    print '''
        1.add user info
        2.disp all user info
        3.update user info by username
        4:del user by username
        5:sort user info by
        0.exit program
    '''
    op = raw_input('Please select one >>> ')
    return op

menu()

