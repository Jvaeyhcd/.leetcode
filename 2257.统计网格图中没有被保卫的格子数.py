#
# @lc app=leetcode.cn id=2257 lang=python3
#
# [2257] 统计网格图中没有被保卫的格子数
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]
        queue = deque([])
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        for i, j in guards:
            grid[i][j] = -1
            for k in range(4):
                queue.append((i, j, k))
        for i, j in walls:
            grid[i][j] = -2

        while queue:
            x, y, k = queue.popleft()
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] >= 0:
                if grid[nx][ny] & (1 << k) == 0:
                    grid[nx][ny] |= (1 << k)
                    queue.append((nx, ny, k))
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    ans += 1
        return ans
# @lc code=end

