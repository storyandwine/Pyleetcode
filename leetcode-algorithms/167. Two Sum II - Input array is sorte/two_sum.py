from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        while 1:
            sums = numbers[i]+numbers[j]
            if target < sums:
                j = j-1
            elif target > sums:
                i = i+1
            else:
                return i+1,j+1
S = Solution()
numbers = [2, 7, 11, 15]
target = 9
print(S.twoSum(numbers,target))