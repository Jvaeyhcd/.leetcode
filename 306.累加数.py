#
# @lc app=leetcode.cn id=306 lang=python3
#
# [306] 累加数
#

# @lc code=start
from functools import lru_cache


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        # 分别表示三个数的起始位置
        @lru_cache(None)
        def dfs(l1, l2, l3):
            if l3 > n or l2 > n - 1 or (num[l1] == '0' and l2 - l1 > 1):
                return False
            if l2 >= l3:
                return dfs(l1, l2, l3 + 1)
            if num[l2] == '0' and l3 - l2 > 1:
                return dfs(l1, l2 + 1, l3)
            
            num3 = self.addString(num[l1:l2], num[l2:l3])
            if len(num3) > n - l3:
                return False
            if num3 == num[l3:l3+len(num3)] and (l3 + len(num3) == len(num) or dfs(l2, l3, l3 + len(num3))):
                return True
            
            return dfs(l1, l2 + 1, l3) or dfs(l1, l2, l3 + 1)
        
        return dfs(0, 1, 2)


    # 大数加法
    def addString(self, num1: str, num2: str) -> str:
        ans = ''
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            t = n1 + n2 + carry
            carry = t // 10
            ans = str(t % 10) + ans
            i -= 1
            j -= 1
        return str(carry) + ans if carry > 0 else ans
# @lc code=end

solution = Solution()
input = '199100199'
print(solution.isAdditiveNumber(input))