#
# @lc app=leetcode.cn id=2050 lang=python3
#
# [2050] 并行课程 III
#

# @lc code=start
import collections
from heapq import heappop, heappush
from typing import List


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        g = collections.defaultdict(list)
        pa = collections.defaultdict(list)
        indeg = [0] * n
        dis = [0] * n
        for u, v in relations:
            g[u - 1].append(v - 1)
            pa[v - 1].append(u - 1)
            indeg[v - 1] += 1
        
        ans = 0
        q = [(u, time[u]) for u in range(n) if indeg[u] == 0]
        while q:
            t = 0
            s = len(q)
            for _ in range(s):
                u, t = q.pop(0)
                dis[u] = t
                ans = max(ans, t)

                for v in g[u]:
                    indeg[v] -= 1
                    if indeg[v] == 0:
                        d = 0
                        for p in pa[v]:
                            d = max(d, dis[p])
                        q.append((v, d + time[v]))
        return ans
# @lc code=end

solution = Solution()

n = 9
relations = [[2,7],[2,6],[3,6],[4,6],[7,6],[2,1],[3,1],[4,1],[6,1],[7,1],[3,8],[5,8],[7,8],[1,9],[2,9],[6,9],[7,9]]
time = [9,5,9,5,8,7,7,8,4]

# n = 3
# relations = [[1,3],[2,3]]
# time = [3,2,5]

# n = 9
# relations = [[3,2],[3,1],[1,7],[2,7],[4,6],[2,9],[3,9],[4,9],[6,9],[8,9]]
# time = [3,5,7,1,8,2,5,7,4]

print(solution.minimumTime(n, relations, time))