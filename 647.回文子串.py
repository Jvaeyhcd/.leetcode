#
# @lc app=leetcode.cn id=647 lang=python
#
# [647] 回文子串
#

# @lc code=start
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        str = '#'
        for c in s:
            str += (c + '#')
        
        n = len(s)
        str_len = 2 * n + 1
        p = [0] * str_len
        maxRight, center = 0, 0
        # 所有回文子串的数量
        ans = 0
        for i in range(str_len):
            mirror = (2 * center) - i
            if i < maxRight:
                p[i] = min(maxRight - i, p[mirror])
            
            left = i - (1 + p[i])
            right = i + (1 + p[i])
            while left >= 0 and right < str_len and str[left] == str[right]:
                p[i] += 1
                left -= 1
                right += 1
            
            if i + p[i] > maxRight:
                maxRight = i + p[i]
                center = i
            
            if str[i] == '#':
                # 中心是分隔符#
                ans += p[i] // 2
            else:
                # 中心不是分隔符
                ans += (p[i] + 1) // 2
            
        return ans

# @lc code=end

