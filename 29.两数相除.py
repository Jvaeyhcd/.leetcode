#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MIN, MAX = -2147483648, 2147483647
        a, b, ans = abs(dividend), abs(divisor), 0
        for i in range(31, -1, -1):
            if (b << i) <= a:
                ans += 1 << i
                a -= b << i
        ans = ans if (dividend > 0) == (divisor > 0) else -ans
        return ans if MIN <= ans <= MAX else MAX
# @lc code=end

