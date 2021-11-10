# -*- coding: UTF-8 -*-
#
# @lc app=leetcode.cn id=301 lang=python3
#
# [301] 删除无效的括号
#

# @lc code=start
from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = set()
        # 最少需要删除的符号个数
        def need_remove(s: str) -> List[int]:
            stack = []
            count = 0
            for c in s:
                if c == '(':
                    stack.append(c)
                elif c == ')':
                    if stack:
                        stack.pop()
                    else:
                        count += 1
            return [len(stack), count]

        # 校验是否括号是否合法正确
        def check_parentheses(s: str):
            stack = []
            for c in s:
                if c == '(': stack.append(c)
                elif c == ')': 
                    if stack: 
                        stack.pop()
                    else:
                        return False
            return len(stack) == 0
        
        # 删除括号
        def remove_parentheses(cur: str, start: int, left_count: int, right_count: int):
            if left_count == 0 and right_count == 0:
                if check_parentheses(cur): res.add(cur)
                return
            
            n = len(cur)
            for i in range(start, n):
                if i > start and cur[i] == cur[i - 1]:
                    continue
                if left_count + right_count > n - i:
                    break

                nxt = cur[:i] + cur[i+1:]
                if cur[i] == '(' and left_count > 0:
                    remove_parentheses(nxt, i, left_count - 1, right_count)
                elif cur[i] == ')' and right_count > 0:
                    remove_parentheses(nxt, i, left_count, right_count - 1)
        
        # 需要删除的左边括号和右边括号的数量
        remove_left, remove_right = need_remove(s)
        print(remove_left, remove_right)
        remove_parentheses(s, 0, remove_left, remove_right)

        return list(res)
# @lc code=end

solution = Solution()
print(solution.removeInvalidParentheses("))(((((()())(()"))