#!/usr/bin/python
# coding=utf-8
'''
import xml.etree.ElementTree as ET
from os import popen
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

msg = (popen('ipconfig').read())

print msg.decode('gbk')


list = ('lili', 'nana', 'xiaochen')
i = 0

while True:
    print len(list[i])
    i += 1
    if i >= 3:
        break

for name in list:
    print '你好',name
'''




import os

# where are we?
cwd = os.getcwd()
print "1", cwd.decode('gbk')

# go down
os.chdir("text")
print "2", os.getcwd().decode('gbk')

# go back up
os.chdir(os.pardir)
print "3", os.getcwd().decode('gbk')





'''
file01 = 'timer_set.xml'



s = cPickle.dumps(msg)
fl = file(file01, 'w')
fl.write(s)
fl.close()

tree = ET.fromstring(msg)
for commendid in tree.findall('body')[0].findall('timer'):
    # print commendid.attrib.get('id')
    # id = commendid.attrib.get('id')
    commendid.set("id", "1234567")
    print commendid.attrib.get('id')
    print tree

timer_list = ('tsu-record-monitor', 'tsu-record-query', 'tsu-record-start')
for timer_id in timer_list:
    print timer_id
    tree = ET.parse('timer_set.xml')
    for commendid in tree.findall('body')[0].findall('timer'):
        if commendid.attrib['id'] != '':
            commendid.set("id", timer_id)
        else:
            commendid.set("id", timer_id)
        tree.write('timer_set.xml')
'''

