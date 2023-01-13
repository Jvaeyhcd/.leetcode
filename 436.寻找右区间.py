#
# @lc app=leetcode.cn id=436 lang=python3
#
# [436] 寻找右区间
#

# @lc code=start
from bisect import bisect_left
from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        for i, interval in enumerate(intervals):
            interval.append(i)
        intervals.sort()

        n = len(intervals)
        ans = [-1] * n
        for _, end, i in intervals:
            idx = bisect_left(intervals, [end])
            if idx < n:
                ans[i] = intervals[idx][2]
        return ans

# @lc code=end
intervals = [[3,4],[2,3],[1,2]]
# intervals = [[1,4],[2,3],[3,4]]
intervals = [[1,12],[2,9],[3,10],[13,14],[15,16],[16,17]]
# intervals = [[1,2],[2,3],[0,1],[3,4]]
solution = Solution()
print(solution.findRightInterval(intervals))
