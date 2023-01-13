#
# @lc app=leetcode.cn id=1235 lang=python3
#
# [1235] 规划兼职工作
#

# @lc code=start
from bisect import bisect_right
from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = sorted(zip(startTime, endTime, profit), key=lambda p: p[1])
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            k = bisect_right(jobs, jobs[i - 1][0], hi=i, key=lambda p: p[1])
            dp[i] = max(dp[i - 1], dp[k] + jobs[i - 1][2])
        return dp[n]
# @lc code=end

