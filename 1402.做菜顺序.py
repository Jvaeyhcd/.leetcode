#
# @lc app=leetcode.cn id=1402 lang=python3
#
# [1402] 做菜顺序
#

# @lc code=start
from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        presum, ans = 0, 0
        for si in satisfaction:
            if presum + si > 0:
                presum += si
                ans += presum
            else:
                break
        return ans
# @lc code=end

