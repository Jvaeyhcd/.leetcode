#
# @lc app=leetcode.cn id=1391 lang=python3
#
# [1391] 检查网格中是否存在有效路径
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
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m * n)

        for i in range(m):
            for j in range(n):
                a = grid[i][j]
                u = i * n + j
                
                # 左边的点
                if j - 1 >= 0:
                    b = grid[i][j - 1]
                    v = i * n + j - 1
                    if a == 1 and (b == 1 or b == 4 or b == 6):
                        uf.union(u, v)
                    elif a == 3 and (b == 4 or b == 6):
                        uf.union(u, v)
                    elif a == 5 and (b == 4 or b == 6):
                        uf.union(u, v)

                # 右边的点
                if j + 1 < n:
                    b = grid[i][j + 1]
                    v = i * n + j + 1
                    if a == 1 and (b == 1 or b == 3 or b == 5):
                        uf.union(u, v)
                    elif a == 4 and (b == 3 or b == 5):
                        uf.union(u, v)
                    elif a == 6 and (b == 3 or b == 5):
                        uf.union(u, v)
                # 上边的点
                if i - 1 >= 0:
                    b = grid[i - 1][j]
                    v = (i - 1) * n + j
                    if (a == 2 or a == 5 or a == 6) and (b == 2 or b == 3 or b == 4):
                        uf.union(u, v)
                # 下边的点
                if i + 1 < m:
                    b = grid[i + 1][j]
                    v = (i + 1) * n + j
                    if (a == 2 or a == 3 or a == 4) and (b == 2 or b == 5 or b == 4):
                        uf.union(u, v)
        
        return uf.is_connected(0, m * n - 1)
# @lc code=end

solution = Solution()
grid = [[1,1,1,1,3],[1,1,1,1,2],[1,1,1,1,2],[1,1,1,1,2],[1,1,1,1,2]]
print(solution.hasValidPath(grid))