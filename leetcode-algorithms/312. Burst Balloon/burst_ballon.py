from typing import List
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) < 2:
            return nums[0]
        nums = [1] + nums + [1]
        dp = [[0] * len(nums) for n in range(len(nums))]
        for gap in range(2,len(nums)):
            for left in range(0,len(nums)-gap):
                right = left + gap
                for i in range(left+1,right):
                    dp[left][right] = max(dp[left][right],dp[left][i]+dp[i][right]+nums[i]*nums[left]*nums[right])
        return dp[0][-1]
s = Solution()
nums = [3,1,5,8]
print(s.maxCoins(nums))