# class Solution:
#     def maximumNumberOfStringPairs(self, words) -> int:

#         ans = 0
#         for idx,i in enumerate(words):
#             for j in words[idx:]:
#                 if i == j:
#                     continue
#                 if i[::-1] == j:
#                     ans += 1
#                     break
#         return ans


# s  = Solution()
# print(s.maximumNumberOfStringPairs(["cd","ac","dc","ca","zz"]))



'''
AA  后面不能接 AA  AB
AB  后面不能接 BB
BB  后面不能接 BB
'''
# class Solution:
#     def longestString(self, x: int, y: int, z: int) -> int:
#         res = float("-inf")

#         def dfs(x,y,z,ans,step):
#             if x==0 or y==0 or z==0:
#                 nonlocal res
#                 res = max(res,step*2)
#             if ans == "AA":
#                 if y-1>=0:
#                     dfs(x,y-1,z,"BB",step+1)
#             elif ans == "BB":
#                 if x-1>=0:
#                     dfs(x-1,y,z,"AA",step+1)
#                 if z-1>=0:
#                     dfs(x,y,z-1,"AB",step+1)
#             elif ans == "AB":
#                 if x-1>=0:
#                     dfs(x-1,y,z,"AA",step+1)
#                 if z-1>=0:
#                     dfs(x,y,z-1,"AB",step+1)
        
#         if x>0:
#             dfs(x-1,y,z,"AA",1)
#         if y>0:
#             dfs(x,y-1,z,"BB",1)
#         if z>0:
#             dfs(x,y,z-1,"AB",1)
#         return res



# s  = Solution()
# print(s.longestString(2,5,1))


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)
    
    def get_components(self):
        components = {}
        for i in range(len(self.parent)):
            root = self.find(i)
            if root in components:
                components[root].append(i)
            else:
                components[root] = [i]
        print(components)
        return len(components)

class Solution:
    

    def minimizeConcatenatedLength(self, words) -> int:
        ans = sum([len(i) for i in words])

        uf = UnionFind(len(words))
                   
        for idx,i in enumerate(words):
            for jdx,j in enumerate(words):
                if idx != jdx and i[-1] == j[0]:
                    uf.union(idx,jdx)


        return  ans-(len(words)-uf.get_components())
s = Solution()
print(s.minimizeConcatenatedLength(["aa","ab","bc"])) # 4
print(s.minimizeConcatenatedLength(["aaa","c","aba"])) # 6
print(s.minimizeConcatenatedLength(["a","aa","ba"])) # 3
print(s.minimizeConcatenatedLength(["ab","cbb","bab"])) # 7

# a
#  aa -> ab  -> bc     6-2=4   6-(3-1) #数组数-连通分量
# aaa -> aba        7-1=6    7-(3-2)
# a -> aa        ba ->a ->aa  5-2 = 3    5-(3-1)
# ab->bab       cbb   8-1=7  # 7 -(3-2)










