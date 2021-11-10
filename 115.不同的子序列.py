#
# @lc app=leetcode.cn id=115 lang=python
#
# [115] 不同的子序列
#

# @lc code=start
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # 技巧：往原字符头部插入空格，这样得到 char 数组是从 1 开始，
        # 同时由于往头部插入相同的（不存在的）字符，不会对结果造成影响，
        # 而且可以使得 f[i][0] = 1，可以将 1 这个结果滚动下去
        n, m = len(s), len(t)
        s = " " + s
        t = " " + t
        # dp[i][j]代表考虑「s 中的下标为 0~i 字符」和「t 中下标为 0~j 字符」是否匹配
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        # 原字符只有小写字符，当往两个字符插入空格之后，
        # dp[i][0] = 1 是一个显而易见的初始化条件
        for i in range(n):
            dp[i][0] = 1
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # 不使用 s[i] 进行匹配，则有 dp[i][j] = dp[i - 1][j]
                dp[i][j] = dp[i - 1][j]
                # 若s[i] == t[j]，则可以使用s[i]进行匹配，
                # 然后就会多出dp[i - 1][j - 1]种匹配，所以有
                # dp[i][j] += dp[i - 1][j - 1]
                if s[i] == t[j]:
                    dp[i][j] += dp[i - 1][j - 1]
        
        return dp[n][m]
# @lc code=end

