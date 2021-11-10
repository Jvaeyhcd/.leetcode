#
# @lc app=leetcode.cn id=441 lang=python3
#
# [441] 排列硬币
#

# @lc code=start
# 二分法
class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        while l < r:
            mid = (l + r + 1) >> 1
            if mid * (mid + 1) <= 2 * n:
                l = mid
            else:
                r = mid - 1
        return l
# @lc code=end

