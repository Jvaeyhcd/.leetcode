#
# @lc app=leetcode.cn id=1857 lang=python3
#
# [1857] 有向图中最大颜色值
#

# @lc code=start
import collections
from typing import List


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        g = collections.defaultdict(set)
        indeg = [0] * n
        for u, v in edges:
            g[u].add(v)
            indeg[v] += 1

        dp = [[0] * 26 for _ in range(n)]
        q = [i for i in range(n) if indeg[i] == 0]
        vis = set()
        while q:
            u = q.pop(0)
            dp[u][ord(colors[u]) - ord("a")] += 1
            vis.add(u)
            for v in g[u]:
                indeg[v] -= 1
                for c in range(26):
                    dp[v][c] = max(dp[v][c], dp[u][c])
                if indeg[v] == 0:
                    q.append(v)
        
        if len(vis) != n:
            return -1
        
        return max([max(dp[i]) for i in range(n)])
        

# @lc code=end

def topological_sort(n: int, edges: List[List[int]]):
    g = [set() for _ in range(n)]
    indeg = [0] * n
    for u, v in edges:
        g[u].add(v)
        indeg[v] += 1
    
    ans = []
    q = [i for i in range(n) if indeg[i] == 0]
    while q:
        u = q.pop(0)
        ans.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return ans