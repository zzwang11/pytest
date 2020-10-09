# '''
# while True:
#   n = int(input('输入n \n'))
#   m=0
#   i=1
#   while i<=n:
#     a = 2*i-1
#     m +=(-1)**(i-1)*(1/a)
#     i+=1
#   print('%.2f'%m)
# '''
# #1
# '''1111
# val = eval(input())
# if val<0:
#   val*=-1
# print(val)
# '''
# #2222
# '''
# while True:
#   n = eval(input())
#   m,a = 1,0
#   while m<=n:
#     a+=m
#     m+=1
#   print('和是%d'%a)
# '''
# # 333
# '''while True:
#   n = int(input('输入一个整数：'))
#   a,m = 1,1
#   while m<=n:
#     a*=m
#     m+=1
#   print(a)
#   '''
#
# #4
# '''while True:
#   n = int(input('输入年份：'))
#   if n%400 ==0:
#     print('no')
#   elif n%4==0:
#       print('yes')
#   else:
#       print('no')
# '''
# #5
# '''
# while True:
#   x = eval(input('输入：'))
#   if 1<x <=2:
#     m = x+2.5
#     print(m)
#   elif -1<=x<=1:
#     m = x*4.35
#     print(m)
#   else:
#     print('invalid')
#   '''
# #6
# '''
# while True:
#   x = int(input('input:'))
#   if 90<= x <=100:
#     print('A')
#   elif 80<=x<89:
#     print('B')
#   elif 70<=x<=79:
#     print('C')
#   elif 60<=x<=69:
#     print('D')
#   elif 0<=x<=59:
#     print('E')
#   else:
#     print('invalid')
#  '''
# #7
# '''
# def d(n):
#   if n>0:
#     m = d(n-1)+c(n)
#   if n ==0:
#     m = 1
#   return m
# def c(n):
#   if n>0:
#     m = c(n-1)*n
#   if n == 0:
#     m = 1
#   return m
#
# while True:
#   n = int(input('input'))
#   print(c(n))
#   print(d(n))
#   '''
# #8 忘清零了，浪费很长时间\
# '''
#
# while True:
#   x = int(input('input:'))
#   a,b,c = 0,0,0
#   i = 0
#   while 0<=a<=x/10:
#     b=0
#     while 0<=b<=(x-a*10)/5:
#       c=x-a*10-b*5
#       if c<0:
#         break
#       print('%d,%d,%d'%(a,b,c))
#       i+=1
#       b+=1
#     a +=1
#   print('total %d kinds'%i)
#     '''
# #9
# '''
# while True:
#   a = int(input('a:'))
#   b = int(input('b:'))
#   if a>999 or a<100 or b>999 or b<100:
#     print('error')
#   else:
#     for i in range(a,b+1):
#       x = int(i/100)
#       y = int((i-x*100)/10)
#       z = int(i-x*100-y*10)
#       if i == x**3+y**3+z**3:
#         print(i)
#  '''
# 10
# while True:
#     n = int(input('int:'))
#     z = 0
#     for x in range(2, n+1):
#         i = 2
#         m = int(x**0.5)
#         while i <= m:
#             if x % i == 0:
#                 break
#             i += 1
#         if i > m:
#             print(x)
#             z += 1
#     print('total %d' % z)
#

# def ree(a):
#     a.remove('a')
#
#
#
# a = 'tianshiaaa'
# b = list(a)
# c = 19
# print(b)
# ree(b)
# ree(b)
# print(b)
# print(''.join(b))


# def exx():
#     return [lambda x:x*i for i in range(3)]
#
# for i in exx():
#     print(i(3))


# a = (lambda x:x+i for i in range(4))
# for i in a:
#     print(i(4))

# s = "this is\na\ttest"
# print(' '.join(s.split()))

# a = (lambda s: " ".join(s.split()))("this is\na\ttest")
# print(a)

# class Exa:
#     name = 'unknown'
#     __id = 'unknown'
#
#     def setinfo(self,name,nid):
#         self.name = name
#         self.__id = nid
#
#     def printinfo(self):
#         print('姓名：%s，身份证号码：%d'%(self.name,self.__id))
#
#
# if __name__ == '__main__':
#     ee = Exa()
#     ee.setinfo('王安', 4222222)
#     ee.printinfo()
#     print(ee._Exa__id)

#
# a = eval('23566/22')
# print(a)

a = {'one': 1, 'two': 2, 'three': 3}
b = dict(one=1, two=2, three=3)
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
print(a)
print(b)
print(c)
