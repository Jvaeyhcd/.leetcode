#
# @lc app=leetcode.cn id=461 lang=python
#
# [461] 汉明距离
#

# @lc code=start
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        dis = 0
        xor = x ^ y
        while xor:
            dis += 1
            xor = xor & (xor - 1)
        
        return dis
# @lc code=end

