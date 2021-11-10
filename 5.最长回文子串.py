#
# @lc app=leetcode.cn id=5 lang=python
#
# [5] 最长回文子串
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 给字符串添加分隔符
        def addBoundaries(s, divide):
            new_str = divide
            for c in s:
                new_str += (c + divide)
            return new_str
        
        n = len(s)
        if n < 2:
            return s
        
        new_str = addBoundaries(s, '#')
        new_len = 2 * n + 1
        p = [0] * new_len
        # 当前最长回文子串的中心
        center = 0
        # 当前最长回文子串的最右边界
        maxRight = 0
        
        # 当前遍历的中心最大扩散步数，其值等于原始字符串的最长回文子串的长度
        max_len = 1
        # 原始字符串的最长回文子串的其实位置，与max_len必须同时更新
        start = 0

        for i in range(new_len):
            # 以center为中心的i的对称点
            mirror = (2 * center) - i
            if i < maxRight:
                p[i] = min(maxRight - i, p[mirror])
            
            # 尝试扩散左右点
            left = i - (1 + p[i])
            right = i + (1 + p[i])

            # left >= 0 并且 right < new_len保证不越界
            # new_str[left] == new_str[right]表示可以扩散
            while left >= 0 and right < new_len and new_str[left] == new_str[right]:
                p[i] += 1
                left -= 1
                right += 1
            
            # 根据maxRight的定义，它是遍历过的i的i+p[i]的最大者
            # 如果maxRight的值越大，进入上面i < maxRight判断的可能性就越大，这样可以重复
            if i + p[i] > maxRight:
                # maxRight和center需要同时更新
                maxRight = i + p[i]
                center = i
            
            if p[i] > max_len:
                # 记录最长回文子串的长度和相应它在原始字符串中的起点
                max_len = p[i]
                start = (i - max_len) / 2
        print p
        return s[start:start + max_len]
# @lc code=end

