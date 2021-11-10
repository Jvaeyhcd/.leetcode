#
# @lc app=leetcode.cn id=7 lang=python
#
# [7] 整数反转
#

# @lc code=start
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(abs(x))
        positive = x >= 0
        ans = int(s[::-1])
        if ans < -2147483648 or ans > 2147483647:
            return 0
        return ans if positive else -ans
# @lc code=end

