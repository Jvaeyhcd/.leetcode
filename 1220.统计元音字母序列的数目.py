#
# @lc app=leetcode.cn id=1220 lang=python3
#
# [1220] 统计元音字母序列的数目
#

# @lc code=start
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9+7
        # dp[i][0] 代表a
        # dp[i][1] 代表e
        # dp[i][2] 代表i
        # dp[i][3] 代表o
        # dp[i][4] 代表u
        dp = [[0 for _ in range(5)] for _ in range(n + 1)]
        for i in range(5):
            dp[1][i] = 1
        
        for i in range(2, n + 1):
            dp[i][0] = (dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4]) % MOD
            dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % MOD
            dp[i][2] = (dp[i - 1][1] + dp[i - 1][3]) % MOD
            dp[i][3] = (dp[i - 1][2]) % MOD
            dp[i][4] = (dp[i - 1][2] + dp[i - 1][3]) % MOD
        
        return sum(dp[n]) % MOD

# @lc code=end

