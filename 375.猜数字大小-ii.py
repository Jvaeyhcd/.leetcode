#
# @lc app=leetcode.cn id=375 lang=python3
#
# [375] 猜数字大小 II
#

# @lc code=start
# 动态规划
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        MAX = 0xf3f3f3f3
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for size in range(2, n + 1):
            for l in range(1, n - size + 2):
                r = l + size - 1
                min_cost = 0xf3f3f3f3
                for x in range(l, r):
                    cost = x + max(dp[l][x - 1], dp[x + 1][r])
                    min_cost = min(min_cost, cost)
                dp[l][r] = min_cost
        return dp[1][n]


# @lc code=end

# 记忆化搜索
from functools import lru_cache


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        return self.f(1, n)
    
    # 深度优先搜索依次递归搜索范围[l,r]间需要的最小花费
    @lru_cache(None)
    def f(self, l: int, r: int) -> int:
        if l >= r: return 0
        ans = 0xf3f3f3f3
        for x in range(l, r + 1):
            # cur表示猜的数字是x，需要支付的金额
            cur = max(self.f(l, x - 1), self.f(x + 1, r)) + x
            ans = min(ans, cur)
        return ans