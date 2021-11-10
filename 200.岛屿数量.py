#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
from typing import List


# 方法一：BFS广度优先搜索
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         dirs = [-1, 0, 1, 0, -1]
#         m, n = len(grid), len(grid[0])
#         self.visited = [[0 for _ in range(n)] for _ in range(m)]
#         self.ans = 0

#         def bfs(row: int, col: int):
#             self.visited[row][col] = 1
#             que = [[row, col]]
#             while que:
#                 r, c = que.pop(0)
#                 for i in range(4):
#                     nr, nc = r + dirs[i], c + dirs[i + 1]
#                     if 0 <= nr < m and 0 <= nc < n and self.visited[nr][nc] == 0 and grid[nr][nc] == '1':
#                         que.append([nr, nc])
#                         self.visited[nr][nc] = 1
#             self.ans += 1
        
#         for r in range(m):
#             for c in range(n):
#                 if grid[r][c] == '1' and self.visited[r][c] == 0:
#                     bfs(r, c)
        
#         return self.ans

# 方法二：并查集
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


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m * n)
        dirs = [-1, 0, 1, 0, -1]
        zero_count = 0

        def pos(x: int, y: int) -> int:
            return x * n + y

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    zero_count += 1
                    continue
                p = pos(i, j)
                for k in range(4):
                    ni, nj = i + dirs[k], j + dirs[k + 1]
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == '1':
                        uf.union(p, pos(ni, nj))
        return uf.size - zero_count
        

# @lc code=end

solution = Solution()
print(solution.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
print(solution.numIslands([["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","0","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0"],["1","0","1","1","1","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","0","1","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1"],["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],["1","0","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]]))