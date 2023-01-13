#
# @lc app=leetcode.cn id=808 lang=python3
#
# [808] 分汤
#

# @lc code=start
class Solution:
    def soupServings(self, n: int) -> float:
        N = n // 25 + 1 if n % 25 > 0 else n // 25
        if N >= 200:
            return 1.0
        
        dp = [[0.0 for _ in range(N + 1)] for _ in range(N + 1)]
        dp[0][0] = 0.5
        for j in range(1, N + 1):
            dp[0][j] = 1.0
        
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                dp[i][j] += dp[max(i - 4, 0)][j]
                dp[i][j] += dp[max(i - 3, 0)][j - 1]
                dp[i][j] += dp[max(i - 2, 0)][max(j - 2, 0)]
                dp[i][j] += dp[i - 1][max(j - 3, 0)]
                dp[i][j] /= 4
        return dp[N][N]
# @lc code=end

