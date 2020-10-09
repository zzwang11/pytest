# class Solution:
#     def countCharacters(self, words, chars):
#
#         num = 0
#         ls1 = list(chars)
#         for j in words:
#             d2 = ls1.copy()
#             for x in j:
#                 if x not in d2:
#                     break
#                 else:
#                     d2.remove(x)
#             else:
#                 print(j)
#                 num += len(j)
#         return num
#
#
# if __name__ == '__main__':
#     words = ["hello","world","leetcode","eeee","eee"]
#
#     chars = "welldonehoneyr"
#
#     print(Solution().countCharacters(words, chars))
#
# a = {'1':'one','3':'three','2':'two','4':'four'}
# ls = sorted(a.items(), key = lambda e:e[0])
# for i in ls:
#     print(list(i))
#     print(i[1])

# b = [2,3,4,5,1,8,9,7]
# c = max(b)
# print(c)
# b.sort()


def minimumAbsDifference(arr):
    arr.sort()
    ls = []
    ls1 = []
    for i in range(len(arr) - 1):
        ls.append(arr[i + 1] - arr[i])
    for i in range(len(arr)-1):
        if ls[i] == min(ls):
            ls1.append([arr[i], arr[i + 1]])
    print(ls1)


a = [1,3,6,10,15]
minimumAbsDifference(a)