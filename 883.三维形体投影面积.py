#
# @lc app=leetcode.cn id=883 lang=python3
#
# [883] 三维形体投影面积
#

# @lc code=start
from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0

        for i in range(m):
            for j in range(n):
                ans += (1 if grid[i][j] else 0)
            ans += max(grid[i])
        
        for j in range(n):
            res = 0
            for i in range(m):
                res = max(res, grid[i][j])
            ans += res
        return ans
# @lc code=end

