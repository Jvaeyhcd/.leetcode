#
# @lc app=leetcode.cn id=1763 lang=python3
#
# [1763] 最长的美好子字符串
#

# @lc code=start
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        if n < 2: return ""
        for i, c in enumerate(s):
            if c.upper() not in s or c.lower() not in s:
                return max(self.longestNiceSubstring(s[:i]), self.longestNiceSubstring(s[i+1:]), key=len)
        return s

# @lc code=end
solution = Solution()
s = "YazaAay"
s = "Bb"
s = "c"
s = "dDzeE"
s = "qQUjJ"
print(solution.longestNiceSubstring(s))
