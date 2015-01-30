__author__ = 'crixalis'
# coding:utf-8
#!/usr/bin/env python

def isleap(year):
    if ((year%4==0) and (year%100!=0)) or year%400==0:
        return True
    else:
        return False
print isleap(2012)

nu = [4,100,400]
def isleap(year):
    for i in nu:
        if ((year%i == 0)):
                return True
        else:
                return False
print isleap(2013)

def isLeap(num):
    if num % 4 == 0 and num % 100 != 0 or num % 400 == 0:
        return 'this year %s is leap year' % num
    else:
        return 'this year %s is not a leap year' % num

print isLeap(2014)

def isLeap():
    while True:
        Nian = raw_input("Input a year:")

        if Nian == "exit":
            break

        year = int(Nian)
        if year < 1582:
            print "There is no define of Leap before 1582"
            continue
        else:
            if year % 4 == 0 and year %100 != 0 or year % 400 ==0:
                leap = 1
            else:
                leap = 0
        if leap == 1:
            print str(year) + " is leap"
            break
        elif leap == 0:
            print str(year) + " is not leap"
            break

isLeap()