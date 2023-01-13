#
# @lc app=leetcode.cn id=2003 lang=python3
#
# [2003] 每棵子树内缺失的最小基因值
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
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        MAX_N = 10 ** 5 + 5
        n = len(parents)

        self.uf = UnionFind(MAX_N)
        self.ans = [1] * n

        g = [[] for _ in range(n)]
        for i, p in enumerate(parents):
            if p >= 0:
                g[p].append(i)

        def dfs(u: int) -> int:
            if not g[u]:
                if nums[u] != 1:
                    self.ans[u] = 1
                    return 1
                else:
                    self.ans[u] = 2
                    return 2
            else:
                mx = 1
                for v in g[u]:
                    mx = max(mx, dfs(v))
                    self.uf.union(nums[u], nums[v])
                
                root = self.uf.find(nums[u])
                for i in range(mx, MAX_N):
                    if root != self.uf.find(i):
                        self.ans[u] = i
                        return i
            return 0
        
        dfs(0)

        return self.ans

        
# @lc code=end

