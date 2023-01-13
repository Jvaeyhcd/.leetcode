#
# @lc app=leetcode.cn id=399 lang=python3
#
# [399] 除法求值
#

# @lc code=start
import collections
from typing import List

class UnionFind:
    def __init__(self):
        self.parent = collections.defaultdict(str)
        self.weight = collections.defaultdict(lambda:1.0)

    def find(self, x: str) -> str:
        if x not in self.parent:
            self.parent[x] = x
        if self.parent[x] != x:
            origin = self.parent[x]
            self.parent[x] = self.find(origin)
            self.weight[x] *= self.weight[origin]
        return self.parent[x]

    def union(self, x: str, y: str, value: float):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y
            self.weight[root_x] = self.weight[y] * value / self.weight[x]

    def is_connected(self, x: str, y: str) -> float:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return self.weight[x] / self.weight[y]
        else:
            return -1.0


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        n = len(equations)
        m = len(queries)

        uf = UnionFind()
        ans = []
        items = set()
        for e, v in zip(equations, values):
            uf.union(e[0], e[1], v)
            items.add(e[0])
            items.add(e[1])
        
        for u, v in queries:
            if u not in items or v not in items:
                ans.append(-1.0)
            else:
                ans.append(uf.is_connected(u, v))

        return ans
# @lc code=end

