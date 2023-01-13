#
# @lc app=leetcode.cn id=1802 lang=python3
#
# [1802] 有界数组中指定下标处的最大值
#

# @lc code=start
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:

        l, r = 0, maxSum + 1
        maxSum -= n
        while l + 1 != r:
            m = (l + r) >> 1
            x, y = m - index - 1, m - n + index
            s = m * m
            s1 = max(0, x) * (x + 1) // 2
            s2 = max(y, 0) * (y + 1) // 2
            if s - s1 - s2 <= maxSum:
                l = m
            else:
                r = m
        return r
            
# @lc code=end

