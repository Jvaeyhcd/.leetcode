#
# @lc app=leetcode.cn id=22 lang=python
#
# [22] 括号生成
#

# @lc code=start
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def backtrack(S, left, right):
            if len(S) == n * 2:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left + 1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right + 1)
                S.pop()
        
        backtrack([], 0, 0)
        return ans
# @lc code=end

