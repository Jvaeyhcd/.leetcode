#
# @lc app=leetcode.cn id=13 lang=python
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        ans = 0
        n = len(s)
        for i in range(n):
            value = dic[s[i]]
            if i < n - 1 and value < dic[s[i + 1]]:
                ans -= value
            else:
                ans += value
        return ans
# @lc code=end

