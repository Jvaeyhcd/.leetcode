#
# @lc app=leetcode.cn id=1559 lang=python3
#
# [1559] 二维网格图中探测环
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

    def is_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m * n)

        for i in range(m):
            for j in range(n):
                u = i * n + j
                for ni, nj in [[i + 1, j], [i, j + 1]]:
                    if 0 <= ni < m and 0 <= nj < n and grid[i][j] == grid[ni][nj]:
                        v = ni * n + nj
                        if uf.is_connected(u, v):
                            return True
                        uf.union(u, v)
        
        return False


# @lc code=end

solution = Solution()
grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
# grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
print(solution.containsCycle(grid))