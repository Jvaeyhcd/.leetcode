#
# @lc app=leetcode.cn id=407 lang=python3
#
# [407] 接雨水 II
#

# @lc code=start
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        M, N = len(heightMap), len(heightMap[0])
        maxHeight = max(max(row) for row in heightMap)
        water = [[maxHeight for _ in range(N)] for _ in range(M)]
        dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        que = []
        for i in range(M):
            for j in range(N):
                if i == 0 or i == M - 1 or j == 0 or j == N - 1:
                    if water[i][j] > heightMap[i][j]:
                        water[i][j] = heightMap[i][j]
                        que.append([i, j])
        
        while que:
            x, y = que.pop(0)
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx >= M or ny >= N:
                    continue
                if water[x][y] < water[nx][ny] and water[nx][ny] > heightMap[nx][ny]:
                    water[nx][ny] = max(water[x][y], heightMap[nx][ny])
                    que.append([nx, ny])
        
        ans = 0
        for i in range(M):
            for j in range(N):
                ans += (water[i][j] - heightMap[i][j])
        return ans
# @lc code=end

