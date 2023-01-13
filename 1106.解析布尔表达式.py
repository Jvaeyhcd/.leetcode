#
# @lc app=leetcode.cn id=1106 lang=python3
#
# [1106] 解析布尔表达式
#

# @lc code=start
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        st = []
        for c in expression:
            if c == ',': continue
            if c != ')':
                st.append(c)
                continue
            t = f = 0
            while st[-1] != '(':
                if st.pop() == 't': t += 1
                else: f += 1
            st.pop()
            op = st.pop()
            if op == '!':
                st.append('t' if f == 1 else 'f')
            elif op == '&':
                st.append('t' if f == 0 else 'f')
            elif op == '|':
                st.append('t' if t != 0 else 'f')
        return st[-1] == 't'
# @lc code=end

