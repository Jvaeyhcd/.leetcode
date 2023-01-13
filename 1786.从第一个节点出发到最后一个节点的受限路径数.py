#
# @lc app=leetcode.cn id=1786 lang=python3
#
# [1786] 从第一个节点出发到最后一个节点的受限路径数
#

# @lc code=start
import collections
import heapq
from typing import List


class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:

        def dijkstra(s: int, g: List[List[int]]):
            INF = 0xf3f3f3f3
            dis = collections.defaultdict(lambda:INF)
            dis[s] = 0

            q = [(0, s)]
            vis = set()
            while q:
                _, u = heapq.heappop(q)
                if u in vis:
                    continue
                vis.add(u)
                for v, w in g[u]:
                    if dis[v] > dis[u] + w:
                        dis[v] = dis[u] + w
                        heapq.heappush(q, (dis[v], v))
            
            return dis
        
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))
        

        dis = dijkstra(n, g)
        print(dis)


# @lc code=end

