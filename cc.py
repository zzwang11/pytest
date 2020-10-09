import sys


class Solution:
    def hasGroupsSizeX(self, deck):
        deck.sort()
        n = len(deck)
        a = []
        for i in deck:
            c = deck.count(i)
            a.append(c)
        b = min(a)
        # print(b)
        print(a)
        if b<2:
            return False
        # print(a)
        i = 0
        while i<=n-1:
            f = deck[i:i+b]
            g = set(f)
            print(i)
            print(f)
            if len(f) != b:
                return False
            if len(g) == 1:
                i += b
            else:
                return False
        else:
            return True


# b = input()
# b = b.replace('[','')
# b = b.replace(']','')
# b = b.split(',')
# c = []
# for i in b:
#     c.append(int(i))
#
n = Solution()
b = n.hasGroupsSizeX([1,1,1,1,1,0,0,0,0])
print(b)
aa = [1,2,3,4,4,3,2,1]
aa.sort()
print(aa)

