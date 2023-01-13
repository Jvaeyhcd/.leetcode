#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        ans, t = 0, 0
        for ch in s:
            if ch == '(':
                stack.append('(')
            elif ch == ')':
                if stack:
                    stack.pop()
                    t += 1
                else:
                    t = 0
                if not stack:
                    ans = max(ans, t * 2)
        return ans
# @lc code=end
s = ")()())"
s = ""
s = "(()"
s = "()(()"
solution = Solution()
print(solution.longestValidParentheses(s))