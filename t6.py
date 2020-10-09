# # 3
# str1 = '  it\'s a book!  '
# str2 = 'python##java##c++##php'
# # ls1 = str1.split()
# ls4 = str2.split('##')
# # print(ls1)
# # print(ls2)
# print(str1)
# print('!'.join(ls4))
# # 4
# ls = str2.replace('##', ' ')
# ls1 = str2.find('##j')
# ls2 = str1.lower()
# ls3 = str1.upper()
# print(ls)
# print(ls1)
# print(ls2)
# print(ls3)
# print(ls4)

# 字符串
# 正则表达式
#
# import re
# import requests
#
#
# class NankaiNewsCrawler:  # 定义NankaiNewsCrawler类
#     headersParameters = {  # 发送HTTP请求时的HEAD信息
#         'Connection': 'Keep-Alive',
#         'Accept': 'text/html, application/xhtml+xml, */*',
#         'Accept-Language':
#             'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
#         'Accept-Encoding': 'gzip, deflate',
#         'User-Agent':
#             'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'
#     }
#     '''
#     headersParameters中保存了请求头的信息，如：
#     headersParameters = { #发送HTTP请求时的HEAD信息
#         'Connection': 'Keep-Alive',
#             # Connection决定当前的事务完成后，是否会关闭网络连接。如果该值是“Keep-Alive”，网络连接就是持久
#         'Accept': 'text/html, application/xhtml+xml, */*',
#             #浏览器接收的媒体类型，text/html代表HTML格式，application/xhtml+xml代表XHTML格式，*/* 代表浏览器可以处理所有类型
#         'Accept-Language':     'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
#             #浏览器申明自己接收的语言
#         'Accept-Encoding': 'gzip, deflate',
#             #浏览器申明自己接收的编码方式：通常指定压缩、是否支持压缩、支持什么方式压缩（gzip/default）
#         'User-Agent': 'Mozilla/6.1 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
#             #告诉HTTP服务器客户端浏览器使用的操作系统和浏览器的版本和名称
#     }
#     '''
#
#     def __init__(self, timeout):  # 定义构造方法
#         self.url = 'http://edu.people.com.cn/n1/2018/0905/c367001-30274290.html'
#         self.timeout = timeout  # 连接超时时间设置（单位：秒）
#         self.titles = []
#
#     def GetHtml(self):  # 定义GetHtml方法
#         request = requests.get(self.url, timeout=self.timeout, headers=self.headersParameters)  # 根据指定网址爬取网页
#         request.encoding = 'GBK'
#         print(request.text)
#         self.html = request.text  # 获取新闻网页内容
#
#
#     def GetTitles(self):  # 定义GetTitles方法
#         titles = re.findall(r'<p style="text-indent: 2em;">([^<]*?)</p>', self.html)  # 匹配新闻标题
#         for i in range(len(titles)):  # 对于每一个标题
#             temp = re.sub(r'<[^>]+>', '', titles[i])  # 去除所有HTML标记，即<...>
#             # temp = re.sub('{[\s\S]*?}', '', temp)
#             print(temp)
#             if len(temp) < 3:
#                 continue
#             self.titles.append(temp.strip())  # 将标题两边的空白符去掉
#
#     def PrintTitles(self):  # 定义PrintTitle方法
#         no = 1
#         for title in self.titles:  # 显示标题
#             print(str(no) + ':' + title)
#             no += 1
#
#     def ExportToFile(self, filepath):  # 定义ExportToFile方法，将标题输出到文件中
#         with open(filepath, 'w', encoding='utf-8') as f:
#             no = 1
#             for title in self.titles:
#                 f.write(str(no) + ':' + title + '\n')
#                 no += 1
#
#     def GetTitlesNum(self):  # 定义GetTitlesNum方法，返回已获取的新闻标题数
#         return len(self.titles)
#
#
# if __name__ == '__main__':
#     bnc = NankaiNewsCrawler(30)  # 创建NankaiNewsCrawler类对象
#     bnc.GetHtml()  # 获取新闻网页的内容
#     bnc.GetTitles()  # 获取新闻标题
#     # bnc.PrintTitles()  # 显示新闻标题
#     bnc.ExportToFile('newstitlelist1.txt')  # 将新闻标题保存到文件中

#
# import re
# import requests
# from urllib.parse import quote  # 导入quote方法对URL中的字符进行编码
# from bs4 import BeautifulSoup  # 导入BeautifulSoup
#
#
# class NankaiNewsCrawler:  # 定义NankaiNewsCrawler类
#     headersParameters = {  # 发送HTTP请求时的HEAD信息
#         'Connection': 'Keep-Alive',
#         'Accept': 'text/html, application/xhtml+xml, */*',
#         'Accept-Language':
#             'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
#         'Accept-Encoding': 'gzip, deflate',
#         'User-Agent':
#             'Mozilla/6.1 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
#     }
#     '''
#     headersParameters中保存了请求头的信息，如：
#     headersParameters = { #发送HTTP请求时的HEAD信息
#         'Connection': 'Keep-Alive',
#             # Connection决定当前的事务完成后，是否会关闭网络连接。如果该值是“Keep-Alive”，网络连接就是持久
#         'Accept': 'text/html, application/xhtml+xml, */*',
#             #浏览器接收的媒体类型，text/html代表HTML格式，application/xhtml+xml代表XHTML格式，*/* 代表浏览器可以处理所有类型
#         'Accept-Language':     'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
#             #浏览器申明自己接收的语言
#         'Accept-Encoding': 'gzip, deflate',
#             #浏览器申明自己接收的编码方式：通常指定压缩、是否支持压缩、支持什么方式压缩（gzip/default）
#         'User-Agent': 'Mozilla/6.1 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
#             #告诉HTTP服务器客户端浏览器使用的操作系统和浏览器的版本和名称
#     }
#     '''
#
#     def __init__(self, timeout):  # 定义构造方法
#         self.url = 'http://news.nankai.edu.cn/ywsd/index.shtml'
#         self.timeout = timeout  # 连接超时时间设置（单位：秒）
#         self.titles = []
#
#     def GetHtml(self):  # 定义GetHtml方法
#         request = requests.get(self.url, timeout=self.timeout, headers=self.headersParameters)  # 根据指定网址爬取网页
#         request.encoding = 'utf-8'
#         self.html = request.text  # 获取新闻网页内容
#
#     def GetTitles(self):  # 定义GetTitles方法
#         bs = BeautifulSoup(self.html, 'html.parser')
#         titles = bs.find_all('div', {'align': 'left'})  # 查找align属性为left的所有div
#         for i in range(len(titles)):  # 对于每一个标题
#             self.titles.append(titles[i].string)
#
#     def PrintTitles(self):  # 定义PrintTitle方法
#         no = 1
#         for title in self.titles:  # 显示标题
#             print(str(no) + ':' + title)
#             no += 1
#
#     def ExportToFile(self, filepath):  # 定义ExportToFile方法，将标题输出到文件中
#         with open(filepath, 'w', encoding='utf-8') as f:
#             no = 1
#             for title in self.titles:
#                 f.write(str(no) + ':' + title + '\n')
#                 no += 1
#
#     def GetTitlesNum(self):  # 定义GetTitlesNum方法，返回已获取的新闻标题数
#         return len(self.titles)
#
#
# if __name__ == '__main__':
#     bnc = NankaiNewsCrawler(30)  # 创建NankaiNewsCrawler类对象
#     bnc.GetHtml()  # 获取新闻网页的内容
#     bnc.GetTitles()  # 获取新闻标题
#     bnc.PrintTitles()  # 显示新闻标题
#     bnc.ExportToFile('newstitlelist.txt')  # 将新闻标题保存到文件中
#
# import re
# import requests
# from urllib.parse import quote  # 导入quote方法对URL中的字符进行编码
# from bs4 import BeautifulSoup  # 导入BeautifulSoup
#
#
# class NankaiNewsCrawler:  # 定义NankaiNewsCrawler类
#     headersParameters = {  # 发送HTTP请求时的HEAD信息
#         'Connection': 'Keep-Alive',
#         'Accept': 'text/html, application/xhtml+xml, */*',
#         'Accept-Language':
#             'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
#         'Accept-Encoding': 'gzip, deflate',
#         'User-Agent':
#             'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'
#     }
#     '''
#     headersParameters中保存了请求头的信息，如：
#     headersParameters = { #发送HTTP请求时的HEAD信息
#         'Connection': 'Keep-Alive',
#             # Connection决定当前的事务完成后，是否会关闭网络连接。如果该值是“Keep-Alive”，网络连接就是持久
#         'Accept': 'text/html, application/xhtml+xml, */*',
#             #浏览器接收的媒体类型，text/html代表HTML格式，application/xhtml+xml代表XHTML格式，*/* 代表浏览器可以处理所有类型
#         'Accept-Language':     'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
#             #浏览器申明自己接收的语言
#         'Accept-Encoding': 'gzip, deflate',
#             #浏览器申明自己接收的编码方式：通常指定压缩、是否支持压缩、支持什么方式压缩（gzip/default）
#         'User-Agent': 'Mozilla/6.1 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
#             #告诉HTTP服务器客户端浏览器使用的操作系统和浏览器的版本和名称
#     }
#     '''
#
#     def __init__(self, timeout):  # 定义构造方法
#         self.url = 'http://news.nankai.edu.cn/nkrw/index.shtml'
#         self.timeout = timeout  # 连接超时时间设置（单位：秒）
#         self.titles = []
#
#     def GetHtml(self):  # 定义GetHtml方法
#         request = requests.get(self.url, timeout=self.timeout, headers=self.headersParameters)  # 根据指定网址爬取网页
#         request.encoding = 'utf-8'
#         self.html = request.text  # 获取新闻网页内容
#
#     def GetTitles(self):  # 定义GetTitles方法
#         bs = BeautifulSoup(self.html, 'html.parser')
#         titles = bs.find_all('div', {'align': 'left'})  # 查找align属性为left的所有div
#         for i in range(len(titles)):  # 对于每一个标题
#             self.titles.append(titles[i].string)
#
#     def PrintTitles(self):  # 定义PrintTitle方法
#         no = 1
#         for title in self.titles:  # 显示标题
#             print(str(no) + ':' + title)
#             no += 1
#
#     def ExportToFile(self, filepath):  # 定义ExportToFile方法，将标题输出到文件中
#         with open(filepath, 'w', encoding='utf-8') as f:
#             no = 1
#             for title in self.titles:
#                 f.write(str(no) + ':' + title + '\n')
#                 no += 1
#
#     def GetTitlesNum(self):  # 定义GetTitlesNum方法，返回已获取的新闻标题数
#         return len(self.titles)
#
#
# if __name__ == '__main__':
#     bnc = NankaiNewsCrawler(30)  # 创建NankaiNewsCrawler类对象
#     bnc.GetHtml()  # 获取新闻网页的内容
#     bnc.GetTitles()  # 获取新闻标题
#     bnc.PrintTitles()  # 显示新闻标题
#     bnc.ExportToFile('newstitlelist.txt')  # 将新闻标题保存到文件中


# a = input()
# ls = ''
# for i in a:
#     if 'A' <= i <= 'Z':
#         ls += i.lower()
#     elif 'a' <= i <= 'z':
#         ls += i.upper()
#     else:
#         ls += i
# print(ls)


# import threading
# import time
#
#
# def run(n):
#     print(n,'start')
#     time.sleep(1)
#     print('s2',n)
#     time.sleep(1)
#     print('s1',n)
#     time.sleep(1)
#     print('s0',n)
#
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=run,args=('t1',))
#     t2 = threading.Thread(target=run,args=('t2',))
#     t1.start()
#     t2.start()

# import threading
# import time
# from datetime import datetime
#
#
# def print_time():
#     for _ in range(5):
#         time.sleep(1)
#         print('current thread is %s, print end time is %s'\
#               %(threading.current_thread().getName(), datetime.today()))
#
#
# thr = [threading.Thread(name='t%s'%(i,),target=print_time) for i in range(5)]
#
# [t.start() for t in thr]


# import time
#
# print(time.time())
# print(time.ctime())
# print(time.localtime())
# print(time.timezone)
# print(time.strftime('%Y-%m-%d-%H-%M-%S---%w-%A---%Z',time.localtime()))

# import threading
# import time
#
# exitflag = 0
#
#
# class MyThread(threading.Thread):
#     def __init__(self, name, id, counter):
#         super().__init__()
#         self.name = name
#         self.id = id
#         self.counter = counter
#
#     def run(self):
#         print('thread start'+self.name)
#         printtime(self.name, self.counter, 5)
#         print('thread over'+self.name)
#
#
# def printtime(sname, delay, counter):
#     while counter:
#         # if exitflag:
#         #     sname.exit()
#         time.sleep(delay)
#         print('%s:-------%s' % (sname, time.localtime(time.time())))
#         counter -= 1
#
#
# if __name__ == '__main__':
#     t1 = MyThread('th1', 1, 1)
#     t2 = MyThread('th2', 2, 2)
#
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     print('exittttt')

# import threading
# import time
#
# ls = [0,0,0,0,0,0,0]
#
#
# def printll(n):
#     time.sleep(0.5)
#     print(n)
#
#
# def sett(n):
#     i = 7
#     while i >= 0:
#         n[i-1] = 1
#         time.sleep(0.1)
#         i -= 1
#
#
# Lock = threading.RLock()
# t1 = threading.Thread(target=printll,args=(ls,))
# t2 = threading.Thread(target=sett,args=(ls,))
#
#
# t2.start()
# t1.start()
# t2.join()
# t1.join()
# print(ls)

# import threading
# import time
#
# exitflag = 0
#
#
# class MyThread(threading.Thread):
#     def __init__(self, name, a_id, delay):
#         super().__init__()
#         self.name = name
#         self.id = a_id
#         self.delay = delay
#
#     def run(self):
#         print('thread start:'+self.name)
#         # lock.acquire()
#         printtime(self.name, self.delay, 5)
#         # lock.release()
#         print('thread over:'+self.name)
#
#
# def printtime(sname, delay, counter):
#     while counter:
#         # if exitflag:
#         #     sname.exit()
#         time.sleep(delay)
#         print('%s:%s' % (sname, time.ctime(time.time())))
#         counter -= 1
#
#
# if __name__ == '__main__':
#     lock = threading.RLock()
#     ls = []
#     t1 = MyThread('th1', 1, 1)
#     t2 = MyThread('th2', 2, 2)
#     t2.start()
#     t1.start()
#
#     # ls.append(t1)
#     # ls.append(t2)
#     # for i in ls:
#     #     i.join()
#     t1.join()
#     t2.join()
#     print('exittttt')

# import queue
# import threading
# import time
# flag = 0
#
#
# class MyThread(threading.Thread):
#     def __init__(self, sid, name, q):
#         super().__init__()
#         self.name = name
#         self.q = q
#         self.id = sid
#
#     def run(self):
#         print('thread start:',self.name)
#         process(self.name,self.q)
#         print('thread stop:',self.name)
#
#
# def process(name, q):
#     while not flag:
#         queuelock.acquire()
#         if not workqueue.empty():
#             data = q.get()
#             queuelock.release()
#             print('%s process:%s' % (name, data))
#         else:
#             queuelock.release()
#         time.sleep(2)
#
#
# threadlist = ['thread1', 'thread2', 'thread3']
# namelist = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
# workqueue = queue.Queue(10)
# queuelock = threading.Lock()
# threads = []
# thid = 1
#
#
# for tname in threadlist:
#     thread = MyThread(thid, tname, workqueue)
#     thread.start()
#     threads.append(thread)
#     thid += 1
#
# queuelock.acquire()
# for word in namelist:
#     workqueue.put(word)
# queuelock.release()
#
# while not workqueue.empty():
#     pass
#
# flag = 1
# for t in threads:
#     t.join()
#
# print('over')

# import threading
# import time
#
# event = threading.Event()
#
#
# def lighter():
#     count = 0
#     event.set()     # 初始值为绿灯
#     while True:
#         if 5 < count <= 10:
#             event.clear()  # 红灯，清除标志位
#             print("\33[41;1mred light is on...\033[0m")
#         elif count > 10:
#             event.set()  # 绿灯，设置标志位
#             count = 0
#         else:
#             print("\33[42;1mgreen light is on...\033[0m")
#
#         time.sleep(1)
#         count += 1
#
#
# def car(name):
#     while True:
#         if event.is_set():      # 判断是否设置了标志位
#             print("[%s] running..." % name)
#             time.sleep(1)
#         else:
#             print("[%s] sees red light,waiting..." % name)
#             event.wait()
#             print("[%s] green light is on,start going..." % name)
#
#
# light = threading.Thread(target=lighter)
# light.start()
#
# car = threading.Thread(target=car, args=("MINI",))
# car.start()

# import threading
# import time
# x = 0
#
#
# def run():
#     global x
#     x += 10
#     print('%s number is: %d' % (threading.current_thread().getName(), x))
#
#
# m = [threading.Thread(target=run) for i in range(10)]
#
# for i in m:
#     i.start()

# import threading
# import time
# x = 0
# lock = threading.Lock()
#
# def run(n):
#     global x
#     lock.acquire()
#     w = x + 1
#     time.sleep(0.1)
#     print('%s number is: %d' % (threading.current_thread().getName(), w))
#     x = w
#     lock.release()
#
#
# m = [threading.Thread(target=run,args=(i,)) for i in range(10)]
#
# for i in m:
#     i.start()
#
# for i in m:
#     i.join()
#
# print(x)

# a = [1,2,3,3,3,5]
#
# b = [_ for _ in a]
# #
# c = dict(zip(range(len(a)), a))
# # print(c)
# d = [v for k,v in c.items() if v == 3]
# print(d)
# # print(type(c.keys()))
# # print(c.keys())
#
# # b = [a,5,[1,2]]
# # print(b[0.2])
# # b = (x for x in a if a.counter(x)>0)
# print(b)



# def sortc(a):
#     c = []
#     for i in range(len(a)):
#         if a[i] == 'A':
#             a[i] = 1
#         elif a[i] == 'J':
#             a[i] = 11
#         elif a[i] == 'Q':
#             a[i] = 12
#         elif a[i] == 'K':
#             a[i] = 13
#     for i in range(len(a)):
#         if a[i] == 'BJ' or a[i] == 'SJ':
#             c[i] = 0
#         else:
#             c[i] = a[i]
#     b = c.sorted()
#
#     if 0 not in b:
#         if b == [i for i in range(b[0], b[0]+5)]:
#             return 0
#         else:
#             return 1
#     else:
#         d = b.count(0)
#         e = b[d:]
#         f = [i for i in range(e[0], e[0]+5)]
#         i = 0
#         j = 0
#         for i in range(len(b)):
#             if f[i] in e:
#                 j += 1
#         if (5-j) == d:
#             return 0
#         else:
#             return 1
#
# sortc([5,6,7,8,9])
# '''
# select * from A where id = max(id);
#
# select * from A where id =(select min(id) from (select distinct top 2 id from A order by id desc));
# '''



import sys
import re


# n = input()
# t = input()
# a = 0
# b = 0
# i = 0

#
# def exists(a):
#     pos = 0
#     pos1 = 0
#     i = 0
#     for ch in a:
#         i += 1
#         if ch == 'M':
#             pos += 1
#         if ch == 'T':
#             pos1 += 1
#             j = i
#         if pos1 >= 1:
#             if
#             return j
#

t = 'MassddTdTsdfadfMaT'
# a = exists(t)
# b = t[a:]
#
# c = b.index('M')
#
# a = exists(t)
# b = t[a:]
# c = b.rfind('M')
# if b.endswith('T') and c > 0 and a>1:
#     e = a+c
#     d = t[a:e]
#     sys.stdout.write(d)
# else:
#     sys.stdout.write('None')
# x = input()
# x = x.split()
# m = int(x[0])
# n = int(x[1])

# a = input()
# a = a.split()
# b = []
# c = []
# d = 0
# for i in a:
#     b.append(int(i))
# del a
#
# def sun(s):
#     for i in range(len(s)-1):
#         if s[i] <= s[i+1]:
#             continue
#         else:
#             return 0
#     return 1
#
#
# for l in range(1,m+1):
#     for r in range(l,m+1):
#         c = []
#         for k in b:
#             if 0<k<l or r<k<m+1:
#                 c.append(k)
#         if sun(c) == 1:
#             d += 1
#
# sys.stdout.write(d)


# for i in range(5,0,-1):
#     print(i)
# a = [1,2,4]
# a.pop()
#
# print(a)

# class Solution:
#     def shortestPalindrome(self, s: str) -> str:
#         n = len(s)
#         m = n//2
#         for i in range(m+1,-1,-1):
#             a = s[i:]
#             b = s[:i]
#             if b.startswith(a[::-1])):
#                 return


