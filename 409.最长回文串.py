#
# @lc app=leetcode.cn id=409 lang=python
#
# [409] 最长回文串
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnts = collections.defaultdict(int)
        for c in s:
            cnts[c] += 1
        
        ans = 0
        odd = False
        for c in cnts.keys():
            if cnts[c] % 2 == 0:
                ans += cnts[c]
            else:
                ans += (cnts[c] - 1)
                odd = True
        
        if odd: ans += 1
        return ans


# @lc code=end

