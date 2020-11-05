import sys
import os
import time

# class Solution:
#     def hasGroupsSizeX(self, deck):
#         deck.sort()
#         n = len(deck)
#         a = []
#         for i in deck:
#             c = deck.count(i)
#             a.append(c)
#         b = min(a)
#         # print(b)
#         print(a)
#         if b<2:
#             return False
#         # print(a)
#         i = 0
#         while i<=n-1:
#             f = deck[i:i+b]
#             g = set(f)
#             print(i)
#             print(f)
#             if len(f) != b:
#                 return False
#             if len(g) == 1:
#                 i += b
#             else:
#                 return False
#         else:
#             return True
#
#
# # b = input()
# # b = b.replace('[','')
# # b = b.replace(']','')
# # b = b.split(',')
# # c = []
# # for i in b:
# #     c.append(int(i))
# #
# n = Solution()
# b = n.hasGroupsSizeX([1,1,1,1,1,0,0,0,0])
# print(b)
# aa = [1,2,3,4,4,3,2,1]
# aa.sort()
# print(aa)/
outputfile = 'results.csv'
power = -10
temp = 3000
date = time.strftime('%Y-%m-%d')
path1 = os.getcwd()+f'/save1/{time.strftime("%Y-%m-%d",time.localtime())}/'
if not os.path.exists(path1):
    os.makedirs(path1)
file = path1 + outputfile[0:-4] + '_' + str(power) + 'dB' + '_' + str(
        temp) + 'mK' + '_'+time.strftime('%H-%M-%S', time.localtime()) + '.csv'
with open(file, 'a+', encoding='utf8') as a:
    a.write('aaaaaaaaaa')

a = open(file, 'r',encoding='utf8')
print(a.read())

