#
# @lc app=leetcode.cn id=1361 lang=python3
#
# [1361] 验证二叉树
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
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        uf = UnionFind(n)
        pa = [set() for _ in range(n)]
        for i, u, v in zip(range(n), leftChild, rightChild):
            if u != -1:
                pa[u].add(i)
                uf.union(i, u)
            
            if v != -1:
                pa[v].add(i)
                uf.union(i, v)
            
            if len(pa[u]) > 1 or len(pa[v]) > 1:
                return False

            for p in pa[i]:
                if i in pa[p]:
                    return False
        return uf.size == 1


# @lc code=end

