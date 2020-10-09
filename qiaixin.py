# # import sys
# # if __name__ == "__main__":
# #     # 读取第一行的n
# #     x = sys.stdin.readline().strip()
# #     try:
# #         n = int(x)
# #         if n <= 0 or n >36:
# #             m = 0
# #         elif n == 1 or n == 2:
# #             m = n
# #         else:
# #             a = 1
# #             b = 2
# #             m = 0
# #             for i in range(2, n):
# #                 m = a + b
# #                 a = b
# #                 b = m
# #     except:
# #         m = 0
# #     print(m)
# 
# 
# 
# class Solution:
#     def house(self , person ):
#         n = len(person)
#         l = [1]*n
#         a = 0
#         for i in range(1, n-1):
#             if person[i - 1] > person[i] < person[i + 1]:
#                 l[i] = 1
#         if person[0]<person[1]:
#             l[0] = 1
#         if person[n-1]<person[n-2]:
#             l[n-1] = 1
#         for i in range(n-1):
#             while person[i]<person[i+1] and l[i]>=l[i+1]:
#                 l[i+1] += 1
#         for i in range(n-1,0,-1):
#             while person[i]<person[i-1] and l[i]>=l[i-1]:
#                 l[i-1] += 1
#         for i in l:
#             a += i
#         return a
# 
# 
# 
# 
# a = Solution()
# print(a.house([1,2,3,4,5,6,5,6,5,5,5,7,9]))


# class Solution:
#     def LRU(self, operators, k):
#         # write code here
#         a = {}
#         b = []
#         c = []
#         if operators:
#             for i in operators:
#                 if i[0] == 1:
#                     key = str(i[1])
#                     val = i[2]
#                     a[key] = val
#                     c.append(key)
#                     if len(c) > k:
#                         d = c.pop(0)
#                         a.pop(d)
#                 if i[0] == 2:
#                     key = str(i[1])
#                     gval = a.get(key, -1)
#                     b.append(gval)
#                     if gval != -1:
#                         e = c.index(key)
#                         del c[e]
#                         c.append(key)
#
#         return b
#
# a = Solution()
# print(a.LRU([[1,1,1],[1,2,2],[1,3,2],[2,1],[1,4,4],[2,2]],3))
# class Node:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
#
#
# # class Solution:
# #     # 返回ListNode
# def ReverseList(pHead):
#     n = pHead
#     if n is None or n.next is None:
#         return n
#     p = None
#     a = None
#     while n:
#         a = n.next
#         n.next = p
#         p = n
#         n = a
#     return p
#
#
# if __name__ == '__main__':
#     a = Node(3)
#     a.next = Node(4)
#     a.next.next = Node(5)
#     a.next.next.next = Node(6)
#     # b = Solution()
#     c = ReverseList(a)
#     while c:
#         print(c.val)
#         c = c.next0



# 小度新买了一个机器人玩具。我们可以把这个机器人放到一个二维坐标上，它的初始位置为（x0,y0）。
# 然后给出一串指令，指令包含四个字符U、D、L和R，分别表示上、下、左、右。
# 每遇到一个指令字符，机器人将朝相应的方向移动一格。请输出机器人的最后位置。


# 单组输入，输入两行。
#
# 第一行两个整数表示起始位置x0和y0，两个整数之间用空格隔开。（起始坐标在±10000以内）
#
# 第二行一个字符串表示指令集（指令集长度不超过10000）。

# 输出两个整数，表示机器人的最终位置坐标，两个整数之间用空格隔开。


# def suan(s,x_,y_):
#     if s == 'L':
#         x_ -= 1
#     elif s == 'R':
#         x_ += 1
#     elif s == 'U':
#         y_ += 1
#     elif s == 'D':
#         y_ -= 1
#     return x_, y_
#
#
# a = input()
# a = a.split()
# x = int(a[0])
# y = int(a[1])
# b = input()
# for i in b:
#     x, y = suan(i,x,y)
#
# print(x,y)

# print(suan('L',3,5))

# 李华顺利地到达了巴黎，他的好友Peter带他开启了他的巴黎之旅。
#
# 途中，李华遇到了许多心动的纪念品想要带回家，但是他又不想自己太累，
# 而且他买纪念品也有相应的预算k，现给出他心动的纪念品清单：共有n件，其中每件都各有其价格price，
# 重量weight，心动值v(其中心动值为1~5之间的数值)，需要注意的是：在心动值不同的情况下，
# 李华会优先选择心动值大的纪念品；若心动值相同，李华会优先选择比较便宜的纪念品，具体见样例。
# 同时给出李华在保证不累的情况下，最多能拿的物品重量m。在不超过预算并且保证不累的情况下，
# 李华最多可以带几件纪念品回家？
class bag:
    def __init__(self, we, v, wi):
        self.we = we
        self.v = v
        self.wi = wi


# s = input()
# s = s.split()
# n = int(s[0])
# m = int(s[1])
# k = int(s[2])
# v = []
# we = []
# wi = []

# for i in range(n):
#     a = input()
#     a = a.split()
#     v.append(int(a[0]))
#     we.append(int(a[1]))
#     wi.append(int(a[2]))
y = []
# for i in range(n):
#     y.append(bag(we[i],v[i],wi[i]))


def sort(x):
    n = len(x)
    for i in range(n):
        for j in range(n-1):
            if x[j].wi > x[j+1].wi:
                x[j], x[j+1] = x[j+1], x[j]


def bq(x,k,w,v):
    if x[k].we<w:
        v = v+x[k].v
        w = w-x[k].we
        bq(x,k+1,w,v)
    else:
        a = w*x[k].wi
        v = v+a

#
# sort(y)
# bq(y,m,k,v)

for i in range(4):
    y.append(bag(i,i+1,10-i))
sort(y)
y.reverse()
for i in y:
    print(i.we,i.v,i.wi)

bq(y,)









