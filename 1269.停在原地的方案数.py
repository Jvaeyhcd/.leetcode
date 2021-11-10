#
# @lc app=leetcode.cn id=1269 lang=python
#
# [1269] 停在原地的方案数
#

# @lc code=start
class Solution(object):
    def numWays(self, steps, arrLen):
        """
        :type steps: int
        :type arrLen: int
        :rtype: int
        """
        mod = 10**9 + 7
        max_column = min(arrLen - 1, steps)

        dp = [[0] * (max_column + 1) for _ in range(steps + 1)]
        dp[0][0] = 1

        for i in range(1, steps + 1):
            for j in range(0, max_column + 1):
                dp[i][j] = dp[i - 1][j]
                if j - 1 >= 0:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % mod
                if j + 1 <= max_column:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j + 1]) % mod
        
        return dp[steps][0]


        
# @lc code=end

