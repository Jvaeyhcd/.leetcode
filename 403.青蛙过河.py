#
# @lc app=leetcode.cn id=403 lang=python
#
# [403] 青蛙过河
#

# @lc code=start
class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        n = len(stones)
        dp = [[False] * n for _ in range(n)]
        dp[0][0] = True

        for i in range(1, n):
            if stones[i] - stones[i - 1] > i:
                return False
        
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                k = stones[i] - stones[j]
                if k > j + 1:
                    break
                dp[i][k] = dp[j][k - 1] or dp[j][k] or dp[j][k + 1]
                if i == n - 1 and dp[i][k]:
                    return True
        
        return False
# @lc code=end

