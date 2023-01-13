#
# @lc app=leetcode.cn id=1219 lang=python3
#
# [1219] 黄金矿工
#

# @lc code=start
from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0

        def backtrack(x: int, y: int, gold: int):
            gold += grid[x][y]
            nonlocal ans
            ans = max(ans, gold)

            tmp = grid[x][y]
            grid[x][y] = 0
            for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > 0:
                    backtrack(nx, ny, gold)
            grid[x][y] = tmp

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    backtrack(i, j, 0)
        return ans
# @lc code=end

