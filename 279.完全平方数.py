#
# @lc app=leetcode.cn id=279 lang=python
#
# [279] 完全平方数
#

# @lc code=start
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            minn = float('inf')
            j = 1
            while j * j <= i:
                minn = min(minn, dp[i - j * j])
                j += 1
            dp[i] = minn + 1
        
        return dp[n]

# @lc code=end

