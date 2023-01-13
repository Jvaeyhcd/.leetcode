#
# @lc app=leetcode.cn id=741 lang=python3
#
# [741] 摘樱桃
#

# @lc code=start
from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        INF = 0x3f3f3f3f
        f = [[[-INF] * n for _ in range(n)] for _ in range(2 * n - 1)]
        f[0][0][0] = grid[0][0]
        for k in range(1, 2 * n - 1):
            for x1 in range(max(k - n + 1, 0), min(k + 1, n)):
                y1 = k - x1
                if grid[x1][y1] == -1:
                    continue
                for x2 in range(x1, min(k + 1, n)):
                    y2 = k - x2
                    if grid[x2][y2] == -1:
                        continue
                    res = f[k - 1][x1][x2]
                    if x1:
                        res = max(res, f[k - 1][x1 - 1][x2])
                    if x2:
                        res = max(res, f[k - 1][x1][x2 - 1])
                    if x1 and x2:
                        res = max(res, f[k - 1][x1 - 1][x2 - 1])
                    res += grid[x1][y1]
                    if x1 != x2:
                        res += grid[x2][y2]
                    f[k][x1][x2] = res
        
        return max(f[-1][-1][-1], 0)

# @lc code=end

