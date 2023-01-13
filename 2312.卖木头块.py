#
# @lc app=leetcode.cn id=2312 lang=python3
#
# [2312] 卖木头块
#

# @lc code=start
from functools import lru_cache
from typing import List


class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        
        d = {(x, y): p for x, y, p in prices}
        @lru_cache(None)
        def dfs(x: int, y: int) -> int:
            ans = d.get((x, y), 0)
            for i in range(1, x):
                ans = max(ans, dfs(i, y) + dfs(x - i, y))
            for i in range(1, y):
                ans = max(ans, dfs(x, i) + dfs(x, y - i))
            return ans
        
        return dfs(m, n)
# @lc code=end

