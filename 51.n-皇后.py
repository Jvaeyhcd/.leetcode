#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = [-1 for _ in range(n)]
        ans = []

        def calcNqueens(row: int):
            if row == n:
                ans.append(printQueens(result))
                return
            for col in range(n):
                if isOk(row, col):
                    result[row] = col
                    calcNqueens(row + 1)

        
        def isOk(row: int, col: int) -> bool:
            leftup, rightup = col - 1, col + 1
            for i in range(row - 1, -1, -1):
                if result[i] == col:
                    return False
                if leftup >= 0 and result[i] == leftup:
                    return False
                if rightup < n and result[i] == rightup:
                    return False
                leftup -= 1
                rightup += 1
            return True

        
        def printQueens(result: List[int]) -> List[str]:
            res = []
            for row in range(n):
                s = ''
                for col in range(n):
                    if result[row] == col:
                        s += 'Q'
                    else:
                        s += '.'
                res.append(s)
            return res

        
        calcNqueens(0)
        return ans
# @lc code=end

S = Solution()
n = 4
print(S.solveNQueens(n))