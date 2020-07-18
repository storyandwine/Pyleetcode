class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        for i in range(amount+1):
            for j in coins:
                if i - j < 0:
                    continue
                dp[i] = min(dp[i],1+dp[i-j])
        if dp[amount] == amount+1:
            return -1
        else:
            return dp[amount]