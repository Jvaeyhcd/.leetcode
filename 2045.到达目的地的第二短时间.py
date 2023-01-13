#
# @lc app=leetcode.cn id=2045 lang=python3
#
# [2045] 到达目的地的第二短时间
#

# @lc code=start
import collections
from typing import List


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        dist = [[float('inf') for _ in range(2)] for _ in range(n + 1)]
        dist[1][0] = 0
        queue = collections.deque([(1, 0)])
        while dist[n][1] == float('inf'):
            u, d = queue.popleft()
            for v in graph[u]:
                dis = d + 1
                if dis < dist[v][0]:
                    dist[v][0] = dis
                    queue.append((v, dis))
                elif dist[v][0] < dis < dist[v][1]:
                    dist[v][1] = dis
                    queue.append((v, dis))
        
        ans = 0
        for _ in range(dist[n][1]):
            if ans % (2 * change) >= change:
                ans += change * 2 - ans % (change * 2)
            ans += time
        return ans

# @lc code=end

