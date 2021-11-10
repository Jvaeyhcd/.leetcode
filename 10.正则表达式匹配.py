#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
# 动态规划
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def matches(i: int, j: int) -> bool:
            if i == 0: return False
            if p[j - 1] == '.': return True
            return s[i - 1] == p[j - 1]

        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        # 初始状态
        dp[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] |= dp[i][j - 2]
                    if matches(i, j - 1):
                        dp[i][j] |= dp[i - 1][j]
                else:
                    if matches(i, j):
                        dp[i][j] |= dp[i - 1][j - 1]
        return dp[m][n]

# @lc code=end

