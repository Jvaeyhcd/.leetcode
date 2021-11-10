#
# @lc app=leetcode.cn id=552 lang=python
#
# [552] 学生出勤记录 II
#

# @lc code=start
class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        dp = [[[-1] * 3 for _ in range(2)] for _ in range(n + 1)]

        # 记忆化搜索，长度为i时，缺席次数还可以为a，还可以连续迟到天数为l的方案数
        def dfs(i, a, l):
            # 已搜索过直接返回
            if dp[i][a][l] != -1:
                return dp[i][a][l]
            if i == n:
                return 1
            
            ans = 0
            # P随便放
            ans += dfs(i + 1, a, 0)
            # A最多只能放一个
            if a == 0:
                ans += dfs(i + 1, 1, 0)
            # L最多放2个
            if l < 2:
                ans += dfs(i + 1, a, l + 1)
            
            ans %= MOD
            # 将已搜索过的记录下来
            dp[i][a][l] = ans
            return ans
        
        return dfs(0, 0, 0)

# @lc code=end

