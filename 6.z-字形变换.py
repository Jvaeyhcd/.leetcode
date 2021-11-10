#
# @lc app=leetcode.cn id=6 lang=python
#
# [6] Z 字形变换
#

# @lc code=start
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        N = len(s)
        print N
        arr = ['' for _ in range(numRows)]
        loop = 2 * numRows - 2
        if numRows == 1:
            loop = 1
        for i in range(N):
            remainder = i % loop
            if remainder < numRows:
                arr[remainder] += s[i]
            else:
                arr[loop - remainder] += s[i]
        
        return ''.join(arr)

# @lc code=end

