#
# @lc app=leetcode.cn id=1020 lang=python3
#
# [1020] 飞地的数量
#

# @lc code=start
import collections
from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        q = collections.deque([])
        visited = set()
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cnt += 1
                    if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                        q.append((i, j))
                        visited.add((i, j))
        while q:
            x, y = q.popleft()
            cnt -= 1
            for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= nx < m and 0 <= ny < n:
                    if (nx, ny) not in visited and grid[nx][ny] == 1:
                        q.append((nx, ny))
                        visited.add((nx, ny))
        return cnt
# @lc code=end

