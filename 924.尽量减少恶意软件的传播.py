#
# @lc app=leetcode.cn id=924 lang=python3
#
# [924] 尽量减少恶意软件的传播
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
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        n = len(graph)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i):                    
                if graph[i][j] == 1:
                    uf.union(i, j)

        cnts = collections.defaultdict(int)
        for u in range(n):
            cnts[uf.find(u)] += 1

        uf_cnts = collections.defaultdict(int)
        for u in initial:
            uf_cnts[uf.find(u)] += 1

        mx_cnt = 0
        ans = None
        for u in sorted(initial):
            p = uf.find(u)
            if uf_cnts[p] == 1 and cnts[p] > mx_cnt:
                mx_cnt = cnts[p]
                ans = u
            elif uf_cnts[p] > 1:
                if ans is None:
                    ans = u
        return ans
        
# @lc code=end

solution = Solution()

graph = [[1,1,0],[1,1,0],[0,0,1]]
initial = [0,1]

# graph = [[1,1,1],[1,1,1],[1,1,1]]
# initial = [1,2]

print(solution.minMalwareSpread(graph, initial))