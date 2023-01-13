#
# @lc app=leetcode.cn id=980 lang=python3
#
# [980] 不同路径 III
#

# @lc code=start
from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # 记录必须要通过的点
        cnt = 0
        start = end = (0, 0)
        for i in range(m):
            for j in range(n):
                if grid[i][j]  >= 0:
                    cnt += 1
                if grid[i][j] == 1:
                    start = (i, j)
                if grid[i][j] == 2:
                    end = (i, j)
        
        self.ans = 0
        def backtrack(path: List, point: tuple):
            if len(path) == cnt and point == end:
                # print(path)
                self.ans += 1
                return
            elif len(path) == cnt or point == end:
                return
            x, y = point
            for nx, ny in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
                if 0 <= nx < m and 0 <= ny < n:
                    if (nx, ny) not in path and grid[nx][ny] != -1:
                        backtrack(path + [(nx, ny)], (nx, ny))
        
        backtrack([start], start)
        return self.ans
            
# @lc code=end

S = Solution()
grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
grid = [[0,1],[2,0]]
grid = [[1,-1],[-1,2]]
print(S.uniquePathsIII(grid))