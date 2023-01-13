#
# @lc app=leetcode.cn id=2400 lang=python3
#
# [2400] 恰好移动 k 步到达某一位置的方法数目
#

# @lc code=start
from math import comb


class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        d = abs(startPos - endPos)
        if k < d or (k - d) & 1:
            return 0
        return comb(k, d + (k - d) // 2) % 1_000_000_007
# @lc code=end

