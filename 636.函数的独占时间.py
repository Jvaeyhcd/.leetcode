#
# @lc app=leetcode.cn id=636 lang=python3
#
# [636] 函数的独占时间
#

# @lc code=start
from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        stack = []
        for log in logs:
            i, tp, t = log.split(':')
            i, t = int(i), int(t)
            if tp[0] == 's':
                if stack:
                    ans[stack[-1][0]] += t - stack[-1][1]
                    stack[-1][1] = t
                stack.append([i, t])
            else:
                ii, tt = stack.pop()
                ans[ii] += t - tt + 1
                if stack:
                    stack[-1][1] = t + 1
        return ans
# @lc code=end

