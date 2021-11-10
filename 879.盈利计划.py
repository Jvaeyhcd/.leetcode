#
# @lc app=leetcode.cn id=879 lang=python
#
# [879] 盈利计划
#

# @lc code=start
class Solution(object):
    def profitableSchemes(self, n, minProfit, group, profit):
        """
        :type n: int
        :type minProfit: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1

        print zip(profit, group)
        
        for earn, members in zip(profit, group):
            for j in range(n, members - 1, -1):
                for k in range(minProfit, -1, -1):
                    dp[j][k] = (dp[j][k] + dp[j - members][max(0, k - earn)]) % MOD
        
        return dp[n][minProfit]
# @lc code=end

