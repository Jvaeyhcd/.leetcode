#
# @lc app=leetcode.cn id=537 lang=python3
#
# [537] 复数乘法
#

# @lc code=start
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a1, b1 = num1.split('+')
        a2, b2 = num2.split('+')
        
        b1 = b1[:-1]
        b2 = b2[:-1]

        a = int(a1) * int(a2) - int(b1) * int(b2)
        b = int(a1) * int(b2) + int(a2) * int(b1)
        
        ans = str(a) + '+' + str(b) + 'i'
        return ans
# @lc code=end
solution = Solution()
num1 = "1+-1i"
num2 = "1+-1i"
print(solution.complexNumberMultiply(num1, num2))