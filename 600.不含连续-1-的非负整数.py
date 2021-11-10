#
# @lc app=leetcode.cn id=600 lang=python3
#
# [600] 不含连续1的非负整数
#

# @lc code=start
class Solution:
    def findIntegers(self, n: int) -> int:
        N = 31
        dp = [0] * N
        dp[0] = 1
        dp[1] = 1
        for i in range(2, N):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        pre = 0
        ans = 0

        for i in range(N - 2, -1, -1):
            val = 1 << i
            if n & val:
                ans += dp[i + 1]
                if pre == 1:
                    break
                pre = 1
            else:
                pre = 0
            
            if i == 0:
                ans += 1
        return ans
# @lc code=end

