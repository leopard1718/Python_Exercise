#!/usr/bin/env python
# coding:utf8
# Author:zhuima
# Date:2015-03-22
# Version:0.1
# Function:display a list and add date



# 导入模块
import os
import cPickle

fname = 'contact.db'

txl = []


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


def txl_add():
    '''添加用户'''
    name = raw_input('Please Enter Your Name >>> ')
    age = raw_input('Please Enter Your Age >>> ')
    gender = raw_input('Please Enter Your Gender >>> ')
    tel = raw_input('Please Enter Your Tel >>> ')
    txl.append({'name': name, 'age': age, 'gender': gender, 'tel': tel})
    txl_save()


def txl_disp():
    '''显示原始的txl列表 '''
    if len(txl) > 0:
        print "name\tage\tgender\ttel"
        print '----------------------------'
        for x in txl:
            print "%(name)s\t%(age)s\t%(gender)s\t%(tel)s" % x
    else:
        print
        print ">>> This is a empty file,There is no infomation! >>>"


def txl_save():
    '''对数据进行写操作，写之前进行格式转换'''
    s = cPickle.dumps(txl)
    fp = file(fname, 'w')
    fp.write(s)
    fp.close()


def txl_load():
    '''对文件进行读取，如果文件存在的情况下 '''
    if os.path.exists(fname):
        fp = file(fname)
        s = fp.read()
        fp.close()
        txl.extend(cPickle.loads(s))


def txl_update(status=True):
    '''根据用户名对该用户的相关数据进行更新操作,用户名不可变，如果选项不更新，则保留默认值，否则更新'''
    txl_disp()
    name = raw_input('Select One Update By Name >>> ')
    for line in txl:
        if line['name'] == name:
            status = False
            old_age = line['age']
            old_gender = line['gender']
            old_tel = line['tel']
            age = raw_input('Please Enter Your Age for %s >>> ' % name)
            gender = raw_input('Please Enter Your Gender for %s >>> ' % name)
            tel = raw_input('Please Enter Your Tel for %s >>> ' % name)
            if len(age) == 0:
                line['age'] = old_age
            else:
                line['age'] = age
            if len(gender) == 0:
                line['gender'] = old_gender
            else:
                line['gender'] = gender
            if len(tel) == 0:
                line['tel'] = old_tel
            else:
                line['tel'] = tel
            break
    if status:
        print "Unkonw User,Try Again!"
    txl_save()


def txl_del():
    '''根据用户名进行删除用户相应的信息，并进行数据存储'''
    name = raw_input('Please Enter Your Want To Delete name >>> ')
    for line in txl:
        if line['name'] == name:
            txl.remove(line)
            break
    txl_save()


def txl_sort():
    '''根据用户的输入对数据进行排序，用到了lambda函数 '''
    op = raw_input('Order By [name | age | gender | tel ] Display >>> ')
    txl.sort(key=lambda x: x[op])
    txl_disp()


def txl_exit():
    ''' 退出程序 '''
    os._exit(0)


def txl_error():
    ''' 当用户输出选项不在定义的选项内的时候，报错'''
    print
    print 'Unkonw options,Please try again!'


# 定义dict，配合函数实现switch功能

ops = {
    '1': txl_add,
    '2': txl_disp,
    '3': txl_update,
    '4': txl_del,
    '5': txl_sort,
    '0': txl_exit,
}

txl_load()


def main():
    '''主程序 '''
    while True:
        op = menu()
        ops.get(op, txl_error)()


if __name__ == '__main__':
    main()