#
# @lc app=leetcode.cn id=1049 lang=python
#
# [1049] 最后一块石头的重量 II
#

# @lc code=start
class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        total = sum(stones)
        n, m = len(stones), total // 2
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(n):
            for j in range(m + 1):
                if j < stones[i]:
                    dp[i + 1][j] = dp[i][j]
                else:
                    dp[i + 1][j] = dp[i][j] or dp[i][j - stones[i]]
        
        ans = None
        for j in range(m, -1, -1):
            if dp[n][j]:
                ans = total - 2 * j
                break
        
        return ans
# @lc code=end

