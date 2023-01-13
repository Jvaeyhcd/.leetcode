#
# @lc app=leetcode.cn id=646 lang=python3
#
# [646] 最长数对链
#

# @lc code=start
from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs.sort(key=lambda x:x[1])
        cur, ans = -float('inf'), 0
        for x, y in pairs:
            if cur < x:
                cur = y
                ans += 1
        return ans

# @lc code=end

