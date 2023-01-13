#
# @lc app=leetcode.cn id=1905 lang=python3
#
# [1905] 统计子岛屿
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
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])

        uf = UnionFind(m * n)
        for i in range(m):
            for j in range(n):
                for ni, nj in [[i + 1, j], [i, j + 1]]:
                    if 0 <= ni < m and 0 <= nj < n:
                        if grid2[i][j] == grid2[ni][nj] == 1:
                            uf.union(ni * n + nj, i * n + j)
        
        mp = collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    pa = uf.find(i * n + j)
                    mp[pa].append((i, j))

        ans = 0
        for _, pos in mp.items():
            flag = True
            for i, j in pos:
                if grid1[i][j] != 1:
                    flag = False
                    break
            if flag:
                ans += 1
        return ans


        
# @lc code=end

