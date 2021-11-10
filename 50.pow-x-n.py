#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
# 迭代快速幂
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 快速幂
        def quickPow(x: float, n: int) -> float:
            ans = 1
            while n:
                if n & 1: ans *= x
                x *= x
                n >>= 1
            return ans
        return quickPow(x, n) if n > 0 else quickPow(1.0 / x, -n)
# @lc code=end

# 递归快速幂
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 快速幂
        def quickPow(x: float, n: int) -> float:
            if n == 0: return 1.0
            y = quickPow(x, n // 2)
            return y * y if n % 2 == 0 else y * y * x
        return quickPow(x, n) if n > 0 else quickPow(1.0 / x, n)