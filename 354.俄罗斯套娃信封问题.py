#
# @lc app=leetcode.cn id=354 lang=python3
#
# [354] 俄罗斯套娃信封问题
#

# @lc code=start
from bisect import bisect_left
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        n = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        nums = [h for _, h in envelopes]
        stack = []
        for num in nums:
            idx = bisect_left(stack, num)
            if idx == len(stack):
                stack.append(num)
            else:
                stack[idx] = num
        return len(stack)
# @lc code=end

