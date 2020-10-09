# import sys
#
# n = int(sys.stdin.readline().strip())
#
#
#
# def urg(a):
#     if a == 1:
#         return 1
#     while a != 1:
#         if a % 2 == 0:
#             a = int(a/2)
#         elif a % 3 == 0:
#             a = int(a/3)
#         elif a % 5 == 0:
#             a = int(a/5)
#         else:
#             return 0
#     return 1
#
#
# j = 0
#
# i = 1
# while j<n:
#     if i%2==1 and i%10 not in [3,9]:
#         continue
#     if urg(i) == 1:
#             j +=1
#     i += 1
# print(i-1)

# for i in range(10000):
#     a = i // 1000
#     b = (i - 1000 * a) // 100
#     c = (i - 1000 * a - 100 * b) // 10
#     d = i - 1000 * a - 100 * b - 10 * c
#     if i+1000*b+100*c+10*d+a==8888:
#         print(a,b,c,d)


# import sys
# # line = sys.stdin.readline().strip()
# # a = list(map(int, line.split(',')))
# # b = a
# # # a.sort()
# # n = len(a)
# # i = 1
# # j = 1
# # x = 2
# # m = 0
# # l = []
# # while i<n-1:
# #     m += a[i]
# #     i += 1
# #     i += 2

# a = 7
# while a:
#
#     b = (a>>1)&1
#     print(b)
#     a = a >> 1