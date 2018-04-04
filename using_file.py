#!/usr/bin/python
# Filename: using_file.py

import os
import cPickle

file01 = 'contact.db'

text = []

def data_add():
    name = raw_input('place input a name >>>')
    text.append({'name': name})
    data_save()

def data_save():
    s = cPickle.dumps(text)
    fl = file(file01, 'w')
    fl.write(s)
    fl.close()

def data_disp():
    if len(file01) > 0:
        print "name"
        print '----------------------------'
        for x in text:
            print "%(name)s" % x
    else:
        print
        print ">>> This is a empty file,There is no infomation! >>>"

def data_load():
    if os.path.exists(file01):
        rd = file(file01)
        s = rd.read()
        rd.close()
        text.extend(cPickle.loads(s))

data_add()
data_load()
data_save()
data_disp()
