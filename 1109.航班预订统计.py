#
# @lc app=leetcode.cn id=1109 lang=python3
#
# [1109] 航班预订统计
#

# @lc code=start
from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diffs = [0] * (n + 1)
        for l, r, seat in bookings:
            diffs[l - 1] += seat
            diffs[r] -= seat
        ans = [0] * n
        ans[0] = diffs[0]
        for i in range(1, n):
            ans[i] = ans[i - 1] + diffs[i]
        return ans
# @lc code=end

