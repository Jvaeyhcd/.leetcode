#
# @lc app=leetcode.cn id=934 lang=python3
#
# [934] 最短的桥
#

# @lc code=start
import collections
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # 第一个岛的所有点
        points = []
        def dfs(i: int, j: int):
            if i < 0 or i > m - 1 or j < 0 or j > n - 1:
                return
            if grid[i][j] != 1:
                return
            if grid[i][j] == 1:
                grid[i][j] = 2
                points.append((i, j))
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        flag = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    flag = 1
                    break
            if flag:
                break
        
        queue = collections.deque()
        visited = [[False for _ in range(n)] for _ in range(m)]
        for point in points:
            queue.append((point, 0))
            visited[point[0]][point[1]] = True
        while queue:
            point, d = queue.popleft()
            i, j = point
            if grid[i][j] == 1:
                return d - 1
            for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:
                    visited[ni][nj] = True
                    queue.append(((ni, nj), d + 1))
            
# @lc code=end
S = Solution()
A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
A = [[0,1,0],[0,0,0],[0,0,1]]
print(S.shortestBridge(A))