#
# @lc app=leetcode.cn id=1278 lang=python
#
# [1278] 分割回文串 III
#

# @lc code=start
class Solution(object):
    def palindromePartition(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def cost(l, r):
            ans, i, j = 0, l, r
            while i < j:
                ans += (0 if s[i] == s[j] else 1)
                i += 1
                j -= 1
            return ans
        
        n = len(s)
        MAX = 10 ** 9 + 7
        dp = [[MAX] * (k + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, min(i, k) + 1):
                if j == 1:
                    dp[i][j] = cost(0, i - 1)
                else:
                    for i0 in range(j - 1, i):
                        dp[i][j] = min(dp[i][j], dp[i0][j - 1] + cost(i0, i - 1))
        
        return dp[n][k]

# @lc code=end

