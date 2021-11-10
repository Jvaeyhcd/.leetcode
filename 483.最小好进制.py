#
# @lc app=leetcode.cn id=483 lang=python
#
# [483] 最小好进制
#

# @lc code=start
class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        num = int(n)
        for i in range(num.bit_length(), 2, -1):
            left, right = 2, num - 1
            while left <= right:
                mid = (left + right) // 2
                s = mid * num - num - pow(mid, i) + 1
                if s == 0:
                    return str(mid)
                elif s > 0:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return str(num - 1)
# @lc code=end

