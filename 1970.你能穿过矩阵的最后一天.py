#
# @lc app=leetcode.cn id=1970 lang=python3
#
# [1970] 你能穿过矩阵的最后一天
#

# @lc code=start
from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.size = n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y
            self.size -= 1

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        n = row * col
        uf = UnionFind(n + 2)

        valid = [[0] * col for _ in range(row)]
        ans = 0
        for i in range(n - 1, -1, -1):
            x, y = cells[i][0] - 1, cells[i][1] - 1
            valid[x][y] = 1
            for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= nx < row and 0 <= ny < col and valid[nx][ny]:
                    uf.union(x * col + y, nx * col + ny)
            if x == 0:
                uf.union(x * col + y, n)
            if x == row - 1:
                uf.union(x * col + y, n + 1)
            
            if uf.connected(n, n + 1):
                ans = i
                break
        return ans
        
# @lc code=end

