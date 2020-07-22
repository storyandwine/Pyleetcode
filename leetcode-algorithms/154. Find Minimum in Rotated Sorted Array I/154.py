from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left<right:
            mid = (left+right)//2
            if nums[mid]>nums[right]:
                left = mid+1
            elif nums[mid]<nums[right]:
                right = mid
            else:
                right -= 1
        return nums[left]

S = Solution()
nums = [2,2,2,0,1]
print(S.findMin(nums))