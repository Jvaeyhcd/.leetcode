#
# @lc app=leetcode.cn id=1034 lang=python3
#
# [1034] 边框着色
#

# @lc code=start
from typing import List


class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        target = grid[row][col]
        visited[row][col] = True
        que = [[row, col]]
        idx = [-1, 0, 1, 0, -1]
        while que:
            r, c = que.pop(0)
            for i in range(4):
                x, y = r + idx[i], c + idx[i + 1]
                if 0 <= x < m and 0 <= y < n and not visited[x][y] and grid[x][y] == target:
                    visited[x][y] = True
                    if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                        grid[x][y] = color
        if row == 0 or row == m - 1 or col == 0 or col == n - 1:
            grid[row][col] = color
        return grid
# @lc code=end

