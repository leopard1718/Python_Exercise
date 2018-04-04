#!/usr/bin/python
# Filename: objvar.py

class shengwu:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print '(Initialized shenwu: %s)' % self.name

    def tell(self):
        print '(Name:"%s" Age:"%s")' % (self.name, self.age)


class dongwu(shengwu):
    def __init__(self, name, age, zhonglei):
        shengwu.__init__(self, name, age)
        self.zhonglei = zhonglei
        print '(Initialized dongwu: %s)' % self.name

    def tell(self):
        shengwu.tell(self)
        print '(zhonglei: %s)' % self.zhonglei


class zhiwu(shengwu):
    def __init__(self, name, age, liebei):
        shengwu.__init__(self, name, age)
        self.liebei = liebei
        print '(Initialized zhiwu:%s)' % self.name

    def tell(self):
        shengwu.tell(self)
        print '(liebei:%s)' % self.liebei

t = dongwu('dog', 10, 'youjizhui')
s = zhiwu('tree', 100, 'muben')

members = [t, s]
for member in members:
    member.tell()