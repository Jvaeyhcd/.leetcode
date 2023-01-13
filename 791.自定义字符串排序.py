#
# @lc app=leetcode.cn id=791 lang=python3
#
# [791] 自定义字符串排序
#

# @lc code=start
from typing import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = Counter(s)
        ans = []
        for c in order:
            ans.append(c * counter[c])
            counter[c] = 0
        
        for c in counter:
            ans.append(c * counter[c])
        
        return ''.join(ans)
# @lc code=end

