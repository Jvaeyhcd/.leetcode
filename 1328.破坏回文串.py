#
# @lc app=leetcode.cn id=1328 lang=python
#
# [1328] 破坏回文串
#

# @lc code=start
class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        n = len(palindrome)
        arr = list(palindrome)
        if n < 2:
            return ''
        find = False
        # 前面能替换成a的都替换成a，不能替换的最后一个替换为b
        for i in range(n / 2):
            if arr[i] != 'a':
                arr[i] = 'a'
                return ''.join(arr)
        arr[n - 1] = 'b'
        return ''.join(arr)

# @lc code=end

