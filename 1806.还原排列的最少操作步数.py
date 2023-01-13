#
# @lc app=leetcode.cn id=1806 lang=python3
#
# [1806] 还原排列的最少操作步数
#

# @lc code=start
class Solution:
    def reinitializePermutation(self, n: int) -> int:
        x = n // 2
        ans = 1
        while x != 1:
            if x % 2:
                x = (x + n - 1) // 2
            else:
                x //= 2
            ans += 1
        return ans
# @lc code=end

