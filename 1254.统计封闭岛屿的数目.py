#
# @lc app=leetcode.cn id=1254 lang=python3
#
# [1254] 统计封闭岛屿的数目
#

# @lc code=start
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def get(x: int, y: int) -> int:
            return x * n + y

        cnt_1 = 0
        cnt_0 = 0
        UF = UnionFind(m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cnt_1 += 1
                    continue
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    cnt_0 += 1
                for ni, nj in [[i, j - 1], [i, j + 1], [i - 1, j], [i + 1, j]]:
                    if 0 < ni < m - 1 and 0 < nj < n - 1 and grid[ni][nj] == 0:
                        UF.union(get(i, j), get(ni, nj))

        return UF.size - cnt_1 - cnt_0


class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.size = n

    
    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    

    def union(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y
            self.size -= 1

# @lc code=end

