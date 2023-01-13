#
# @lc app=leetcode.cn id=1665 lang=python3
#
# [1665] 完成所有任务的最少初始能量
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x:(x[1]-x[0], [0]), reverse=True)
        ans = 0
        cur = 0
        for actual, mininum in tasks:
            if cur < mininum:
                ans += (mininum - cur)
                cur = mininum
            cur -= actual
        return ans

# @lc code=end
tasks = [[1,3],[2,4],[10,11],[10,12],[8,9]]
tasks = [[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]
solution = Solution()
print(solution.minimumEffort(tasks))