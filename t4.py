# #析构方法   对应同一空间的都被删除才会有del，函数调用类会在函数结束时del
#
# '''
# class stu:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         print('name:%s has been created!'%self.name)
#
#     def __del__(self):
#         print('%s is deleted'%self.name)
#
# def func(name,age):
#     st=stu(name,age)
#
# if __name__=='__main__':
#     st1 = stu('wangan',25)
#     st2 = stu('wangshu',26)
#     print(st2)
#     st3=st2
#     print(st3)
#     print(st1)
#     print(st2)
#     #del st1
#     del st2
#     func('zhang',49)
#     print('668885555')
#     print(st3)
#     print(st3.name)
#     del st3
#     st4 = func('zhao',39)
#     '''
#
#
# #内置方法
# '''
# class comp:
#     def __init__(self,real,image):
#         self.real = real
#         self.image = image
#
#
#     def __str__(self):
#         return str(self.real)+'+'+str(self.image)+'j'
# if __name__=='__main__':
#     c=comp(3.2,5.4)
#     print(c)
# '''
#
# '''
# class compare:
#         def __init__(self,name,age):
#             self.name= name
#             self.age= age
#
#         def __le__(self,other):
#             return self.age<=other.age
#
# if __name__=='__main__':
#     m = compare('zzw',16)
#     n = compare('ws',17)
#     print(m<=n)
# '''
# #子类
# '''
# class person:
#     def setname(self,name):
#         self.name = name
# class Student(person):
#     def setsno(self,sno):
#         self.sno = sno
# class teacher(person):
#     def settno(self,tno):
#         self.tno = tno
# class TA(Student,teacher):
#     def settea(self,teacher):
#         self.teacher=teacher
# if __name__=='__main__':
#     stu = Student()
#     stu.setname('wangan')
#     stu.setsno('01101')
#     print('ID:%s,Name:%s'%(stu.sno,stu.name))
#     tea = teacher()
#     tea.setname('ma')
#     tea.settno('5555')
#     print('ID:%s,Name:%s'%(tea.tno,tea.name))
#     zhu = TA()
#     zhu.setname('sss')
#     zhu.settno('335')
#     zhu.setsno('6564')
#     zhu.settea('zhao')
#     print(zhu.name,zhu.tno,zhu.sno,zhu.teacher)
# '''
#
#
# #方法重写 鸭子类型
#
# '''
# class person:
#     def __init__(self,name):
#         self.name = name
#     def printinfo(self):
#         print(self.name)
#
#
# class student(person):
#     def __init__(self,id,name):
#         self.id = id
#         self.name = name
#     def printinfo(self):
#         print(self.id+'+'+self.name)
#
# def printii(aa):
#     print('\n')
#     aa.printinfo()
#
# if __name__=='__main__':
#     p = person('zhao')
#     stu = student('111','li')
#     p.printinfo()
#     stu.printinfo()
#     printii(p)
#     printii(stu)
# '''
#
#  #super方法
#  # isinstance issubclass type
#  #类方法 静态方法
# '''
# class complex:
#     def __init__(self,real = 0,image=0):
#         self.real = real
#         self.image = image
#
#     @classmethod
#     def add(arg,c1,c2):
#         print(arg)
#         c = complex()
#         c.real = c1.real + c2.real
#         c.image = c1.image + c2.image
#         return c
#
#     @staticmethod
#     def add(c1,c2):
#         c = complex()
#         c.real = c1.real +c2.real
#         c.image = c1.image+c2.image
#         return c
#
# if __name__ == '__main__':
#     c1 = complex(1,2)
#     c2 = complex(3,4)
#     c = complex.add(c1,c2)
#     print(c)
#     print(c.real,c.image)
# '''
#
# #动态扩展类
#
# '''
# from types import MethodType
# class student:
#     pass
# def setname(self,name):
#     self.name = name
# def setsno(self,sno):
#     self.sno = sno
# if __name__=='__main__':
#     stu1 = student()
#     stu2 = student()
#     stu1.setname = MethodType(setname,stu1)
#     stu1.setname('lihua')
#     student.setsno=setsno
#     stu1.setsno('1111')
#     stu2.setsno('222')
#     print(stu1.name)
#     print(stu2.sno)
#     print(stu1.sno)
# '''
# #slots
#
# '''
# class person:
#     __slots__=('name')
# class student(person):
#     __slots__=('sno')
# class graduate(student):
#     pass
#
# stu = student()
# stu.name = 'zhao'
# print(stu.name)
# stu.sno = '111'
# print(stu.sno)
# pr = person()
# pr.name = 'aaa'
# print(pr.name)
# '''
#
# #@property
# #1
# '''
# class Student:
#     def __init__(self,name = 'unknown'):
#         self.name = name
#     def printinfo(self):
#         print(self.name)
# if __name__=='__main__':
#     stu1=Student()
#     stu2 = Student('Mary')
#     stu1.printinfo()
#     stu2.printinfo()
#     '''
#
# '''
# class Student:
#     def __init__(self,name):
#         self.name = name
#     def __del__(self):
#         print(self.name)
# if __name__=='__main__':
#     stu1=Student('li')
#     stu2=Student('xiao')
#     stu3=stu2
#     del stu2
#     del stu1
# '''
# #5
# '''
# class Time:
#     def __init__(self,h,m,s):
#         self.h = h
#         self.m = m
#         self.s = s
#     def __eq__(self,other):
#         return self.h==other.h and self.m==other.m and self.s==other.s
#     def __ne__(self,other):
#         return self.h!=other.h or self.m!=other.m or self.s!=other.s
#
# if __name__=='__main__':
#     t1=Time(1,2,3)
#     t2=Time(4,5,6)
#     t3=Time(7,8,9)
#     print(t1==t2)
#     print(t2!=t3)
# '''
#
# #6


# class a:
#     def display(self):
#         print('a', end = '')
#
#
# class b(a):
#     def display(self):
#         print('b', end='\n')
#         super().display()
#
#
# class c(b):
#     def display(self):
#         print('c', end='\n')
#         super().display()
#
#
# if __name__ == '__main__':
#     ss = c()
#     ss.display()

# #7
# '''
# class c:
#     @classmethod
#     def add(self,c1,c2):
#         return c1+c2
#     @staticmethod
#     def sub(a,b):
#         return a-b
# cc=c()
# print(cc.add(2,3))
# print(cc.sub(3,4))
# '''
# #9
# '''
# class A:
#     @property
#     def a(self):
#         return self._a
#     @a.setter
#     def a(self,a):
#         self._a = a
# st=A()
# st.a=48
# print(st.a)
# '''
# #8
# '''
# from types import MethodType
# class A:
#     def __init__(self,name):
#         self.name = name
# def func(n):
#     print(n.name)
#
# a = A(1)
# a.func = MethodType(func,a)
# a.func()
# '''
#
# #1
# '''
# import math
# class circle:
#     def setcenter(self,x,y):
#         self.x = x
#         self.y = y
#     def setradius(self,r):
#         self.r=r
#     def getarea(self,r):
#         return math.pi*r**2
#
# x = eval(input())
# y = eval(input())
# r = eval(input())
# c = circle()
# c.setcenter(x,y)
# c.getarea(r)
# print('center:(%.2f,%.2f),radius:%.2f'%(x,y,r))
# print('area:%.2f'%c.getarea(r))
# '''

#2
#
# import sys
# class Time:
#     def settime(self,h,m,s):
#         self.h=h
#         self.m=m
#         self.s=s
#         if self.h>23 or self.h<0 or self.m>59 or self.m<0 or self.s>59 or self.s<0:
#             print('error!')
#             sys.exit()
#     def addonesec(self):
#         self.s+=1
#         if self.s>=60:
#             self.s=0
#             self.m+=1
#         if self.m>=60:
#             self.h+=1
#             self.m=0
#         if self.h>=24:
#             self.h=0
#             self.m=0
#             self.s=0
# h = int(input())
# m = int(input())
# s = int(input())
# count = int(input())
# c = Time()
# c.settime(h,m,s)
# for i in range(count):
#     print('%02d:%02d:%02d'%(c.h,c.m,c.s))
#     c.addonesec()
#


#3

# import math
# class linder:
#     def __init__(self,r,h):
#         self.r = r
#         self.h = h
#     def getvolume(self):
#         return math.pi*h*r**2
#
# r = eval(input())
# h = eval(input())
# l = linder(r,h)
# print('r:%.2f,h:%.2f'%(l.r,l.h))
# print('volum:%.2f'%l.getvolume())

'''
单例模式是一个常用的软件设计模式，该模式的主要目的是确保某一个类只有一个实例存在。
比如说：利用加标签的白名单防止跨站脚本攻击XXS创建一个XxsFile类，不同的人访问都要创建XxsFile对象的实例，
这就导致系统中存在多个XxsFile的实例对象，而这样会严重浪费内存资源。事实上类似于XxsFile这样的类，
我们希望在程序运行期间只存在一个实例对象，在python中，我们可以使用单例。如下列几种方法:
在Python中new方法和init方法类似，但是如果两个都存在那么new先执行

__new__(cls, *args, **kwargs)

new()中的需要传递一个参数cls，cls表示需要实例化的类，此参数在实例化时由Python解析器自动提供
1、类方法classmethod
'''


# class Foo(object):
#     __instance = None
#
#     @classmethod
#     def instance(cls):
#         if cls.__instance:
#             return cls.__instance
#
#         else:
#             obj = cls()
#             cls.__instance = obj
#             return cls.__instance
#
#
# obj1=Foo.instance()
# obj2=Foo.instance()
# print(obj1,obj2)
'''
2、基于__new__方法实现(推荐使用、方便)

当我们实例化一个对象时，是先执行了类的__new__方法(当我们没写时，默认调用object.__new__),
实例化对象；然后再执行类的__init__方法，对这个对象进行初始化，所以我们可以基于这个，实现单例模式:
__new__方法：

使用MusicPlayer()创建对象时，python的解释器首先会调用new方法为对象分配空间，
如果不分配空间那么就不会调用初始化init，new是一个由object基类提供的内置的静态方法，主要作用有两个:

1、在内存空间中为对象分配空间

2、返回对象的引用
Python的解释器获取得到对象的引用后，将引用作为第一个参数，传递给__init__,

1、重写__new__方法python用return super().__new__(cls),否则Python的解释器得不到
分配了空间的对象引用，就不会调用对象的初始化方法，注意:__new__是一个静态方法，在调用时需要主动传递cls参数
'''
# class Foo:
#     __instance=None
#     def __init__(self):
#         print('create:',self)
#     def __new__(cls, *args, **kwargs):
#         print(cls)
#         if cls.__instance:
#             return cls.__instance
#         else:
#             obj = object.__new__(cls,*args,**kwargs)
#             cls.__instance = obj
#             return cls.__instance
# obj1=Foo()
# obj2=Foo()
# print(obj1,obj2)

#
# class MusicPlayer:
#     __instance = None
#     # 为对象分配内存空间
#
#     def __new__(cls, *args, **kwargs):
#         # 1、创建对象时,new方法会被自动调用
#         print("创建对象，分配内存空间")
#         if cls.__instance:
#             return cls.__instance
#         else:
#             # 2、为对象分配空间
#             cls.__instance = super().__new__(cls)
#             # 3、返回对象引用
#             return cls.__instance
#     # 对象初始化，定义实例属性
#
#     def __init__(self):
#         print("播放器初始化")
#
# # 创建播放器对象
# player = MusicPlayer()
# p2 = MusicPlayer()
# print(player)
# print(p2)


# # -*-coding:utf-8 -*-
# class MusicPlayer(object):
#
#     # 为对象分配内存空间
#     def __new__(cls, *args, **kwargs):
#         # 1、创建对象时,new方法会被自动调用
#         print("创建对象，分配内存空间")
#
#     # 对象初始化，定义实例属性
#     def __init__(self):
#         print("播放器初始化")
#
#
# # 创建播放器对象
# player = MusicPlayer()
# print(player)

# class A:
#     def __init__(self):
#         print('use A')
#     def pr(self):
#         print('pr A')
#
# class B(A):
#     def __init__(self):
#         print('use B')
#     def p(self):
#         super().pr()
#
# B().pr()
# A().pr()

# import math
#
#
# class Circle:
#     __radius = 0
#
#     def __init__(self, radius=0):
#         self.__radius = radius
#
#     def __del__(self):
#         print('yijieshu')
#     def setradius(self):
#         return self.__radius
#     def area(self):
#         aa = math.pi*self.__radius**2
#         return '%.2f'%aa
#     def __str__(self):
#         return 'mianji:'+str(self.__radius**2*math.pi)
#     def __gt__(self, other):
#         return self.area()> other.area()
#
#
# a = Circle(2)
# b = Circle(3)
# print(a.setradius())
# print(a.area())
# print(a)
# print(a>b)
# del a
# del b

# a = [[1,2,3],[4,5,6],[7,8,9]]
#
# for i in a:
#     for j in i:
#         print(j)
# import re
# t = '''sno:#1810101#,name:#李晓明#,age:#19#,major:#计算机#
# 3 sno:#1810102#,name:#马红#,age:#20#,major:#数学#'''
# a = re.findall(r'#([^#]*?)#', t, re.I)
# print(a)

# try:
#     print(4+2j>2-1j)
# except:
#     print('error')
# print('abc'>'xyz')
# try:
#     print((3,2)<('a','b'))
# except:
#     print('3333')
#
# print(3>2>2)

# class Solution:
#
#     def longest(self, s):
#         b = []
#         for i in range(len(s)):
#             for j in range(1, len(s)-i+1):
#                 a = s[i:j+i]
#                 if self.jug(a) == 1:
#                     b.append(a)
#         print(b)
#         return 0
#
#
#
#         # for i in range(len(c)):
#
#     def jug(self, s):
#         nn = len(s)
#         for i in range(nn):
#             if s[i] != s[nn - 1 - i]:
#                 return 0
#         else:
#             return 1
#
#
#
#
#
# if __name__ == '__main__':
#     a = Solution()
#     print(a.longest('aadasssffff'))
#     # print(a.jug('a'))
#     # print('s'.split())
from collections import deque
from queue import Queue
class Tree:
    def __init__(self, data):
        self.data = data
        self.lc = None
        self.rc = None

nn = locals()

for i in 'ABCDEFGH':
    nn[i.lower()] = Tree(i)


a.lc = b
a.rc = c
b.lc = d
b.rc = e
c.lc = f
c.rc = g
d.lc = h
def fir(tree):
    if tree:
        print(tree.data,end = ',')
        fir(tree.lc)
        fir(tree.rc)

def mid(tree):
    if tree:

        mid(tree.lc)
        print(tree.data, end=',')
        mid(tree.rc)

def lev(tree):
    queue1 = deque()
    queue1.append(tree)
    while len(queue1):
        node = queue1.popleft()
        print(node.data,end=',')
        if node.lc:
            queue1.append(node.lc)
        if node.rc:
            queue1.append(node.rc)
fir(a)
print('\n')
mid(a)
print('\n')
lev(a)

ss = Queue()
ss.put(1)
ss.put(2)
print(ss)