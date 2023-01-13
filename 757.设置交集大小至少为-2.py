#
# @lc app=leetcode.cn id=757 lang=python3
#
# [757] 设置交集大小至少为2
#

# @lc code=start
from typing import List


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[1], -x[0]))
        a, b, ans = -1, -1, 0
        for l, r in intervals:
            if l > b:
                a, b, ans = r - 1, r, ans + 2
            elif l > a:
                a, b, ans = b, r, ans + 1
        return ans
# @lc code=end

