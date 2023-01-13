#
# @lc app=leetcode.cn id=630 lang=python3
#
# [630] 课程表 III
#

# @lc code=start
from typing import List
import heapq


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda c:c[1])
        q = list()
        total = 0
        for ti, di in courses:
            if total + ti <= di:
                total += ti
                heapq.heappush(q, -ti)
            elif q and -q[0] > di:
                total -= -q[0] - ti
                heapq.heappop(q)
                heapq.heappush(q, -ti)
        
        return len(q)

# @lc code=end

