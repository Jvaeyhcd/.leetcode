#
# @lc app=leetcode.cn id=516 lang=python
#
# [516] 最长回文子序列
#

# @lc code=start
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        
        arr = list(s)
        for l in range(2, n + 1):
            for i in range(n):
                j = i + l - 1
                if j > n - 1:
                    break
                if arr[i] == arr[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
        return dp[0][n - 1]
# @lc code=end

