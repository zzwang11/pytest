# '''for break else 用法：
#     for i in range(5):
#         if i > 3:
#             break
#     else:
#         print('aaa')
#     当break不发生作用的时候，else才有作用'''
#


# #1
# '''
# def a(m,n):
#   if m%n==0:
#     return 1
#   else:
#     return 0
# b=1
# c=0
# list=[]
# while b:
#   b= int(input())
#   list.append(b)
# for i in list:
#   if a(i,3)==0:
#     c+=i
# print(c)
#    '''
#
# #2
# '''
# while True:
#   n = int(input('输入n \n'))
#   m=0
#   for i in range(1,n):
#     a = 2*i-1
#     m +=(-1)**(i-1)*(1/a)
#     i+=1
#   print('%.2f'%m)
#  '''
# #1
# '''
# def StudentInfo(name, country='China', chineselevel='A'):
#
#     print('%s,%s,%s'%(name,country,chineselevel))
#
# StudentInfo(country='America', chineselevel='B', name='John')
# '''
# #2
# '''
# def StudentInfo(name, *args):
#     print(name,args)
# StudentInfo('Li Xiaoming', 'China', 'A')
# '''
# #3
# '''
# def Sum(a,b,c):
#     print(a+b+c)
# t=(1,2,3)
# Sum(*t)
# '''
# #4
# '''
# def f1():
#     print(x)
#
# def f2():
#     global x
#     x=50
#     print(x)
#
# x=10
#
# f2()
#
# f1()
# '''
# #5
# '''
# def deco(func):
#     def inner(*args):
#         print('deco begin')
#         func(*args)
#         print('deco end')
#     return inner
# @deco
# def add(a,b):
#     print(a+b)
# if __name__=='__main__':
#     add(3,5)
# '''
# '''
# def outer(x):
#   y = 10
#   def inner(z):
#     global y
#     y = 20
#     return x+y+z
#   return inner
# f=outer(5)
# g=outer(50)
# print(f(20))
# print(g(20))
# '''
#
# '''
# def use_logging(func):
#   def _deco(*args,**kwargs):
#     print("%s is running" % func.__name__)
#     func(*args,**kwargs)
#   return _deco
# @use_logging
# def bar(a,b):
#   print('i am bar:%s'%(a+b))
# @use_logging
# def foo(a,b,c):
#   print('i am bar:%s'%(a+b+c))
# bar(1,2)
# foo(1,2,3)
# '''
# #闭包
# '''
# def my_func(*args):
#     fs = []
#     for i in range(3):
#         def func():
#           return i*i
#         fs.append(func())
#     return fs
#
# fs1,fs2,fs3= my_func()
#
# print(fs1)
# print(fs2)
# print(fs3)
# '''
# #装饰器
# '''
# def func_dec(func):
#      def wrapper(*args):
#          if len(args) == 2:
#             func(*args)
#          else:
#             print('Error! Arguments = %s'%list(args))
#      return wrapper
# @func_dec
# def add_sum(*args):
#      print(sum(args))
#
# # add_sum = func_dec(add_sum)
# args = range(1,4)
# add_sum(*args)
# '''
# '''
# def deco1(func):
#   def inner1(*args, **kwargs):
#     print('deco1 begin')
#     func(*args, **kwargs)
#     print('deco1 end')
#   return inner1
#
# def deco2(func):
#   def inner2(*args, **kwargs):
#     print('deco2 begin')
#     func(*args, **kwargs)
#     print('deco2 end')
#   return inner2
#
# # @deco1
# def f1(a,b):
#   print('a+b=',a+b)
#
# @deco1
# @deco2
# def f2(a,b,c):
#   print('a+b+c=',a+b+c)
#
# f1(3,5)
# f2(1,3,5)
# '''
# '''
# import functools
# def use_logging(func):
#   @functools.wraps(func)
#   def _deco(*args,**kwargs):
#     print("%s is running" % func.__name__)
#     func(*args,**kwargs)
#   return _deco
# @use_logging
# def bar():
#   print('i am bar')
#   print(bar.__name__)
# bar()
# '''
# '''
# import functools
# def use_logging(level):
#   def logging(func):
#     @functools.wraps(func)
#     def _deco(*args, **kwargs):
#       if level=='up':
#         print('%s is running!'%func.__name__)
#       return func(*args, **kwargs)
#     return _deco
#   return logging
#
# @use_logging(level='up')
# #@use_logging
# def bar(a,b):
#   print('i is wa%d:'%(a+b))
#   print(bar.__name__)
# bar(3,4)
# '''
#
# #6
# '''
# def sushu(n):
#   if n<=2:
#     print('invalid')
#   else:
#     m = int(n**0.5)
#     i = 2
#     while i <=m:
#         if n%i==0:
#           break
#         i+=1
#     if i>m:
#         print('yes')
#     else:
#         print('no')
#
# if __name__=='__main__':
#   i = 1
#   while i:
#     i = int(input('shuru:'))
#     sushu(i)
# '''
# #7
# '''
# def slist(a, b):
#
#   if len(a)<=len(b):
#     i=sslist(a,b)
#   else:
#     i= sslist(b,a)
#   if i==0:
#     print('no')
#
# def sslist(a,b):
#     i = 0
#     while i<=len(b):
#         if a !=b[:i]:
#             i+=1
#         else:
#             print(a)
#             break
#
#     if i>len(b):
#         m = 0
#     else:
#         m = 1
#     return m
#
# a = input()
# b = input()
# slist(a,b)
# '''
#
# #8
# '''
# def aa(n):
#   m = 1
#   if n>1:
#     m= aa(n-1)*n
#   else:
#     m=1
#   return m
#
# def c(i,n):
#   m = aa(n)/aa(i)
#   s = int(m/aa(n-i))
#   return s
#
#
# m = int(input())
# n = int(input())
# i = 1
# x=0
# if m>=1 and n >=1 and m<=n:
#   while i<=m:
#     x += c(i,n)
#     i+=1
#   print(x)
# else:
#   print('invalid')
# '''
#
# #9   异常处理的第一次使用 try
# '''
# def jug(a):
#     if type(a)==int:
#         return 1
#     else:
#         return 0
#
# m = input()
# n = input()
# try:
#     m = int(m)
# except ValueError:
#     pass
# try:
#     n =int(n)
# except ValueError:
#     pass
# if jug(m)==1 and jug(n)==1:
#     print(m-n)
# elif jug(m)==0 and jug(n)==0:
#     print(m+n)
# elif jug(m)^jug(n)==1:
#     print(m*n)
#
# '''
# #10
#
# def hano(n,a,b,c):
#     if n==1:
#         move(n,a,c)
#     else:
#         hano(n-1,a,c,b)
#         move(n,a,c)
#         hano(n-1,b,a,c)
# def move(n,a,b):
#     print('%d:%s---->%s'%(n,a,b))
#
# n = int(input('shuru:'))
# hano(n,'a','b','c')

# def outer(x):
#     y = 100
#
#     def inner(z):
#         return x*y+z
#     return inner
#
#
# f = outer(25)(5)
#
# print(f)


# def fibo(n):
#     if n > 2:
#         m = fibo(n-2)+fibo(n-1)
#         print(m)
#         return m
#     elif n == 1 or n == 2:
# #        print(1)
#         return 1
# fibo(5)
#

# a = [1,4,6,78,5]
# b = set(a)
# print(b)
# for i in b:
#     print(i)

# a = 355
# b = str(a)
# print(b)
# print(type(b))

# def t():
#     for i in range(4):
#         return i+5
# print(t())

# def return_test(n):
#     for i in range(n):
#         return 2*n
#
# print(return_test(3))
#
# for i in range(return_test(3)):
#     print(i)

# def yield_te(n):
#     for i in range(n):
#         yield i+4
#
# for i in yield_te(3):
#     print(i)
# print(77 or 0)
#
# print(11|44)
# print(222<<4)
# for i,j in enumerate(range(1,100,-2)):
#     print(i,j)
# aa = dict(aaa='aaa', bbb='bbbb', ccc='cccc')
# print(aa)
# def summ(**a):
#     for i in a.items():
#         print(i)
#
#
# a = dict(zip(['a','b','c','d'],[1,34,5,76]))
# summ(**a)
#
# summ(aa = 'aa',bb='bb')


import sys

n = int(sys.argv[1])
print(n)