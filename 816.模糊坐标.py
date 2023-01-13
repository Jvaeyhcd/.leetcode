#
# @lc app=leetcode.cn id=816 lang=python3
#
# [816] 模糊坐标
#

# @lc code=start
from typing import List

# 穷举法
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        
        ans = []
        for i in range(2, len(s) - 1):
            for left in self.make(s, 1, i):
                for right in self.make(s, i, len(s) - 1):
                    ans.append('(' + left + ', ' + right + ')')

        return ans
    
    def make(self, s: str, i: int, j: int) -> List[str]:
        ans = []
        for d in range(1, j - i + 1):
            left = s[i:i+d]
            right = s[i+d:j]
            if (not left.startswith('0') or left == '0') and not right.endswith('0'):
                ans.append(left + ('.' if d < j - i else '') + right)
        return ans
# @lc code=end

solution = Solution()
s = "(123)"
print(solution.ambiguousCoordinates(s))
