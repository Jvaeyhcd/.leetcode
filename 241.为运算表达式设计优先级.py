#
# @lc app=leetcode.cn id=241 lang=python3
#
# [241] 为运算表达式设计优先级
#

# @lc code=start
from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]
        
        ans = []
        for i, c in enumerate(expression):
            if c in '+-*':
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for l in left:
                    for r in right:
                        if c == '+':
                            ans.append(l + r)
                        elif c == '-':
                            ans.append(l - r)
                        elif c == '*':
                            ans.append(l * r)
        return ans
# @lc code=end

solution = Solution()
expression = "2*3-4*5"
print(solution.diffWaysToCompute(expression))
