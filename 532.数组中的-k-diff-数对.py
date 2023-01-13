#
# @lc app=leetcode.cn id=532 lang=python3
#
# [532] 数组中的 k-diff 数对
#

# @lc code=start
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        
# @lc code=end

