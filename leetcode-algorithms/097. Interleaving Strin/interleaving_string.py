
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3)!=len(s1)+len(s2):
            return False
        else:
            # 初始化 base case
            dp = [[False]*(len(s2)+1) for i in range(len(s1)+1)]
            dp[0][0] = True
            for i in range(1,len(s1)+1):
                dp[i][0] = dp[i-1][0] and s1[i-1]==s3[i-1]
            for i in range(1,len(s2)+1):
                dp[0][i] = dp[0][i-1] and s2[i-1]==s3[i-1]
            # 进行状态转移
            for i in range(1,len(s1)+1):
                for j in range(1,len(s2)+1):
                    up = dp[i-1][j] and s1[i-1]==s3[i+j-1]
                    left = dp[i][j-1] and s2[j-1]==s3[i+j-1]
                    dp[i][j] = left or up
            return dp[len(s1)][len(s2)]
s1 = "a"
s2 = ""
s3 = "a"
S = Solution()
re = S.isInterleave(s1, s2, s3)
print(re)