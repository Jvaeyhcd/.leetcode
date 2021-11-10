#
# @lc app=leetcode.cn id=1449 lang=python
#
# [1449] 数位成本和为目标值的最大数字
#

# @lc code=start
class Solution(object):
    def largestNumber(self, cost, target):
        """
        :type cost: List[int]
        :type target: int
        :rtype: str
        """
        dp = [-float('inf')] * (target + 1)
        dp[0] = 0
        for i in range(1, 10):
            u = cost[i - 1]
            for j in range(u, target + 1):
                dp[j] = max(dp[j], dp[j - u] + 1)
        
        if dp[target] < 0:
            return '0'
        
        ans = ''
        j = target
        for i in range(9, 0, -1):
            u = cost[i - 1]
            while j >= u and dp[j] == dp[j - u] + 1:
                ans += str(i)
                j -= u
        
        return ans
# @lc code=end

