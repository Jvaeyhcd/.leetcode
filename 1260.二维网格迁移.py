#
# @lc app=leetcode.cn id=1260 lang=python3
#
# [1260] 二维网格迁移
#

# @lc code=start
from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0 for _ in range(n)] for _ in range(m)]
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                index = (i * n + j + k) % (m * n)
                ans[index // n][index % n] = grid[i][j]
        return ans
# @lc code=end

