class Solution:
    def numberofprize(self, a, b, c):
        l = [a,b,c]
        l.sort()
        x = l[0]
        y = l[1]
        z = l[2]
        i = x
        s = i
        while i<=z:
            if i==x==y==z:
                s = i
                break
            if x<=i<=y:
                if (z + y - 2*i)>=(i-x)*2:
                    i += 1
                else:
                    s = i-1
                    break
            elif y<i<=z:
                if (z - i)>=(i*2 - x - y)*2:
                    i +=1
                else:
                    s = i-1
                    break
        return s




a = Solution()
print(a.numberofprize(2,2,7))


# class Solution:
#     def getHouses(self, t, xa):
# # write code here
#         m = 2
#         n = len(xa)
#         i = 0
#         a = []
#         while i<n:
#             x = xa[i]
#             y = xa[i+1]
#             a.append(x-y/2)
#             a.append(x+y/2)
#             i += 2
#         i = 1
#         while i < n-1:
#             if a[i+1]-a[i] > t:
#                 m += 2
#             elif a[i+1]-a[i] == t:
#                 m +=1
#             i += 2
#         return m
#
# s = Solution()
# print(s.getHouses(2,[-1,4,5,2]))







