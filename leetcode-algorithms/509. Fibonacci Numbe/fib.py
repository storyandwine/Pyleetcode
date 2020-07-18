class Solution:
    def fib(self, N: int) -> int:
        # 初始化 base case
        dp = [0,1]
        new_dp = []
        # 进行状态转移
        if N<2:
            return N
        else:
            i = 2
            while(i<N):
                new_dp.append(dp[1])
                new_dp.append(sum(dp))
                dp = new_dp
                new_dp = []
                i=i+1
            return sum(dp)