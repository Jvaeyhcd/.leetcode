#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        arr = []
        graph = collections.defaultdict(list)
        indeg = [0 for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)
            indeg[a] += 1
        # arr中存储的是已安排的课程
        arr = []
        queue = collections.deque(i for i in range(numCourses) if indeg[i] == 0)
        while queue:
            u = queue.popleft()
            arr.append(u)
            for v in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    queue.append(v)
        # 已安排的课程不是所有的课程，那么将无法完成学习
        return len(arr) == numCourses


# @lc code=end

