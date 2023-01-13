#
# @lc app=leetcode.cn id=1723 lang=python3
#
# [1723] 完成所有工作的最短时间
#

# @lc code=start
from typing import List


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:

        jobs.sort()
        l, r = max(jobs), sum(jobs)

        def backtrack(workloads: List[int], i: int, limit: int) -> bool:
            if i >= len(jobs):
                return True
            
            cur = jobs[i]
            for j in range(len(workloads)):
                if workloads[j] + cur <= limit:
                    workloads[j] += cur
                    if backtrack(workloads, i + 1, limit):
                        return True
                    workloads[j] -= cur

                if workloads[j] == 0 or workloads[j] + cur == limit:
                    break
            return False

        def check(limit: int) -> bool:
            workloads = [0] * k
            return backtrack(workloads, 0, limit)

        while l < r:
            mid = (l + r) >> 1
            if check(mid):
                r = mid
            else:
                l = mid + 1
        
        return l

# @lc code=end

