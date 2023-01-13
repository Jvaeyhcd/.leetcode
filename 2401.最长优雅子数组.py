#
# @lc app=leetcode.cn id=2401 lang=python3
#
# [2401] 最长优雅子数组
#

# @lc code=start
from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        mask = 0
        ans = 0
        l = 0
        for r, num in enumerate(nums):
            while mask and mask & num:
                mask ^= nums[l]
                l += 1
            mask |= num
            if ans < r - l + 1:
                ans = r - l + 1
        return ans
# @lc code=end

