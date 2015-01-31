__author__ = '100068'
# coding:utf-8
# !/usr/bin/env python
class Human(object):
    laugh='hahahaha'
    def show_laugh(self):
        print self.laugh
    def laugh_100th(self):
        for i in range(100):
            self.show_laugh()


li_lei=Human()
li_lei.laugh_100th()

