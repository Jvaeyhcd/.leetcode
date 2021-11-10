#
# @lc app=leetcode.cn id=260 lang=python3
#
# [260] 只出现一次的数字 III
#

# @lc code=start
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xornum = 0
        for num in nums:
            xornum ^= num
        lsb = xornum & (-xornum)
        num1 = num2 = 0
        for num in nums:
            if lsb & num:
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]
# @lc code=end

