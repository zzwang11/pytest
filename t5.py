# 列表复制


# import copy
# def pr(ls1,ls2):
#     print(ls1,ls2)
#     print(id(ls1[1]),id(ls2[1]))
#
# #ls1=[1,2,3]
#
# #ls2=ls1   赋值
# #ls2 = ls1[:] 截取
#
# ls1 = [1,[2,3]]
# ls2 = copy.deepcopy(ls1)
# #ls2 = ls1[:]
# pr(ls1,ls2)
# ls1[0]=5
# pr(ls1,ls2)
# ls1[1][1] = 5
# pr(ls1,ls2)
#
#
# # 列表中元素排列
# '''
# class stu:
#     def __init__(self,sno,name):
#         self.sno = sno
#         self.name = name
#     def __str__(self):
#         return '学号：'+self.sno+'姓名：'+self.name
#
# ls = [stu('111','zha'),stu('222','qian'),stu('333','sun'),stu('444','li')]
# for i in ls:
#     print(i)
# ls.sort(key =lambda st:st.sno)
# for i in ls:
#     print(i)
# ls.sort(key = lambda st:st.sno, reverse = True)
# for i in ls:
#     print(i)
# '''
#
# '''
# d = dict(sno=None,name = '44',grade='3')
# for i in d:
#     print(i,end = ' ')
#     print(d[i])
# print(d.keys())
# for i in d.keys():
#     print(i)
# print(d.values())
# print(d.items())
# for i in d.items():
#     print(i)
# '''
# # 生成器
# '''
# g = (x**3 for x in range(10))
# print(type(g))
# print(g)
# for i in g:
#     print(i)
# '''
# # generator
#
# '''
# def xx(n):
#     r = 1
#     for i in range(2,n+1):
#         yield r
#         r *= i
# print(xx(10))
# for n in xx(20):
#     print(n)
# '''
# 1
# a = []
# m = int(input('object:'))
# n = int(input('no:'))
# i = 0
# while i < n:
#     b = int(input())
#     a.append(b)
#     i += 1
#
# print(a)
# b = 0
# c = []
#
#
# def ind(x, y):
#     try:
#         s = x.index(y)
#     except ValueError:
#         s = len(x)
#     return s
#
#
# while b < n:
#     ll = ind(a[b:], m)
#     b += ll
#     if b >= n:
#         break
#     c.append(b)
#     b = b+1
# print(c)

# 2
# import copy
# a = [[1, 2, 3], 'a']
# b = copy.deepcopy(a)
# a[0][0] = 5
# print(a)
# print(b)

# 3
# class A:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#
# if __name__ == '__main__':
#     ls = [A(10, 20), A(30, 15), A(20, 10)]
#     ls.sort(key=lambda c: c.a, reverse=True)
#     for x in ls:
#         print('a:%d, b:%d'%(x.a,x.b))

# 3
# a = set([1, 2, 3, 4])
# # a.update((5, 6))
# # print(5 in a)
# # a.add((5, 6))
# # print((5, 6) in a)

# 4
# def su(m):
#     for i in range(2, m+1):
#         n = int(i**0.5)
#         for j in range(2, n+1):
#             if i % j == 0:
#                 break
#         else:
#             yield i
#
#
# s = eval(input())
# for x in su(s):
#     print(x, end=' ')

# 5
#
# class seq:
#     def __init__(self, beg, step):
#         self.val = beg
#         self.step = step
#
#     def __next__(self):
#         old_val = self.val
#         self.val += self.step
#         return old_val
#
#     def __iter__(self):
#         return self
#
# s = seq(3,5)
# for i in range(5):
#     print(next(s), end=' ')

# 6


# def ex(b, m):
#     x = b[m:].index(max(b[m:]))
#     if x != 0:
#         y = b[m]
#         b[m] = max(b[m:])
#         b[x+m] = y
#     print(b)
#
#
# n = int(input())
# i = 0
# a = []
# x = 0
# while i < n:
#     a.append(int(input()))
#     i += 1
#
# print(a)
#
# for x in range(n-1):
#     ex(a, x)
# # while x < n-1:
# #     ex(a, x)
# #     x += 1

# 7

# def is_mag(ls):
#
#     a, b, c, d = 0, 0, 0, 0
#     n = []
#     for i in range(len(ls)):
#         for j in range(len(ls)):
#             n.append(ls[i][j])
#     if len(set(n)) == len(n):
#         a = 1
#
#     n = []
#     for i in range(len(ls)):
#         x = 0
#         for j in range(len(ls)):
#             x += ls[i][j]
#         n.append(x)
#     if len(set(n)) == 1:
#         b = 1
#
#     n = []
#     for i in range(len(ls)):
#         x = 0
#         for j in range(len(ls)):
#             x += ls[j][i]
#         n.append(x)
#     if len(set(n)) == 1:
#         c = 1
#
#     x = 0
#     y = 0
#     i = 0
#     while i < len(ls):
#         x += ls[i][i]
#         y += ls[i][len(ls)-i-1]
#         i += 1
#     if x == y:
#         d = 1
#
#     if a == 1 and b == 1 and c == 1 and d == 1:
#         return True
#     else:
#         return False
#
#
# n = eval(input())
# ls1 = []
# for xx in range(n):
#     ls1.append(list(eval(input())))
#
# print(ls1)
#
# if is_mag(ls1):
#     print('zzzzz')
# else:
#     print('xxxxx')

# 8

# def fun(d):
#     m = input()
#     n = input()
#     d.update({n: m})
#     print(d)


# def che(d, x):
#     m = input()
#     x.append(d.get(m, 'notfound'))
#     print(x)


# dic = {}
# a = int(input('字典:'))
# for i in range(a):
#     fun(dic)
# print(dic)

# x = []
# b = int(input('查询个数：'))
# for i in range(b):
#     che(dic, x)

# for i in x:
#     print(i)



# import redis

# pool = redis.ConnectionPool(host='localhost', port='6379',decode_responses=True)

# r = redis.StrictRedis(host='localhost', port='6379',decode_responses=True)
# r.set('nn','mm')
# r.set('foo', 'bar')
# print(r.get('foo'))
# print(r['foo'])
# print(type(r['foo']))
# print(r.keys())
# r.delete('mymy')


from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello():
    return 'hellohelli'

if __name__ == "__main__":
    app.run()
