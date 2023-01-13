#
# @lc app=leetcode.cn id=1036 lang=python3
#
# [1036] 逃离大迷宫
#

# @lc code=start
import collections
from typing import List

BOUND = int(1e6)
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        n = len(blocked)
        max_step = n * (n - 1) // 2

        blocked = {tuple(p) for p in blocked}
        
        def bfs(start: List[int], end: List[int]) -> bool:
            start, end = tuple(start), tuple(end)
            visited = {start}
            queue = collections.deque([start])

            step = 0
            while queue:
                u = queue.popleft()
                step += 1
                if step > max_step or u == end:
                    return True
                for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    v = (u[0] + dx, u[1] + dy)
                    if 0 <= v[0] < BOUND and 0 <= v[1] < BOUND and v not in blocked and v not in visited:
                        queue.append(v)
                        visited.add(v)

            return False

        return bfs(source, target) and bfs(target, source)


# @lc code=end

