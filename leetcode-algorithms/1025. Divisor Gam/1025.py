class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = [False for i in range(N+1)]
        dp[2] = True
        for i in range(3,N+1):
             for j in range(1, i//2 + 1):
                    if i % j == 0 and (not dp[i - j]):
                        dp[i] = True
                        break
        return dp[N]
# print(Solution().divisorGame(2))
print(Solution().divisorGame(5))