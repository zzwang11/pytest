# # import sys
# # if __name__ == "__main__":
# #     #读n，m
# #     num = sys.stdin.readline().strip()
# #     values = list(map(int, num.split()))
# #     n = values[0]
# #     m = values[1]
# #     #读S,T
# #     S = sys.stdin.readline().strip()
# #     T = sys.stdin.readline().strip()
# #     #s的字串
# #     tem = []
# #     like_num = 0
# #     for i in range(n):
# #         for j in range(i+1,n+1):
# #             tem.append(S[i:j])
# #     print(tem)
# #     # temp = []
# #     #     # size = 2**m
# #     #     #
# #     #     # for i in range(size):
# #     #     #     aa = ''
# #     #     #     for j in range(m):
# #     #     #         if (i>>j) % 2:
# #     #     #             aa += T[j]
# #     #     #     if aa:
# #     #     #         temp.append(aa)
# #     #     # print(temp)
# #     #     # for i in tem:
# #     #     #     if i in temp:
# #     #     #         like_num += 1
# #
# #     for i in tem:
# #         x = len(i)
# #         k = 0
# #         l = 0
# #         while k<x and l<m:
# #             if i[k]==T[l]:
# #                 k += 1
# #             l += 1
# #             if k==x:
# #                 like_num += 1
# #     print(like_num)
#
#
# import sys
# if __name__ == "__main__":
#     # 读取第一行的n
#     num = sys.stdin.readline().strip()
#     values = list(map(int, num.split()))
#     n = values[0]
#     m = values[1]
#     a = []
#     b = []
#     for i in range(n):
#         # 读取每一行
#         line = sys.stdin.readline().strip()
#         line1 = line.split()
#         a.append(int(line1[0],2))
#         b.append(int(line1[1]))
#     print(a)
#
#         # 把每一行的数字分隔后转化成int列表

