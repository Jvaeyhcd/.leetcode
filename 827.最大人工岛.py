#
# @lc app=leetcode.cn id=827 lang=python3
#
# [827] 最大人工岛
#

# @lc code=start
import collections
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

    def is_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        uf = UnionFind(n * n)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    for ni, nj in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                            uf.union(ni * n + nj, i * n + j)

        mp = collections.defaultdict(int)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    p = uf.find(i * n + j)
                    mp[p] += 1

        ans = 0
        if mp:
            ans = max(mp.values())
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    # 上下左右四个方向，是否都有岛屿
                    ps = set()
                    t = 0
                    for ni, nj in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                            p = uf.find(ni * n + nj)
                            if p not in ps:
                                ps.add(p)
                                t += mp[p]
                    ans = max(ans, t + 1)

        return ans

# @lc code=end

solution = Solution()
grid = [[1,0],[1,0]]
print(solution.largestIsland(grid))