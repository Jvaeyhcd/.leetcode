#
# @lc app=leetcode.cn id=479 lang=python3
#
# [479] 最大回文数乘积
#

# @lc code=start
class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1: return 9
        upper = 10**n - 1
        for left in range(upper, upper // 10, -1):
            p, x = left, left
            while x:
                p = p * 10 + x % 10
                x //= 10
            x = upper
            while x * x >= p:
                if p % x == 0:
                    return p % 1337
                x -= 1
# @lc code=end

