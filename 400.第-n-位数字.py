#
# @lc app=leetcode.cn id=400 lang=python3
#
# [400] 第 N 位数字
#

# @lc code=start
class Solution:
    def findNthDigit(self, n: int) -> int:
        # 第一步计算出target是几位数
        base = 9
        digits = 1
        while n - base * digits > 0:
            n -= base * digits
            base *= 10
            digits += 1
        # 计算target的值
        idx = n % digits
        if idx == 0:
            idx = digits
        target = 1
        for i in range(1, digits):
            target *= 10
        if idx == digits:
            target += n // digits - 1
        else:
            target += n // digits

        # 找到target中对应的数字
        for i in range(idx, digits):
            target //= 10
        
        return target % 10

# @lc code=end

