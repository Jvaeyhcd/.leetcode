#
# @lc app=leetcode.cn id=886 lang=python3
#
# [886] 可能的二分法
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
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        uf = UnionFind(n + 1)
        dis = [0] * (n + 1)

        for a, b in dislikes:
            if uf.is_connected(a, b):
                return False
            
            if dis[a] == 0:
                dis[a] = b
            else:
                uf.union(dis[a], b)
            
            if dis[b] == 0:
                dis[b] = a
            else:
                uf.union(dis[b], a)
        return True

# @lc code=end

