#
# @lc app=leetcode.cn id=1201 lang=python3
#
# [1201] 丑数 III
#

# @lc code=start
import heapq
from math import lcm


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        ab, ac, bc = lcm(a, b), lcm(a, c), lcm(b, c)
        abc = lcm(a, b, c)
        l, r = min(a, b, c) - 1, int(2e9) + 1
        while l + 1 != r:
            mid = (l + r) >> 1
            cnt = mid // a + mid // b + mid // c - mid // ab - mid // ac - mid // bc + mid // abc
            if cnt < n:
                l = mid
            else:
                r = mid
        return r

# @lc code=end

