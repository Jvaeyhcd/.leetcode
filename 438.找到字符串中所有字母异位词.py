#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
from typing import List
import collections


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)
        if s_len < p_len: return []

        orda = ord('a')
        ans = []
        count = [0] * 26
        for i in range(p_len):
            count[ord(s[i]) - orda] += 1
            count[ord(p[i]) - orda] -= 1
        
        # 不一样的个数
        diff = [c != 0 for c in count].count(True)
        if diff == 0:
            ans.append(0)

        for i in range(s_len - p_len):
            if count[ord(s[i]) - orda] == 1:
                diff -= 1
            elif count[ord(s[i]) - orda] == 0:
                diff += 1
            count[ord(s[i]) - orda] -= 1

            if count[ord(s[i + p_len]) - orda] == -1:
                diff -= 1
            elif count[ord(s[i + p_len]) - orda] == 0:
                diff += 1
            count[ord(s[i + p_len]) - orda] += 1

            if diff == 0:
                ans.append(i + 1)

        return ans
# @lc code=end

