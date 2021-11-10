#
# @lc app=leetcode.cn id=371 lang=python3
#
# [371] 两整数之和
#

# @lc code=start
MASK1 = 2 ** 32
MASK2 = 2 ** 31
MASK3 = MASK2 - 1
class Solution:
    def getSum(self, a: int, b: int) -> int:
        a %= MASK1
        b %= MASK1
        while b != 0:
            carry = ((a & b) << 1) % MASK1
            a = (a ^ b) % MASK1
            b = carry
        
        if a & MASK2:
            return ~((a ^ MASK2) ^ MASK3)
        else:
            return a
# @lc code=end

