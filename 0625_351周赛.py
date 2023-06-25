# class Solution:

#     def gcd(self, a, b):
#         if a > b:
#             a, b = b, a
#         while a != 0:
#             a, b = b % a, a
#         return b
#     def countBeautifulPairs(self, nums) -> int:
#         n = len(nums)
#         ans = 0
#         for i in range(n):
#             for j in range(i+1, n):


#                 if self.gcd(int(str(nums[i])[0]),int(str(nums[j])[-1])) == 1:
#                     ans += 1
#         return ans

# s = Solution()
# print(s.countBeautifulPairs([2,5,1,4]))

class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        if num1 - (1+num2) < 0:
            return -1

        ans = float('inf')

        def dfs(step,num):
            if num == 0:
                nonlocal ans
                ans = min(ans, step)
                return

            tmp = float('inf')
            idx = None
            for i in range(60,-1,-1):
                tmp = min(tmp, abs(num-(2**i+num2)))
                if tmp == abs(num-(2**i+num2)) and num!=num-(2**i+num2) :
                    idx = i
            new_num = num-(2**idx+num2)
            dfs(step+1,new_num)        
        dfs(0, num1)
        return ans
s = Solution()
print(s.makeTheIntegerZero(3,-2))
print(s.makeTheIntegerZero(5,-21)) # 3


# class Solution:
#     def numberOfGoodSubarraySplits(self, nums) -> int:
#         i_list = [idx for idx,i in enumerate(nums) if i == 1]
#         n = len(i_list)
#         if n==0:
#             return 0
#         ans = 1
#         for i in range(n-1):
#             ans*=(i_list[i+1] - i_list[i])
#             ans%=(10**9 + 7)
#         return ans


# s = Solution()
# print(s.numberOfGoodSubarraySplits([0,1,0,0,1]))
# print(s.numberOfGoodSubarraySplits([0,1,0]))
# print(s.numberOfGoodSubarraySplits([0,0,0]))



# 碰撞问题用栈
# class Solution:
#     def survivedRobotsHealths(self, positions, healths, directions: str):

#         # 碰撞的条件主要是 position[i] < position[j] and directions[i]=  = R  directions[i]=L
#         tmp = [ ]
#         for i,j,k in zip(positions, healths, directions):
#             tmp.append([i,j,k])
#         tmp = sorted(tmp,key=lambda x:(x[0],x[1],x[2]))
#         # positions = []
#         # healths = []
#         # directions =[]
#         # for i,j,k in tmp:
#         #     positions.append(i)
#         #     healths.append(j)
#         #     directions.append(k)


#         n = len(positions)

#         for i in range(n-1):
#             for j in range(i+1, n):
#                 if positions[i]< positions[j] and directions[i] == 'R' and directions[j] == 'L' and healths[i] !=-1 and healths[j] != -1:
#                     if healths[i] < healths[j]:
#                         healths[i] = -1
#                         healths[j] -= 1
#                     elif healths[i] == healths[j]:
#                         healths[i] = -1
#                         healths[j] = -1
#                     else:
#                         healths[j] = -1
#                         healths[i] -= 1
#                 elif positions[i] > positions[j] and directions[i] == 'L' and directions[j] == 'R' and healths[i] !=-1 and healths[j] != -1:
#                     if healths[i] < healths[j]:
#                         healths[i] = -1
#                         healths[j] -= 1
#                     elif healths[i] == healths[j]:
#                         healths[i] = -1
#                         healths[j] = -1
#                     else:
#                         healths[j] = -1
#                         healths[i] -= 1

#         return [i for i in healths if i!=-1]


# s = Solution()
# print(s.survivedRobotsHealths(positions = [5,4,3,2,1], healths = [2,17,9,15,10], directions = "RRRRR"))
# print(s.survivedRobotsHealths(positions = [3,5,2,6], healths = [10,10,15,12], directions = "RLRL"))
# print(s.survivedRobotsHealths(positions = [1,2,5,6], healths = [10,10,11,11], directions = "RLRL"))
# print(s.survivedRobotsHealths(positions = [13,3], healths = [17,2], directions = "LR"))
# print(s.survivedRobotsHealths(positions = [4,37,23], healths = [50,15,49], directions = "RLR"))

