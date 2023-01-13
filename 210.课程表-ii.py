#
# @lc app=leetcode.cn id=210 lang=python3
#
# [210] 课程表 II
#

# @lc code=start
import collections
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indeg = [0 for _ in range(numCourses)]
        graph = collections.defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)
            indeg[a] += 1
        ans = []
        queue = collections.deque(i for i in range(numCourses) if indeg[i] == 0)
        while queue:
            u = queue.popleft()
            ans.append(u)
            for v in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    queue.append(v)
        return ans if len(ans) == numCourses else []
# @lc code=end

