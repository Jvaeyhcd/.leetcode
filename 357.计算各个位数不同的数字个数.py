#
# @lc app=leetcode.cn id=357 lang=python3
#
# [357] 计算各个位数不同的数字个数
#

# @lc code=start
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        for i in range(1, n + 1):
            add = 9
            for j in range(i - 1):
                add *= (9 - j)
            dp[i] = add + dp[i - 1]
        return dp[n]

# @lc code=end

