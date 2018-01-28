#!/usr/bin/env python
#coding=utf-8
def getAge(age=123):
    if age > 122:
        return "大于122"
    elif age < 1000:
        return "小于1000"
    else:
        return "bye"
print "come into testmodule"

class People(object):
    def getName(self,name="张三"):
        return "你好呀！%s"%name

