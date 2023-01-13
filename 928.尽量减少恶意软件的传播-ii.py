#
# @lc app=leetcode.cn id=928 lang=python3
#
# [928] 尽量减少恶意软件的传播 II
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

        g = collections.defaultdict(list)

        circles = set()
        for i in range(n):
            for j in range(i):                    
                if graph[i][j] == 1:
                    g[i].append(j)
                    g[j].append(i)
                    if uf.is_connected(i, j):
                        circles.add(uf.find(i))
                    uf.union(i, j)

        cnts = collections.defaultdict(int)
        for u in range(n):
            cnts[uf.find(u)] += 1

        uf_cnts = collections.defaultdict(int)
        for u in initial:
            uf_cnts[uf.find(u)] += 1

        malware = set(initial)

        mx_cnt = 0
        ans = None
        for u in sorted(initial):
            p = uf.find(u)
            if uf_cnts[p] == 1 and cnts[p] > mx_cnt:
                mx_cnt = cnts[p]
                ans = u
            elif uf_cnts[p] > 1:
                s = set()
                s.add(u)
                for v in g[u]:
                    ss = set()
                    ss.add(v)
                    q = [v]
                    vis = set()
                    vis.add(u)
                    vis.add(v)
                    while q:
                        node = q.pop(0)
                        if node in malware:
                            ss = set()
                            break
                        ss.add(node)
                        for nxt in g[node]:
                            if nxt not in vis:
                                vis.add(nxt)
                                q.append(nxt)
                    s = s.union(ss)
                if len(s) > mx_cnt:
                    mx_cnt = len(s)
                    ans = u
        return ans
# @lc code=end

solution = Solution()
graph = [[1,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,1],[0,0,1,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,1],[0,0,0,0,1,0,1,1,1],[0,0,0,0,0,1,0,0,1],[0,0,0,0,1,0,1,1,0],[0,0,0,0,1,0,1,1,0],[0,1,0,1,1,1,0,0,1]]
initial = [8,4,2,0]

print(solution.minMalwareSpread(graph, initial))