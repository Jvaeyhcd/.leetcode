#
# @lc app=leetcode.cn id=790 lang=python3
#
# [790] 多米诺和托米诺平铺
#

# @lc code=start
class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        if n == 3: return 5
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5
        for i in range(4, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] * 2
        return dp[n]

# @lc code=end

