#
# @lc app=leetcode.cn id=1765 lang=python3
#
# [1765] 地图中的最高点
#

# @lc code=start
import collections
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        ans = [[0 if isWater[i][j] == 0 else -1 for j in range(n)] for i in range(m)]
        visited = [[False for _ in range(n)] for _ in range(m)]
        q = collections.deque()
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    q.append((i, j, 0))
                    visited[i][j] = True
        
        while q:
            for _ in range(len(q)):
                x, y, height = q.popleft()
                ans[x][y] = height
                for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                        q.append((nx, ny, height + 1))
                        visited[nx][ny] = True
        return ans
# @lc code=end

s = Solution()
isWater = [[0,0,1],[1,0,0],[0,0,0]]
isWater = [[0]]
print(s.highestPeak(isWater))