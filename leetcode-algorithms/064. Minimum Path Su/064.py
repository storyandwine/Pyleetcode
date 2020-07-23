from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0]*2+[9999]*(n-1)]+[[0]+[9999]*n]+[[9999]*(n+1) for _ in range(m-1)]
        i = 1
        j = 1
        for i in range(1,m+1):
            for j in range(1,n+1): 
                dp[i][j] = min(dp[i-1][j],dp[i][j-1])+grid[i-1][j-1]
        return dp[m][n]
S = Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]])
print(S)