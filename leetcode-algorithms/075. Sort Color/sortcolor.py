from typing import List

"""
交换过的元素还需要做判断
"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, left, right = 0, 0, len(nums) - 1
        while i <= right:
            if i < left:
                i += 1
            elif nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            else:
                i += 1
        return nums


S = Solution()
print(S.sortColors([2, 0, 2, 1, 1, 0]))

