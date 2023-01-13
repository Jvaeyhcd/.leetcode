#
# @lc app=leetcode.cn id=2039 lang=python3
#
# [2039] 网络空闲的时刻
#

# @lc code=start
import collections
from typing import List


class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        n = len(patience)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        q = collections.deque([0])
        vis = [False for _ in range(n)]
        vis[0] = True
        ans, dist = 0, 1
        while q:
            for _ in range(len(q)):
                u = q.popleft()
                for v in graph[u]:
                    if not vis[v]:
                        vis[v] = True
                        q.append(v)
                        ans = max(ans, (dist * 2 - 1) // patience[v] * patience[v] + dist * 2 + 1)
            dist += 1
        return ans
# @lc code=end

