#
# @lc app=leetcode.cn id=664 lang=python
#
# [664] 奇怪的打印机
#

# @lc code=start
class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = [s[0]]
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                arr.append(s[i])
        
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if i == j:
                    dp[i][j] = 1
                
                if arr[i] == arr[j]:
                    dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = min(dp[i][k] + dp[k + 1][j] for k in range(i, j))
        
        return dp[0][n - 1]


# @lc code=end

