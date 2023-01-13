#
# @lc app=leetcode.cn id=736 lang=python3
#
# [736] Lisp 语法解析
#

# @lc code=start
import collections


class Solution:
    def evaluate(self, expression: str) -> int:
        i, n = 0, len(expression)

        def parseInt() -> int:
            nonlocal i
            sign, x = 1, 0
            if expression[i] == '-':
                sign = -1
                i += 1
            while i < n and expression[i].isdigit():
                x = x * 10 + int(expression[i])
                i += 1
            return sign * x
        
        def parseVar() -> str:
            nonlocal i
            i0 = i
            while i < n and expression[i] != ' ' and expression[i] != ')':
                i += 1
            return expression[i0:i]

        scope = collections.defaultdict(list)

        def innerEvaluate() -> int:
            nonlocal i
            if expression[i] != '(':
                if expression[i].islower():
                    return scope[parseVar()][-1]
                return parseInt()
            i += 1

            if expression[i] == 'l':
                i += 4
                vars = []
                while True:
                    if not expression[i].islower():
                        ret = innerEvaluate()
                        break
                    var = parseVar()
                    if expression[i] == ')':
                        ret = scope[var][-1]
                        break
                    vars.append(var)
                    i += 1
                    scope[var].append(innerEvaluate())
                    i += 1

                for var in vars:
                    scope[var].pop()
            elif expression[i] == 'a':
                i += 4
                e1 = innerEvaluate()
                i += 1
                e2 = innerEvaluate()
                ret = e1 + e2
            elif expression[i] == 'm':
                i += 5
                e1 = innerEvaluate()
                i += 1
                e2 = innerEvaluate()
                ret = e1 * e2
            i += 1
            return ret
        
        return innerEvaluate()
# @lc code=end

