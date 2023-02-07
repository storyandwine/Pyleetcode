from typing import List

import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []
        for num in nums:
            if len(res) < k:
                heapq.heappush(res, num)
            elif num > res[0]:
                heapq.heappop(res)
                heapq.heappush(res, num)
        return heapq.heappop(res)


S = Solution()
numbers = [1]
target = 1
print(S.findKthLargest(numbers, target))

