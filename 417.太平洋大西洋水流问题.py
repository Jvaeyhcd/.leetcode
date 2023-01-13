#
# @lc app=leetcode.cn id=417 lang=python3
#
# [417] 太平洋大西洋水流问题
#

# @lc code=start
import collections
from typing import List
import functools


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        direction = [0, 1, 0, -1, 0]
        m, n = len(heights), len(heights[0])
        inpacific = [[False for _ in range(n)] for _ in range(m)]
        queue1 = collections.deque()
        visited1 = [[False for _ in range(n)] for _ in range(m)]
        for i in range(n):
            queue1.append((0, i))
            inpacific[0][i] = True
            visited1[0][i] = True
        for i in range(1, m):
            queue1.append((i, 0))
            inpacific[i][0] = True
            visited1[i][0] = True
        
        while queue1:
            x, y = queue1.popleft()
            for i in range(4):
                nx, ny = x + direction[i], y + direction[i + 1]
                if 0 <= nx < m and 0 <= ny < n and not visited1[nx][ny] and heights[nx][ny] >= heights[x][y]:
                    visited1[nx][ny] = True
                    queue1.append((nx, ny))
                    inpacific[nx][ny] = True

        inatlantic = [[False for _ in range(n)] for _ in range(m)]
        queue2 = collections.deque()
        visited2 = [[False for _ in range(n)] for _ in range(m)]
        for i in range(n):
            queue2.append((m - 1, i))
            inatlantic[m - 1][i] = True
            visited2[m - 1][i] = True
        for i in range(m - 1):
            queue2.append((i, n - 1))
            inatlantic[i][n - 1] = True
            visited2[i][n - 1] = True
        
        while queue2:
            x, y = queue2.popleft()
            for i in range(4):
                nx, ny = x + direction[i], y + direction[i + 1]
                if 0 <= nx < m and 0 <= ny < n and not visited2[nx][ny] and heights[nx][ny] >= heights[x][y]:
                    visited2[nx][ny] = True
                    queue2.append((nx, ny))
                    inatlantic[nx][ny] = True


        ans = []
        for i in range(m):
            for j in range(n):
                if inpacific[i][j] and inatlantic[i][j]:
                    ans.append([i, j])
        return ans
    
# @lc code=end

