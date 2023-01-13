#
# @lc app=leetcode.cn id=788 lang=python3
#
# [788] 旋转数字
#

# @lc code=start
from functools import lru_cache


class Solution:
    def rotatedDigits(self, n: int) -> int:
        s = str(n)
        DIFFS = (0, 0, 1, -1, -1, 1, 1, -1, 0, 1)

        @lru_cache(None)
        def f(i: int, has_diff: bool, is_limit: bool) -> int:
            if i == len(s):
                return has_diff
            res = 0
            up = int(s[i]) if is_limit else 9
            for d in range(0, up + 1):
                if DIFFS[d] != -1:
                    res += f(i + 1, has_diff or DIFFS[d], is_limit and d == up)
            return res
        return f(0, False, True)
# @lc code=end

