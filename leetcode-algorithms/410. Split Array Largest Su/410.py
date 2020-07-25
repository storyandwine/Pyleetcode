from typing import List
#DP
# class Solution:
#     def splitArray(self, nums: List[int], m: int) -> int:
#         n = len(nums)
#         dp = [[0x7fffffff]*(m+1) for _ in range(n+1)]
#         sub = [0]
#         dp[0][0] = 0
#         for each in nums:
#             sub.append(sub[-1]+each)
#         for i in range(1,n+1):
#             for j in range(1,min(i,m)+1):
#                 for k in range(i):
#                     dp[i][j] = min(dp[i][j],max(dp[k][j - 1],sub[i] - sub[k]))
#         return dp[n][m]
#Bin_Search
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left = max(nums)
        right = sum(nums)
        def test_mid(mid):
            #初始化
            num = 1
            s = 0 #s表示当前数组的和

            for i in nums:
                if s+i > mid: #如果当前数组已经超过mid，要停止这个数组
                    s = i #这个数变为下一个数组的开头
                    num += 1 #会得到的数组数量+1
                else:
                    s += i

            return num > m

        while left < right:
            mid = (left + right) // 2
            if test_mid(mid):
                left = mid + 1
            else:
                right = mid
        return left
nums = [7,2,5,10,8]
m = 2
print(Solution().splitArray(nums, m))